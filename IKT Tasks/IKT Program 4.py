# n = 21 natural ədədi verilmişdir. 
# Həmin ədəddən öz rəqəmlərinin cəmini(3) çıxaq. 
# Alınan ədəddən də yenə öz rəqəmlərinin cəmini 
# çıxaq və s. Bu prosesi nə qədər ki, 
# alınan ədəd müsbətdir davam etdirəcəyik. 
# Verilmiş əməliyyatı neçə dəfə icra edəcəyik?


num1 = 21

count = 0
while num1 > 0:
    num2 = str(num1)
    mySum = 0
    for i in num2:
        mySum+=int(i)
    count+=1
    num1-=mySum

print(count)

count = 0
while num1 > 0:
    num2 = num1
    mySum = 0
    while num2 > 0:
        mySum+=num2%10
        num2//=10


    num1-=mySum
    count+=1

print(count)