# 寄存器

## 通用寄存器

32 - 16 - 8
1. EAX - AX - AL
2. ECX - CX - CL
3. EDX - DX - DL
4. EBX - BX - BL
5. ESP - SP - AH
6. EBP - BP - CH
7. ESI - SI - DH
8. EDI - DI - BH

Note:
1. AL(low), AH(high), 表示 AX 的 高8位和低8位, 其他寄存器类似
2. ESP, EBP, ESI, EDI 没有 8 位的寄存器符号

## 通用寄存器的常见用途

1. ECX, 常用于计数, count, REP等
2. ESI, EDI, 常用于源, 目的, STOS
3. EAX, 常用于保存结果
4. ESP, EBP, 常用作堆栈