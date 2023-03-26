# Ededin eksi ile duzune formasi eynidirse, True, ferqlidirse, False versin.


num1 = num2 = 12021
reverse = 0

while num2 > 0:
    reverse = reverse*10+num2%10
    num2//=10

print(reverse == num1)