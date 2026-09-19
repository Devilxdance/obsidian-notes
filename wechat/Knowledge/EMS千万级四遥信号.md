# 【致知—EMS】千万级四遥信号究竟对应多大的储能电站？

# 一、引言

这还要从一些EMS企业的宣传说起：为了体现自研EMS的性能实力，不少EMS企业宣称支持千万级四遥信号全接入。那么多大的储能电站才有千万点四遥信号？经学生计算，若采用314Ah电芯，单站点至少得5GWh；若采用587Ah电芯，单站点至少得9GWh。从目前国内储能电站单站装机规模来看，基本在GWh以内，那其实是没有这么大信号量的；有时候，不仅要看到厂家宣传的优势，也要去匹配自身的需求。

# 二、什么是四遥

简单说下吧，四遥指的是遥测、遥信、遥控、遥调；其中遥测和遥信是设备上送给系统的信息，遥控和遥调是系统对设备下发的控制指令。对于储能电站来说，EMS主要接入的设备包含PCS、BMS、箱变测控装置，其四遥信息简要描述如下：

- 遥测：模拟量，如电芯温度、电压、电流等信息；
    
- 遥信：数字量，0或1，如电芯主动均衡状态、开关机、告警信号、故障信号等；
    
- 遥控：数字量，0或1，如EMS下发开机、关机指令，合闸、分闸指令等；
    
- 遥调：模拟量，如EMS下发有功功率、无功功率等，不过要注意的是有的设备企业会把开关机指令归入遥调中。
    

# 三、储能电站四遥信号量的估算

储能电站内上送信息量最大的设备是BMS，BMS会上送电芯的温度、电压信息，这个是大头。若简单估算的话，根据电芯的数量就能算得七七八八了；若要详细一点分析，如下：

电芯温度和电压遥测

基于587Ah电芯，目前直流侧主流产品规格为6.25MWh，其成簇方式如下：

- 电池PACK：1P104S
    
- 电池簇：1P416S
    
- 电池堆：8P416S（单舱按一个电池堆考虑，不过也有设置2个电池堆的，即4簇1个电池堆接入一台1600kW PCS）
    

根据《GB/T 34131-2023 电力储能用电池管理系统》约定：电池模块内温度采集通道数应不小于模块内电池单体电压采集50%，宜与模块内电池池单体申压采集数量相同。

考虑到成本，常规的方案是每两个电芯配置1个温度采集点，当然也有1个电芯配置1个温度采集点的；另外，还需要在电池PACK正负极处配置温度采集点。基于此，就能知道单个PACK的温度和电压遥测信号量了。

电芯主动均衡遥信

常规被动均衡无此遥信，主动均衡才有，主要就是主动均衡使能标志即主动均衡是否开启的状态反馈。

其他设备的四遥信息就不一一列举了吧，学生做了一个四遥信号计算模板，供老师指导。虽然每个厂家的点表都有一些差异，但是整体四遥信号量级大差不差吧。

详细如下：

1. 储能电站典型四遥信号统计表：
    
    ![图片](https://mmbiz.qpic.cn/mmbiz_png/AwbsXcAibfCGsCqkqicvXp2O8sOicsT3ZHacYNZGCB253lI5Zl73MiaeLoia6v0uzn6gmwrdtPZwTT8rrR7cp9zyPnYibDian9rIMZsMmibsfEXlibEY/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)
    
2. 基于314Ah的储能单元四遥信号表：
    
    ![图片](https://mmbiz.qpic.cn/mmbiz_png/AwbsXcAibfCH0ntNH35vNXSHlFe9utGGiaBsITrpVTJTFc2HnNqKibLwiaK66hLOwicpreQrrIJ7t6nu9libMlHXNgq5DjqlYzHE7rRbOhluGLMx4/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)
    
      
    
3. 基于587Ah的储能单元四遥信号表：
    
    ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/AwbsXcAibfCEgGXeUL3qN5M7wicFZA9wYNFZysxEJuLPClcxeciacVj1iboCHpga0HIS2ZfJ5Bc71D33Q85ibGxr7ug8s8gvyLVxaBVb6ABruTNU/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)