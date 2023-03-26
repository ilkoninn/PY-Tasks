# name = 'python 1programing language' string icindeki 
# butun sozlerin ilk herflerini boyudun
# lakin reqemle baslayanlar xaric ve netice stringi name 
# stringden uzunluq olaraq ferqlenmemelidir 

# name = 'python programing  1language'

# name2 = ''

# for i in range(len(name)):
#     if i == 0 or name[i-1] == ' ' and name[i].isalpha():
#         name2+=name[i].upper()
#     else:
#         name2+=name[i]

# print(name2)

name = 'python prog1raming  1language'
name2 = name.split()

for i in name2:
    for x in range(len(i)):
        if i[x:].isalpha() or x == 0 and i[x].isalpha():
            print(i[:x]+i[x].upper()+i[x+1:])
            break