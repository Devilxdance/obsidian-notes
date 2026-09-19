# GOOSE报文逐帧解析，带你看懂goose报文

# [小电工笔记调试工具箱](https://mp.weixin.qq.com/s/2jBoy7meNsw9ti12I8jIpA)

本文依据 IEC 61850 系列（国内等同采用为 DL/T 860）与 IEC 61850-8-1，系统梳理 61850 标准体系、GOOSE 报文封装结构、ASN.1 BER 编码、关键运行参数，并结合一条按标准构造、逐字节核算的完整 GOOSE 帧给出解析方法，可作为智能变电站过程层组网与协议栈开发的技术参考。

## 一、标准与体系

IEC 61850 是电力系统自动化领域唯一的全球通用国际标准《变电站通信网络与系统》，由 IEC TC57 制定（2004 发布，现行 Ed2.1）。其目标是实现不同厂商智能电子设备（IED）间的互操作性，是智能变电站、数字化变电站的"通用语言"。国内以电力行业标准 **DL/T 860 系列等同采用（IDT）IEC 61850**，并非 GB 强制国标；配套工程模型另有国家标准 GB/T 32890-2016《继电保护 IEC 61850 工程应用模型》（规定虚端子、虚连线）。

|国际部分|国内编号|内容|
|---|---|---|
|IEC 61850-1~5|DL/T 860.1~5|基本原则 / 术语 / 一般要求 / 系统管理 / 通信要求|
|IEC 61850-6|DL/T 860.6|变电站配置语言 SCL（ICD/SSD/SCD/CID）|
|IEC 61850-7-1~4|DL/T 860.71~74|基本通信结构（ACSI、公共数据、逻辑节点 LN）|
|IEC 61850-8-1|DL/T 860.81|SCSM：映射到 MMS + GOOSE（GOOSE 出处）|
|IEC 61850-9-2|DL/T 860.92|SCSM：采样值 SV 映射到以太网（合并单元 MU）|
|IEC 61850-10|DL/T 860.10|一致性测试|
|—|GB/T 32890-2016|继电保护工程应用模型|

核心分工：**ACSI**（IEC 61850-7-2）定义逻辑节点、数据对象、数据集、GOOSE/SV 控制块等抽象模型，与底层无关；**SCSM**将其映射到具体协议——站控层用 MMS（TCP/102），间隔层—过程层用 GOOSE（0x88B8）与 SV（0x88BA）；SCL（IEC 61850-6）用 XML 描述设备与拓扑，落实"一次建模、多次使用"。GOOSE 在 IEC 61850-7-2 中属 GSE（Generic Substation Event）模型，编码与映射由 IEC 61850-8-1 规定。

## 二、报文结构组成（以太网封装 + APDU）

GOOSE 直接封装在以太网帧中，无传统"链路层校验和"（依赖以太网 CRC-32）。完整帧 = 以太网帧头 + GOOSE 协议头 + GOOSE APDU（ASN.1 BER 编码的应用数据单元）：

目的MAC(6) 源MAC(6) VLAN(4)  
EtherType(2)=0x88B8  APPID(2) Length(2) Res1(2) Res2(2)  
APDU = 0x61(IECGoosePdu) + ASN.1 BER 字段序列

**以太网封装**：目的 MAC 使用 IEC 61850 专用多播段 `01-0C-CD-01-xx-xx`，末两字节与 APPID 对应；源 MAC 为发送 IED 物理地址；VLAN Tag（TPID 0x8100 + TCI）承载优先级与 VID；EtherType 固定 **0x88B8**（GSE=0x88B9，SV=0x88BA）。

**GOOSE 协议头**：APPID 为全站唯一的应用标识，GOOSE 范围 `0x0000–0x3FFF`（SV 为 0x4000–0x7FFF）；Length 为自 APPID 起至 APDU 结束的总字节数（含 APPID、Length、Res1、Res2 及 APDU 自身）；两字节 Reserved 置 0。

**GOOSE APDU**：以 `0x61`（APPLICATION [1] 构造型）起头，内部为一组 TLV（Tag-Length-Value）。关键字段与 TAG 见附录 A。其中 stNum 在每次数据变位时 +1（范围 0–4294967295，上电首帧=1），sqNum 在同一 stNum 下重发时递增；timeAllowedtoLive（TAL）为允许生存时间，订阅者据此判超时。

## 三、主要参数

|参数|取值 / 范围|说明|
|---|---|---|
|传输方式|以太网多播（发布/订阅）|无主从，一变多|
|多播 MAC|01-0C-CD-01-00-00 ~ 01-01-FF|GOOSE 专用；SV 用 01-0C-CD-04-xx-xx|
|EtherType|0x88B8|GOOSE（GSE=0x88B9，SV=0x88BA）|
|APPID|0x0000–0x3FFF|全站唯一，与 MAC 末两字节对应|
|VLAN PCP|4–7|高优先级转发|
|T0 / T1|5000 ms / 2 ms|心跳周期 / 变位首重传间隔|
|TAL|10000 ms（=2×T0）|超时判据；断链时间=2×TAL|
|stNum / sqNum|0–4294967295 / 0–n|状态号 / 顺序号|
|配置文件|ICD/SSD/SCD/CID|SCL 描述订阅关系|
|MMS 端口|TCP/102|站控层（非 GOOSE）|

变位重传时序：首次变位立即发（T0=0）→ 间隔 T1=2 ms → 2 ms → 4 ms → 8 ms → 16 ms（共 5 帧突发），随后恢复 T0 心跳。

## 四、报文案例（逐字节）

以下为按标准构造的合法 GOOSE 帧（示例值，已逐字节核算长度）。目的 MAC 末两字节 `00 04`与 APPID `00 04`对应；APDU 内容 191 字节，因 ≥128 按 BER 扩展长度编码为 `81 BF`；Length=0x00CA（202）。

01 0C CD 01 00 04 44 4D 35 30 30 30 81 00 80 00  
88 B8 00 04 00 CA 00 00 00 00 61 81 BF 80 1C 49 45  
44 31 2F 41 50 31 2F 4C 44 31 2F 58 43 42 52 31  
2E 47 4F 24 47 4F 4F 53 45 31 81 04 00 00 27 10  
82 1A 50 5F 4C 32 32 30 34 41 50 49 47 4F 2F 4C  
4C 4E 30 24 64 73 47 4F 4F 53 45 31 83 17 50 5F  
4C 32 32 30 34 41 50 49 47 4F 2F 4C 4C 4E 30 2E  
67 6F 63 62 31 84 08 68 07 68 04 9E 5C A2 0A 85  
04 00 00 00 83 86 04 00 00 00 0A 87 01 00 88 04  
00 00 00 01 89 01 00 8A 04 00 00 00 03 AB 3C A0  
12 83 01 00 84 03 03 00 00 91 08 68 07 68 04 9E  
5C A2 0A A0 12 83 01 01 84 03 03 00 00 91 08 68  
07 68 04 9E 5C B0 0A A0 12 83 01 00 84 03 03 00  
00 91 08 68 07 68 04 9E 5C C0 0A

|字节|字段|值 / 含义|
|---|---|---|
|0–5|目的 MAC|01 0C CD 01 00 04（GOOSE 多播）|
|6–11|源 MAC|44 4D 35 30 30 30（IED 物理地址）|
|12–15|VLAN|81 00 80 00（PCP=4，VID=0）|
|16–17|EtherType|88 B8（GOOSE）|
|18–19|APPID|00 04|
|20–21|Length|00 CA（=202）|
|22–25|Reserved1/2|00 00 00 00|
|26|APDU Tag|61（IECGoosePdu）|
|27–28|APDU Len|81 BF（内容 191 B）|
|29–30|gocbRef Len|80 1C（28 B）|
|31–58|gocbRef|IED1/AP1/LD1/XCBR1.GO$GOOSE1|
|59–64|timeAllowedtoLive|81 04 00 00 27 10（10000 ms）|
|65–66|datSet Len|82 1A（26 B）|
|67–92|datSet|P_L2204APIGO/LLN0$dsGOOSE1|
|93–94|goID Len|83 17（23 B）|
|95–117|goID|P_L2204APIGO/LLN0.gocb1|
|118–119|t Len|84 08（8 B）|
|120–127|t|68 07 68 04 9E 5C A2 0A|
|128–129|stNum Len|85 04|
|130–133|stNum|00 00 00 83（=131）|
|134–135|sqNum Len|86 04|
|136–139|sqNum|00 00 00 0A（=10）|
|140–142|simulation|87 01 00（False）|
|143–144|confRev Len|88 04|
|145–148|confRev|00 00 00 01（=1）|
|149–151|ndsCom|89 01 00（False）|
|152–153|numEnt Len|8A 04|
|154–157|numDatSetEntries|00 00 00 03（=3）|
|158–159|allData Len|AB 3C（60 B）|
|160–219|allData|3 个数据项（A0 12 + 值/品质/时标）|

stNum/sqNum 解析要点：稳态心跳每 T0 发一帧，stNum 不变、sqNum 自增，接收端刷新超时计时器；变位时 stNum+1 并连发 5 帧（sqNum 0→4），各帧 allData 反映新状态。接收端判据：stNum 变化 → 事件；sqNum 变化而 stNum 不变 → 同状态重传，取最新即可。

## 五、解析与抓包要点

- **Wireshark 过滤**
    
    ：`eth.type == 0x88b8`（或 `ether[12:2] == 0x88b8`）；按多播 MAC 限定：`ether dst host 01:0c:cd:01:00:00/ff:ff:ff:ff:00:00`。新版 Wireshark 内置 IEC 61850/GOOSE 解析器。
    
- **订阅过滤三步**
    
    ：接收端依次校验 目的 MAC（粗筛流量）→ APPID（区分业务流）→ goID（最终确认），全部匹配才解析，否则丢弃。
    
- **时间解码**
    
    ：t 的 8 字节 = 前 4 B Unix 纪元秒 + 中 3 B 小数秒（24 bit，精度 2⁻²⁴ s）+ 末 1 B 时间品质。上例 0x68076804 秒对应 2025-04-22 09:57:24（UTC），国内本地时间 +8 h。
    
- **断链判定**
    
    ：接收端持续收不到帧，计时累加；一旦 ≥ TAL → 上送 GOOSE 通信中断告警；工程判据常取 2×TAL。
    
- **配置一致性**
    
    ：gocbRef/datSet/goID/APPID 须与订阅端 SCD 一致；confRev 变更触发不一致告警。GOOSE 不自带应用层校验，依赖以太网 CRC-32。
    

## 附录 A：GOOSE APDU TAG 速查表

|TAG|字段|类别|
|---|---|---|
|0x61|IECGoosePdu|APPLICATION [1] 构造|
|0x80|gocbRef|上下文 [0]|
|0x81|timeAllowedtoLive|上下文 [1]|
|0x82|datSet|上下文 [2]|
|0x83|goID|上下文 [3]|
|0x84|t（UTC 时间）|上下文 [4]|
|0x85|stNum|上下文 [5]|
|0x86|sqNum|上下文 [6]|
|0x87|simulation|上下文 [7]|
|0x88|confRev|上下文 [8]|
|0x89|ndsCom|上下文 [9]|
|0x8A|numDatSetEntries|上下文 [10]|
|0xAB|allData|上下文 [11] 构造|

## 附录 B：与 101 / 104 / Modbus / CDT 对比

|维度|101|104|Modbus|CDT|61850/GOOSE|
|---|---|---|---|---|---|
|体系|IEC 60870-5-101|101+TCP|Modbus-IDA|DL 451|IEC 61850|
|国内|DL/T 634.5101|DL/T 634.5104|GB/T 19582|DL 451|DL/T 860|
|传输|串行 FT1.2|TCP/2404|串行/TCP|串行同步字|以太网多播|
|模式|问答|平衡|主从|循环上报|发布/订阅|
|帧标志|启动 68H|启动 68H|地址+CRC|EB90|88B8+APPID|
|实时性|低|低|低|中|毫秒级|

文章末尾留言获取详细PDF资料

参考标准：IEC 61850 系列、DL/T 860 系列、DL/T 860.81（GOOSE 映射）、GB/T 32890-2016、IEC 61850-8-1。本文报文案例为按标准构造的示例帧（APDU 总长 194 B，其中内容 191 B；Length=0x00CA），用于说明字段排布，现场实际帧以装置配置与 SCD 为准。