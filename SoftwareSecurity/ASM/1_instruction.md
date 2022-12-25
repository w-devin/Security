# 指令

## MOV

```asm
# mov <dst>, <src>
mov eax, 1

# mov <data size> <dst> <src>
mov byte ptr ds:[xxx], 1
``` 

## ADD

```asm
add <dst>, <src>

dst = dst + src
```

## SUB

```asm
sub <dst>, <src>

dst = dst - src
```

## AND

```asm
and <dst>, <src>
<dst> = <dst> & <sc>
```

## OR

```asm
or <dst>, <src>
<dst> = <dst> | <src>
```

## XOR

```asm
xor <dst>, <src>
<dst> = <dst> ^ <src>
```

## NOT

```asm
not <dst>
dst = !<dst>
```

## MOVS

mov string, mov data from mem to mem

DF 标志位控制 edi, esi 的移动方向, DF = 0, +， DF = 1, -

```asm
MOVS BYTE ptr es:[edi], BYTE ptr ds:[esi] # 可简写为 MOVSB
MOVS WORD ptr es:[edi], WORD ptr ds:[esi] # 可简写为 MOVSW
MOVS DWORD ptr es:[edi], DWORD ptr ds:[esi] # 可简写为 MOVSD
```

## STOS

将AL/AX/EAX 的值存储到[edi]指定的内存单元

STOSB, STOSW, STOSD

```asm
STOS BYTE PTR ES:[EDI]
```

## REP

重复 ECX 次操作

```asm
mov ecx, 10
rep 
```


