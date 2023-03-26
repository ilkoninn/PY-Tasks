num1 = '2481632'
num2 = ''

result = 0
num3 = 1
new = []

while num1 != num2:
    result = 2**num3
    new.append(result)
    num2+=str(result)
    num3+=1

print(new)