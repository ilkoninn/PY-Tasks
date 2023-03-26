# Verilmis massivin daxilindeki adlarda "ir" varsa, ekrana hemin adi ve 
# names = ["Qirmizi", "Samir", "Aytac", "Kendir", "Eli"]
# Qirmizi (1, [1])
# Samir (1, [3])
# Kendir (1, [4])


names = ["Qirmizi", "Samir", "Aytac", "Kendir", "Eli"]

def find(param, word):
    count = 0
    index = []
    for i in range(len(param)):
        if param[i:].lower().startswith(word.lower()):
            count += 1
            index.append(i)
    
    return count, index

for i in names:
    a = find(i, "ir")
    if a[1] != []:
        print(i, a)