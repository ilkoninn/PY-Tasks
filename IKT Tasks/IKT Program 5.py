# [('turkan', 'quluzade'), ('musa', 'abbasov)] verilmis list 
# icindeki tuple dict-e cevirin
# CAVAB: [{'name':'turkan', 'lname':'quluzade'},{'name':'musa', 'lname':'abbasov'}]

names = [('iqbal', 'memmedov'), ('vusal', 'elizade'), ('nebi', 'davidov')]
new = []

for i in range(len(names)):
    new.append({'id':i+1, 'name':names[i][0], 'lname':names[i][1]})

print(new)