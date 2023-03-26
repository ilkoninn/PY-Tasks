array = [1,1,1,1,1,1,1,2,3,4,4]

index = 0
count = 0
while len(array) > index:
    if index != len(array)-1 and array[index] == array[index+1]:
        array.pop(index)
        count+=1
        index-=1
    index+=1



for i in range(count):
    array.append(array[-1]+1)

print(array)