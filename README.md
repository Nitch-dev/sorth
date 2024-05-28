# sorth
A language started as a Project to Learn How compilers and Interpreters Work, Its based of Python.

Its has no real use-case just making this for Fun and to get to Know more about Compilers.

Open to Suggestions



**Quick Start:**  
`$ python3 sorth.py <File Name>`

* File should end with .sorth



### PUSH

**Description:**  
Push a number onto the stack.

**Syntax:**  
`<number>`

**Example:**  
```plaintext
5 10 20
```

### ADD

**Description:**  
It will add 2 numbers from stack and push the answer on stack 

**Syntax:**  
`'+'`

**Example:**  
```plaintext
5 
10
'+'
```
### MINUS

**Description:**  
It will Minus 2 numbers from stack in reverse order and push the answer on stack 

**Syntax:**  
`'-'`

**Example:**  
```plaintext
5 
10
'-'
```

### PRINT

**Description:**  
It will Print the last element of the Stack and wont pop anything from stack

**Syntax:**  
`'.'`

**Example:**  
```plaintext
5 
'.'
```

### CMP

**Description:**  
It will Compare the elemts from stack in reverse order so if its A B on stack it will do compare A with B and not B with A and will Update the Zcheck Flag Accordingly

**Syntax:**  
`'!!'`

**Example:**  
```plaintext
5
5
'!!'
```
### Z-Check Print

**Description:**  
It will Print the Zcheck Flag If its *0* then the elemts are same if its *1* then elemts are not same either are greater or smaller 

**Syntax:**  
`'. .'`

**Example:**  
```plaintext
5
10
'!!'
'. .'
```

## Summary of OP Codes

| Operation        | OP Code | Description                                               |
|------------------|---------|-----------------------------------------------------------|
| PUSH             | `<number>` | Push a number onto the stack                              |
| ADD              | `+`     | Pop two numbers, add them, and push the result             |
| MINUS            | `-`     | Pop two numbers, subtract the first popped from the second, and push the result |
| CMP              | `!!`    | Pop two numbers, compare them, and set `Zcheck`            |
| PRINTING         | `.`     | Print the top element of the stack                         |
| Zcheck-PRINTING  | `. .`   | Print the value of `Zcheck`                                |
