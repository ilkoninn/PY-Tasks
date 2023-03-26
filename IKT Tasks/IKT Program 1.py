# nums = ['11 2 ', '3 4'] list icindeki stringleri ayri ayriliqda int olaraq toplayin ekrana cap edin
#    CVB: 13, 7

nums = ['11 2 34 12 13 1', '3 4', '12 44']

for i in nums:
    nums = list(map(int, i.split()))
    mySum = 0
    for x in nums:
        mySum+=x
    print(mySum)