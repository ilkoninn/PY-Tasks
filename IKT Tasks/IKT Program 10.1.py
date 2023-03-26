# num1 = 5 verilmis reqeme uygun olaraq asagidaki list yarading
#  [
#       [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], 
#       [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], 
#       [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], 
#       [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], 
#       [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]
# ]

num1 = 5
new = []
new2 = []

for i in range(num1):
    new2 = [] 
    for j in range(num1):
        new2.append([i, j])
    #print(new2)
    new.append(new2)


print(new)