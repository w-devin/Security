# 内存操作

大部分汇编指令, 不支持从内存到内存的数据流
例外:
- movs

## 内存地址的表示

```asm
1. 立即数直接寻址
mov eax, dword ptr ds:[0x12345678]

2. 寄存器间接寻址
mov eax, dword ptr ds:[ecx]

3. 寄存器相对寻址, 变址寻址
mov eax, dword ptr ds:[ecx + 4]

4. 寄存器基址变址寻址
 mov eax, dword ptr ds:[eax + ecx * 4]

5. [reg + reg * {1, 2, 4, 8} + 立即数]
mov edx, dword ptr ds:[eax + ecx * 4 + 4]
```

## od like 调试器内存查看操作

1. db, display byte
2. dw, display word
3. dd, display dword