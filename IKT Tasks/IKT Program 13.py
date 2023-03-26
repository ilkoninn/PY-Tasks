def dec(param:int) -> int:
    num1 = 0
    num3 = 0
    while param > 0:
        if param%10 != 0:
            num1+=2**num3
        num3+=1
        param//=10
    return num1