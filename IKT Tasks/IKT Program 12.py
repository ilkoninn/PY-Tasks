def myBin(param:int) -> int:
    new = []
    while param > 0:
        new.insert(0, str(param%2))
        param//=2

    return int(''.join(new))


print(myBin(343433))