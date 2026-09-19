# 连接方式详解：CV/CCV

**一、目的：**介绍海外项目常见PCS升压一体机的连接方式和常见问题与解答

**二、常见两种连接方式：**

1，**手拉手连接：**多套PCS升压一体机（PCS MV Station）连接到一个电网开关，中压开关柜常见配置CCV

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNhedSttJFlGrFYr23BicLDsexpwYPgIuMTLedAJLFqo7mFqEW7j0KyBqjDBofwUSHkNk8hjOAiaAuD8tZrBpvkCNCSTUvPTnpGyrVzBCuRdA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**图1****：CCV** **连接图**

**2，****单独连接：**一套PCS升压一体机连接一个电网开关，中压开关柜常见配置CV

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/zNhedSttJFkl2k6iaRupHwLJXvicoicjbu8g0tEF4p5ick8SWkr6w8Q5v95BMCyxOZRA7Eeic4S2MsGdzTRCRxI2upvPAKk9yT3M75xVR6bzcMbw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**图2****：CV** **连接图**

**备注：**PCS升压一体机集成中压开关柜，升压变压器和集中式PCS等，组成在集装箱中，交流侧连接中压电网，直流侧连接电池

**三、中压开关柜CCV****配置说明和适用场景：**

下图为PCS升压一体机的部分单线图，中压开关柜（Medium Voltage Switchgear）、升压变压器和PCS等

中压开关柜有三个柜，两个C柜（含负荷开关），一个V柜（含真空断路器），两个C柜的配置完全相同，因此，可以选择C柜连接到电网或下一个中压开关柜，**中压开关柜****CCV****配置的两个对外接口为两个C****柜**。V柜内部已经在出厂前连接完毕

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/zNhedSttJFlHkG4EjJT60jKhb9JCwAgRoo7SXiaS5BxHw8DiavCThLAqP8IVHPPqiaGDZ4IXldZgSfZCTjfdjnDq8wYFVpn7Q3QIcsnwU6AlUg/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

**图3****：CCV** **内部图**

**适用场景：****CCV****适用于电网连接点数量少于PCS** **升压一体机数量的场景**

如图1，只有一个电网连接点，但有三套PCS升压一体机，只有一套可以连接到电网，剩余手拉手连接

**四、中压开关柜CV****配置说明和适用场景：**

CV配置等于CCV减掉一个C柜，即CV中只有一个C柜和一个V柜，对外接口只有一个C柜接口

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNhedSttJFmmTXtVNnl3xLU80oB1AOqib64uuIbLeOiatkK1zVhjHadf4briaBOLpicwnZMJEZE11fTfyBZfibEZ7JwxgoT0s018aME9drLyKd0s/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**图4****：CV** **内部图**

**适用场景：CV****适用于电网连接点数量≥PCS****升压一体机数量的场景**，如图2所示

连接方式介绍完毕，接下来为常见的问题和解答

**常见****Q & A**

**（一）负荷开关、真空断路器和隔离开关的作用**

**1，****负荷开关（Load Switch****）（C****柜内）**

**作用：**负荷开关具有一定灭弧能力，可以切断正常电流，**但切勿在短路时操作**，因此负荷开关不能用作系统保护装置

**图示：**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/zNhedSttJFkqqC8oibn5POD51JqTs6zT3J3QCTd5Rb6cj2bbK1lPViaaWAiaSfbQZ1CbNyZZOk1aCW4vwViciaCCkjSUlM9uicThbuMPN9CicnETBc/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**2，****真空断路器（Vacuum Circuit Breaker****）（V****柜内）**

**作用：**真空断路器具有强大的灭弧功能，**可以切断正常电流和短路电流**，是系统主要保护装置

**图示：**![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNhedSttJFm2oiat2oibpicON8ic0IqHmYvcq62vlwbrVAmEa2iaSQbI44SbXNqib10QCc8GQQQ7FnOH6icLoVIV97K4O1aaqE6sf2GYKeOMRnEFnc/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**3，****隔离开关（Disconnector****）（V****柜内）**

**作用：**没有灭弧能力，**切勿在有电流时操作**。隔离开关在系统维护期间提供可见的物理断开点，确保人身安全

**图示：**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/zNhedSttJFm26nJxiagkKj9xX3rxLZmffYzDx3RGDKeTfWQ55lWXIgHhlQbM47IwPSD6HaUylJKENLLZ1gWbdShDvQozQNyhyk4AsibwxzaZo/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**总之，只有真空断路器才能在发生短路时作为保护装置使用**

**（二）如何选择****CCV****或****CV**

**1****，CCV****：**当PCS 升压一体机数量≥ 电网连接点数量时

**2****，CV****：**当PCS升压一体机数量≤ 电网连接点数量时

显然，CCV也能当成CV使用，但浪费一个C柜并不划算

**（三）一个电网连接点可以连接多少套****PCS****升压一体机****_CCV****配置**

假设：

1，电网电压为20kV

2，单套PCS升压一体机功率：5MW

3，中压开关柜的额定电流：630A

因此，20kV侧单套5MW升压一体机的额定电流为：（忽略效率损失）

144A=5MW/20kV/√3（20kV是线电压，所以除以根号3）

则：

630A/144A=4.375，因此CCV的最大数量为4

但请考虑开关柜温度和海拔的降额曲线。通常，很多供应商会更保守，他们可能会考虑电网电压的下限值并预留更多余量，以上结果供参考

查阅下图方便理解：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNhedSttJFkzecFZice7CKJpZSwhPxsgJshdzddiczr5R2UYMPXay27SnbgabrhiaEPvzdPgNAnwZdgYSaf0dXd57LDge4PHn19jpruPmXticCU/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

**图5****：CCV****连接图_****标注额定电流**

**（四）****PCS****升压一体机内部****AC****侧短路时，****CCV****和****CV****配置的影响范围**

**1****，CV**

PCS升压一体机内部AC侧的短路故障，**最劣势情况**将导致V柜中的真空断路器跳闸或电网侧的断路器跳闸

两种情况对储能系统影响范围是相同的：发生短路的PCS升压一体机将退出，而其他升压一体机不受影响

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/zNhedSttJFmjrre2Qz0tqQedtnqm7zofrnjJjthNgrbyicOuHVbT3U8HeQ7UU2DAicnzZurNwojZXwPcv0S7Ej3mXwnsKqRiab2TfJAQb8bia5A/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)

**图6****：CV****短路故障说明**

**2****，CCV**

CCV发生AC侧短路时，两种情况会导致不同结果

下图展示两套PCS升压一体机手拉手连接，接入一个电网连接点

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNhedSttJFlaiavhawqYk1tmZLrLG8nRGNPJbI8sjzgLPImPQuibHgxFchqU8xxk6Bz7MUrcic7r1UmYZ2nhicsspUC6ib6ErONyMiarF0icCRjna8/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

**图7****：CCV****短路故障说明**

**2.1****：**当V柜内真空断路器QF2，下游发生短路故障时（A点后，蓝线标记），最严重结果是V柜内的真空断路器QF2跳闸。其他升压一体机不受影响

**2.2****：**当V柜内真空断路器QF2，上游发生短路故障时，即在C柜和V柜共同交流母线或C柜中（B点之前，红线标记），因为C柜中的负荷开关无法切断短路电流

因此，电网侧断路器QF1将跳闸以保护整个系统。此时，将导致同一电网连接点下的所有升压一体机均退出运行

同时，当短路点A点和B点发生在任何一台中压开关柜内时，结果和上述表述相同

然而，在B点（红线）发生短路概率很小，因此问题不大

**中英文名词对照**

中压开关柜 Medium Voltage Switchgear/MV Switchgear

环网柜 RMU Ring Main Unit

负荷开关 Load Switch

真空断路器 Vacuum Circuit Breaker

隔离开关 Disconnector

短路 Short Circuit