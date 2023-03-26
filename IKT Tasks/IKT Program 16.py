def test(param):
    simvols = {'{':'}', '(':')', '[':']'}
    param = list(param)
    while True:
        test2 = False
        index = 0
        while len(param) > index:
            if index != len(param)-1 and param[index+1] == simvols.get(param[index]):
                test2 = True
                param.pop(index)
                param.pop(index)
                break
            index+=1
        if not test2:
            break
        test2 = False
    return not param

a = '[[]]()'

print(test(a))