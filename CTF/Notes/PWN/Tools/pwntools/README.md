# pwntools

## 0x00 常用方法

```python
remote(host, port)  # 连接远程服务

process(file_path) # 使用本地文件创建进程
dbg.attach(process_name) # attach 一个进程

ELF(file_path) # 读取本地ELF文件
symbols['a_function'] 找到 a_function 的地址
got['a_function'] 找到 a_function的 got
plt['a_function'] 找到 a_function 的 plt
next(e.search("some_characters")) 找到包含 some_characters(字符串,汇编代码或者某个数值)的地址.

send(payload)
sendline(payload)
sendafter(some_string, payload)

recvn(N) # 接收 N 个字符
recvline() # 接收一行输出
recvlines(N) # 接收 N 行输出
recvuntil(some_string) # 接收到 some_string 为止

p32() # 整数 -> 4字节小端序格式, 同类的有 p64, p16

interactive() # getshell 后开始交互模式
```


## 0x0n reference

1. [一步一步学pwntools](https://bbs.pediy.com/thread-247217.htm)