# Verilmis ededin eksini yigan proqram yazin.
# Mes, n = 1234, new = 4321

num1 = 12345667
num2 = 0

while num1 > 0:
    num2 = num2 * 10 + num1%10
    num1//=10

print(num2)