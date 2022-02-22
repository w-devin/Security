# 通过 windows api 判断程序被调试

1. IsDebuggerPresent

```g++
#include <windows.h>
#include <stdio.h>

int main()
{
    if(IsDebuggerPresent()){
        printf("on debugger\n");
    } else {
        printf("not on debugger\n");
    }

    getchar();
    return 0;
}
```

本地测试 gdb, OllyDbg是没问题的, 其他没有做测试

[ctf-wiki/windows/anti-debug/isdebuggerpresent](https://ctf-wiki.org/reverse/windows/anti-debug/isdebuggerpresent/)

2. CheckRemoteDebuggerPresent

```g++
#include <iostream>
#include <Windows.h>

int main() {
    BOOL isDebuggerPresent = TRUE;
    CheckRemoteDebuggerPresent(GetCurrentProcess(), &isDebuggerPresent);

    if (isDebuggerPresent) {
        printf("is debugging");
    }
    else {
        printf("not on debugging");
    }
} 
```

Note: 这里本地测试的时候有些翻车

1. MinGW 编译