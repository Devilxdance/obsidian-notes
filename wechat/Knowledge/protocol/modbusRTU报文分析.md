
报文格式，报文全部为16进制，遥信状态需要转换为二进制：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/qUkcN24ENacK5ibSFxOjwUMagvNggrYMAMmL0rC95uhyVxh092jR1fCkPVIzySEBqLbqZB5cNxMRJ2CaBgicZiaiaQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/qUkcN24ENacK5ibSFxOjwUMagvNggrYMAOKWBHicMPE1XLUVUkgicEJPicpj7f3Fbibc5ulPztKTV4P8MQ9JHhViavLg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/qUkcN24ENacK5ibSFxOjwUMagvNggrYMAyc9w98jDBsu7RkBru6krgK97icicK42hz8fQOOgL0icWQrDzHJzjjG0bw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)报文实例

01H功能码读取输出线圈：

发送报文格式：从站地址 + 功能码 + 开始线圈地址 + 线圈数量 + CRC

接收报文格式：从站地址 + 功能码 + 字节计数 + 数据 + CRC

我们观察一下报文：

发送报文：01 01 00 0A 00 14 1C 07

接收报文：01 01 03 C7 C0 00 DD B3

报文解析：

发送报文 :01（从站地址）01（功能码）00 0A（开始线圈地址，占用两个字节，高位取0，0A换算为十进制为10，从地址10开始读取）00 14（线圈数量，也占用两个字节，14十六进制换算为十进制为20，读取20个线圈数量）1C 07

接收报文：01（从站地址）01（功能码）03（字节计数，一个字节8位，需要读取20个地址的数据，2个字节只能读16位数据，所以需要3个字节来读取20个地址的数据，03代表的读取的数据有几个字节，并不是具体数据）C7 C0（具体读取的数据）DD B3

02H功能码读取输入线圈：

发送报文格式：从站地址 + 功能码 + 开始线圈地址 + 线圈数量 + CRC

接收报文格式：从站地址 + 功能码 + 字节计数 + 数据 + CRC

报文分析：

发送报文：05 02 00 14 00 0A B9 8D

接收报文：05 02 02 06 00 4B D8

报文解析：

发送报文05 02 （5号从站，02H功能码） 00 14 （换算十进制位20，在第20个地址开始）00 0A （读取10个数据）B9 8D （CRC校验码）

接收报文：05 02 （5号从站，02H功能码） 02 （接收了两个字节的数据）06 00 （这两个字节具体数据）4B D8 （CRC校验码）

03H功能码读取输出寄存器：

发送报文格式：

从站地址 + 功能码 + 开始寄存器地址 + 寄存器数量 + CRC

  

接收报文格式：

从站地址 + 功能码 + 字节计数 + 数据 + CRC

报文分析：

发送报文：02 03 00 0A 00 04 64 38

接收报文：02 03 08 00 01 00 02 00 03 00 04 02 50

报文解析：  

发送报文：02 (2号从站) 03 (功能码) 00 0A（从地址10开始） 00 04（读取4个寄存器）64 38 (CRC校验)

接收报文：02(2号从站) 03(03H功能码) 08(8个字节，一个寄存器占2个字节，一个线圈占1/8个字节) 00 01 （寄存器1数据）00 02（寄存器2数据） 00 03 （寄存器3数据）00 04（寄存器4数据） 02 50 （CRC校验）

04H功能码读取输入寄存器：

发送报文格式：

从站地址 + 功能码 + 开始寄存器地址 + 寄存器数量 + CRC

  

接收报文格式：

从站地址 + 功能码 + 字节计数 + 数据 + CRC

06H功能码预置单寄存器：

发送报文格式：

从站地址 + 功能码 + 寄存器地址 + 寄存器值 + CRC

接收报文格式：

从站地址 + 功能码 + 寄存器地址 + 寄存器值 + CRC

报文分析：

发送报文：05 06 00 0A 00 7B E8 6F

接收报文：05 06 00 0A 00 7B E8 6F

报文解析：00 0A（地址10） 00 7B （换算十进制为123）