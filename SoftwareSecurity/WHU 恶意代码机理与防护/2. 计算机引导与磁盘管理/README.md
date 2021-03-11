# C2 计算机引导与磁盘管理

## 系统引导与控制权

### 计算机系统引导过程

1. BIOS: Basic Input and Output System. 为计算机提供最底层的， 最直接的硬件设置和控制

2. BIOS引导模式

    - 传统BIOS： 开发效率低， 性能差， 扩展性差
      - 开机 -> BIOS初始化 -> POST 自检 -> MBR(硬盘主引导程序) -> DBR(活动分区引导程序) -> bootmgr/NTLDR(操作系统引导) -> 读取BCD/boot.ini -> 启动对应系统(操作系统内核启动 -> 驱动程序及服务 -> 系统自启动程序)
    - UEFI: Unified Extensible Firmware Interface. 支持 GPT， 取消了POST自检
      - 开机 -> BIOS初始化 -> ESP分区 启动管理器(EFI分区bootxxx.efi) -> 读取BCD -> 调用对应系统盘 winload.efi -> 启动对应系统

    tips: `Msinfo32.exe` / `bcdedit.exe` 可查看系统BIOS信息

3. BIOS的自检与初始化工作

    关键设备检查并初始化， 并将控制权交给后续引导程序

4. 硬盘主引导程序

    位置: MBR, Master Boot Record, 硬盘第一个扇区
    功能: 通过主分区表中定位活动分区. 装载活动分区的引导程序， 并移交控制权

5. 活动分区引导程序

    位置: DBR(Dos Boot Record), 或 OBR(OS Boot Record), 或 PBR(Partition Boot Record), 分区引导记录. 分区的第一个扇区
    功能: 加载操作系统引导程序. windows xp 系统的NTLDR, windows Vista及以后的BOOTMGR

6. 操作系统引导(NTLDR)

    1. 将处理器从16位扩展为32、64位内存模式
    2. 启动小型文件系统驱动， 以识别FAT32和NTFS文件系统
    3. 读取boot.ini, 进行多系统选择(或hiberfil.sys恢复休眠)
    4. 检测和配置硬件(NT或XP系统, 则运行NTDETECT.COM， 其将硬件信息提交给NTLDR, 写入 "HKEY_LOCAL_MACHINE" 中的Hardware)

7. 系统内核加载

    1. NTLDR 加载内核程序 NTOSKRNL.EXE 及硬件抽象层 HAL.dll 等
    2. 读取并加载 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet 下指定的驱动程序
    3. NTLDR将控制权传递给NTOSKRNL.EXE 引导结束

8. Windows系统装载

    1. 创建系统变量
    2. 启动win32.sys (windows子系统的内核模式部分)
    3. 启动csrss.exe(windows子系统的用户模式部分)
    4. 启动winlogon.exe等

    至此，显示开机logo

9. Windows系统装载-登录阶段

    1. 启动需要自启动的windows服务
    2. 启动本地安全认证 Lsass.exe
    3. 显示登录界面等

10. Windows 登录之后

    1. 系统启动当前用户环境下的自启动项程序
        - 注册表特定键值
        - 特定目录(如startup)等
    2. 用户触发和执行各类程序

11. 系统引导与恶意软件的关联

    1. 在计算机引导阶段获得控制权 Bootkit(BIOS木马, MBR木马)， CIH病毒
    2. 在系统启动阶段获取控制权
    3. 在应用程序执行阶段获得控制权

## 80X86 处理器的工作模式

## Windows 内存结构与管理

## 磁盘的物理与逻辑结构

## FAT32文件系统及数据恢复

## NTFS文件系统

## 程序的二进制表示
