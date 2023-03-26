# Verilmis massivde cutlerle, tekleri ayiran proqram yazin.

nums = [1,2,4,5,6,7]

new = []
index = 0

while len(nums) > index:
    if nums[index]%2 == 0:
        new.append(nums.pop(index))
        index-=1
    index+=1

print(nums)
print(new)
