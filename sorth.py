import sys
stack = []
program = [] 
Zcheck = None
def push(num):
    num = int(num)
    stack.append(num)

def pull():
    stack.pop()

def add():
    a = stack.pop()
    b = stack.pop()
    stack.append(a+b)
def minus():
    a = stack.pop()
    b = stack.pop()
    a = int(a)
    b = int(b)
    stack.append(b - a)
def Compare():

    global ZchecZcheck
    b = stack.pop() 
    a = stack.pop() 
    a = int(a)
    b = int(b)
    if(a > b):
        Zcheck = 1
    elif(a < b):
        Zcheck = 1
    elif(a == b):
        Zcheck = 0
def PrintzCheck():
    print(Zcheck)

def bruh():
    print(stack[len(stack)-1])

def readCode(name):
    with open(name) as f:
        lines = f.read().splitlines()
        program.append(lines)
def takeArgs():
    return sys.argv[1]
readCode(takeArgs())
for i in program: #this is just to get inside the first list 
    for OP in i: #actual intrustions list
        if(OP == "'+'"):
            add()
        elif(OP == "'.'"):
            bruh()
        elif(OP == "'-'"):
            minus()
        elif(OP == "'!!'"):
            Compare()      
        elif(OP == "'. .'"):
            PrintzCheck()
        elif(type(OP) == str): # this elif should be in the last always
            push(OP)