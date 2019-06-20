#!/usr/bin/env
#simple fuzzer

import os

shellcode=("Your shell code in little endian form")

param= "edb --run ./bufferoverflow" #Here EDB debugger is used
param += "A"*30   #A is printed 30 times to overflow the stack
param += "Your Address in little endian form ex: (\xfc\x05\x56\x4b)"
param +=shelcode

os.system(param)
