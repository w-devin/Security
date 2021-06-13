# BASH

## variables

1. declare

```bash
say='hello world'
```

2. ' & "

> Bash treats single and double quotes differently.
When encountering single quotes, Bash interprets every enclosed character literally. When
enclosed in double quotes, all characters are viewed literally except "$", "`", and "\" meaning
variables will be expanded in an initial substitution pass on the enclosed text

3. $(command) & `command`

> It is also important to note that command
substitution happens in a subshell and changes to variables in the subshell will not alter variables
from the master process.

## Arguments

1. Some special variables

| Variable Name     | Description                                       |
|  ----             | ----                                              |
| $0                | the name of the bash script                       |
| $1 - $9           | The first 9 arguments to the bash script          |
| $#                | number of arguments passed to the bash script     |
| $@                | all arguments passed to the bash script           |
| $?                | the exit status of the most recently run process  |
| $$                | the process id of the current script              |
| $USER             | the username of the user running the script       |
| $HOSTNAME         | the hostname of the machine                       |
| $RANDOM           | a random number                                   |
| $LINENO           | the current line number in the script             |

## reading user input

- `p` specify a prompt
- `s` makes the user input silent

```bash
read var

read -p 'username: ' username
read -sp 'password: ' password
```

## if, else, elif

```bash
if [ test ]
then
   action
fi


if [ test ]
then
  action
else
  another action
fi

if [ test1 ]
then
  action1
elif [ test2 ]
then
  action2
else
  action3
fi
```

*test command*

| Operator              | Description                                       |
|  ----                 | ----                                              |
| !EXPRESSION           | the EXPRESSION is False                           |
| -n STRING             | STRING length is greater than zero                |
| -z STRING             | the length of STRING is zero(empty)               |
| STRING1 != STRING2    | STRING1 is not equal to STRING2                   |
| STRING1 = STRING2     | STRING is equal to STRING2                        |
| INT1 -eq INT2         | INT1 is equal to INT2                             |
| INT1 -ne INT2         | INT1 is not equal to INT2                         |
| INT1 -gt INT2         | INT1 is greater than INT2                         |
| INT1 -lt INT2         | INT1 is less than INT2                            |
| INT1 -ge INT2         | INT1 is greater than or equal to INT2             |
| INT1 -le INT2         | INT1 is less than or equal to INT2                |
| -d FILE               | FILE exists and is a directory                    |
| -e FILE               | FILE exists                                       |
| -s FILE               | FILE exists and is not empty                      |
| -r FILE               | FILE exists and has read permission               |
| -w FILE               | FILE exists and has write permission              |
| -x FILE               | FILE exists and has execute permission            |

## Boolean Logical Operations

ADN(&&), OR(||), 类似于其他编程语言, 逻辑运算有短路特性

## Loops

1. For Loops

```bash
for var in <list>
do
  action
done

for var in <list>; do action; done
```

2. WHile Loops

```bash
while [ test ]
do
  action
done

while [ test ]; do action ;done
```

tips:

1. '#!/bin/bash -x': print additional debug output

> commands preceded with a single “+” character were executed in the current shell and 
> commands preceded with a double “++” were executed in a subshell.



## Functions

```bash
function fun_name {
  actions
}

fun_name(){
  actions
}
``` 

## Others

1. cutycapt

a Qt WebKit web page rendering capture utility

```bash
cutycapt --url="url" --out="file_to_save"
```
