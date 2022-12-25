# windows 提权

## 信息收集

### 命令/工具

```cmd
1. msf: local_exploit_suggester
2. Windows-Exploit_suggester
```


## 提权

### 漏洞提权

1. 烂土豆

2. 利用系统错误

系统使用系统权限对服务的二进制文件路径进行解析

a. 可以用 wmic 查看没有被引号引起来的服务路径
b. 创建文件
c. 重启服务或者计算机
 
3. mimikatz
4. Pr, windows 本地溢出工具
5. churrasco, 巴西烤肉 cve-2009-0079


### windows access token

1. whoami /group 可查看完整性权限等级
2. 工具
    - incognito(msf/windows, 也有单独可执行文件的版本)窃取目标主机的令牌或假冒用户
    - Invoke-TokenManipulation, 利用 Powershell 编写用来盗窃目标主机的令牌或假冒用户的脚本 

### UAC(User Account Control)

#### UAC 机制

1. 需要UAC的授权才能进行的操作列表如 下：
    - 配置WindowsUpdate
    - 增加、删除账户
    - 更改账户类型
    - 更改UAC的设置
    - 安装Activex
    - 安装、卸载程序
    - 安装设备驱动程序
    - 将文件移动/复制到ProgramFiles或Windows目录下
    - 查看其它用户的文件夹

2. MIC(Mandatory Integrity Control) 强制完整性控制
    - IL (Integrity Level), 低、中、高、系统
    - Biba-Model: no read down, no write up

#### UAC 绕过技术

注意: visa等老系统, bypass uac 无用

1. msf 绕过
    - exploit/windows/local/bypassuac
    - exploit/windows/local/ask
2. dll hijack
3. 白名单绕过
    - 不会触发uac的白名单程序, 例如win10下的 `C:\Windows\System32\ComputerDefaults.exe`
    - 可以使用 `sigcheck` | `Invoke-PsUACme` 检查应用是否在白名单
    - 例: slui.exe, wusa.exe, taskmgr.exe, msra.exe, eudcedit.exe, eventvwr.exe, CompMgmtLauncher.exe, rundll32.exe, explorer.exe
4. shell api
5. com类提权
    - 注入到系统可信进程, explorer.exe, dllhost等
    - 修改当前进程的peb结构, 欺骗 psapi, 可以把peb路径修改为 explorer.exe
    - 可信文件直接调用com组建, 比如 powershell.exe
    - 利用条件: elvation 开启, auto approval 开启
    - 寻找这类接口 (OleViewDotNet, yuubari)

#### 绕过实例, 白名单(C:\Windows\System32\fodhelper.exe)

管理可选功能, 可以与注册表交互

1. 利用条件
    - 系统版本 < win10 build 1709
2. fodhelper 行为
    - 启动时检查注册表 `\Software\Classes\ms-settings\shell\open\command` 以及 `...\command\DelegateExecute`
    - 先检查 `HKCU` 再检查 `HKCR`
    - 我们可以通过写 `HKCU` 来让 fodhelper 执行我们指定的命令
3. 提权过程
    - 写注册表
        ```bat
        reg add HKEY_CURRENT_USER\Software\Classes\ms-settings\shell\open\comand /ve /d C:\\Windows\\System32\\cmd.exe
        
        reg add HKEY_CURRENT_USER\Software\Classes\ms-settings\shell\open\command /v DelegateExecute
        ```
        
#### 绕过实例, shell api + 白名单(eventvwr.exe)

1. 利用条件
    - 若 enablua = 0, 可直接只用 psexec 执行进行提权
    - enablua 值为 默认值 0, 2, 5(?)

#### 绕过实例, Invoke-PsUACme(com类提权)

1. 利用条件
    - 使用来自 UACME 项目的DLL绕过UAC, 需要运行账号处在管理员组
    - 目前只支持win7, win8    
2. 利用姿势
    ```powershell
    # 使用 sysprep 方法并执行默认的 payload
    Import-Module .\Invoke-PsUACme.ps1; Invoke-PsUACme -verbose
    
    # 使用 oobe 方法并执行默认的payload
    Import-Module .\Invoke-PsUACme.ps1; Invoke-PsUACme -method oobe -verbose
    ```
3. 可选 method
    - sysprep
    - oobe
    - action queue
     - migwiz
    - cliconfg
    - winsat
    - mmc

    
## Reference

1. [从项目中看BypassUAC和BypassAMSI](https://bbs.pediy.com/thread-266375.htm)
1. [UACME](https://github.com/hfiref0x/UACME)