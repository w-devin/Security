# PE文件格式

## 0x00 PE 文件及其表现形式

1. PE, Portable Executable File
2. 其他EXE文件格式
   - DOS: MZ 格式
   - Windows 3.0/3.1: NE, New Executable; 16位windows可执行文件

## 0x01 PE 文件格式与恶意代码的关系

1. 文件感染: 使目标PE文件具备或启动病毒功能或目标程序, 但不破坏PE文件原有功能和外在形态(目的 + 隐匿)
2. 如何合并
   - 代码植入
   - 控制权获取
   - 图标更改

## 0x02 PE文件格式总体结构

### 常用工具/资源
   - PEView
   - Stud_PE
   - OllyDbg
   - UltraEdit, 16进制查看和编辑
   - WinHex

### 结构

1. DOS MZ header
   - MZ文件头, 0x40 bytes
   - 0x3C: 4 bytes, PE文件头的位置
2. DOS stub, DOS 模式下运行该程序时, 将会提示: "This Program cannot be run in DOS mode"
3. PE header
   - IMAGE_NT_SIGNATURE, 0x50(P) 0x45 (E) 0x00 0x00, PE标记
   - IMAGE_FILE_HEADER
     - Machine, 2 bytes, 机器类型, x86为 0x14C
     - NumberOfSection, 2 bytes, 文件中节的个数
     - TimeDataStamp, 4 bytes, 生成该文件的时间
     - PointerToSymbolTable, 4 bytes, COFF符号表的偏移
     - NumberOfSymbols, 4 bytes, 符号数目
     - SizeOfOptionalHeader, 2 bytes, 可选头的大小
     - Characteristics, 2 bytes, 关于文件信息的标记, 比如文件时exe还是dll
   - IMAGE_OPTIONAL_HEADER
     - 0xD8(我本地测试是0xA8), AddressOfEntryPoint, 4 bytes, PE loader 准备运行的PE文件的第一条指令的RVA
     - 0xE4(我本地为0xB4), ImageBase, PE文件优先装载地址
     - 0xE8(0xB8), SectionAlignment, 4 bytes, 内存中节对齐的粒度
     - 0xEC(0xBC), FileAlignment, 4 bytes, 文件中节对齐粒度
     - Directory, 16 * 8 bytes
       - EXPORT Table
       - IMPORT Table
       - RESOURCE Table
       - EXCEPTION Table
       - CERTIFICATE Table
       - ...
4. Section table, 紧邻PE Header, 每一节对应一个节表项
5. Sections, 常见节类型:
   - .text|CODE, 代码节, 含有程序的可执行代码, 每个PE文件都有代码节
   - .data|DATA, 数据节, 已初始化的数据节中放的是编译时就确定的数据
   - .rdata, 引入函数节, 只保留了函数信息, 函数名, 其驻留的DLL名等
     - IMPORT Address Table
     - IMPORT Directory Table, IMAGE_OPTIONAL_HEADERS/Directory/IMPORT TABLE 记录了 IDT 在内存中的位置 RVA
       - IMAGE_THUNK_DATA
         - Import Name Table RVA, 4 bytes
           - Characteristics,
           - OriginalFirstThunk,
         - Time Date Stamp, 4 bytes
         - Forwarder Chain, 4 bytes
         - Name RVA, 4 bytes, dll 文件名字符串的RVA
         - Import Address Table RVA, 4 bytes
       - 最后以一个全0的 IMAGE_THUNK_DATA 作为 IDT 结束
     - IMPORT Name Table
       - Hint/Name RVA, 最高位为0, 表示通过函数名引入, 为1, 通过序号引入
       - End of Imports
     - IMPORT Hints/Names & DLL Names
   - .bss, 未初始化的数据节, 一般为未初始化的全局变量和静态变量， eg. `static int k;`
   - .idata
   - .CRT
   - .tls
   - .rsrc

### 相关概念

1. RVA地址, Relative Virtual Address, 相对虚拟地址, 相对内存中 ImageBase 的偏移地址
2. 对齐粒度
   - 文件中节对齐粒度为0x200
   - 内存中节对齐粒度为0x1000