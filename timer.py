#!/usr/bin/env python3
# timer.py
# Simple timer on a clear screen
import time as t
import sys, os
s=0
m=0
h=0
nv='\033[?25l'
v='\033[?25h'
def cl():
    os.system('cls'if os.name=='nt'else'clear')
def main():
    global h,m,s
    try:
        while True:
            cl()
            print(f'{nv}{h:02d} : {m:02d} : {s:02d}',end='\r')
            t.sleep(1)
            s+=1
            if s==60:
                s=0
                m+=1
            if m==60:
                m=0
                h+=1
    except KeyboardInterrupt:
        print(f'{v}\nTIMER has been stopped... ')
        sys.exit()
    except Exception as e:
        print(f'\n[ERROR] -> {e} ')
        sys.exit()
main()
