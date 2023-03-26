# Replacein alqoritmi

import time

def replace(param1:str, param2:str, param3:str) -> str:
    length = len(param2)
    index = 0
    while len(param1) > index:
        if param1[index:index+length] == param2:
            param1 = param1[:index] + param3 + param1[index+length:]
        index+=1
    return param1


name = 'abrakadabra'
print(replace(name, 'ab', 'ups'))