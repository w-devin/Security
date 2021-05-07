# 代理/端口转发

## 工具

### HTran

应该是由 cnhonker 的一伙人开发的, 最初是用C写的 Windows 版本, 后来内部做了 linux 适配版, [项目地址](https://github.com/HiwinCN/HTran)

后来由 [bGn4](https://github.com/bGN4) 做了多平台适配版, [项目地址](https://github.com/bGN4/HTran)

#### usage

```cmd
(base) PS D:\Projects\socket_client\Debug> .\socket_client.exe
======================== HUC Packet Transmit Tool V1.00 =======================
=========== Code by lion & bkbll, Welcome to http://www.cnhonker.com ==========

[Usage of Packet Transmit:]
 D:\Projects\socket_client\Debug\socket_client.exe -<listen|tran|slave> <option> [-log logfile]

[option:]
 -listen <ConnectPort> <TransmitPort>
 -tran   <ConnectPort> <TransmitHost> <TransmitPort>
 -slave <ConnectHost> <ConnectPort> <TransmitHost> <TransmitPort>
```

支持三种转发方式, 分别是 端口转端口(listen), 端口转连接(tran), 连接转连接(slave)

核心转发代码在 transmitdata 方法, 在 slave 模式下, 由 bkbll 做了连接方式的改进, 在接收端接收到数据后, 再向目标发起连接

### LCX

这个工具很奇怪, 感觉像是 HTran 被人多平台兼容后的版本, 

使用可参考: [红队技能：Hash读取与端口转发](https://mp.weixin.qq.com/s/tXRGfiinPkOOVpQ1n7z1-g)