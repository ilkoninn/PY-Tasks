strs = ["flower","flowe","floightwe"]

for i in range(len(strs[0])):
    a = strs[0][i:]
    for x in range(len(a)+1):
        for c in strs:
            if a[:x] not in c:
                break
        else:
            if len(a[:x]) > 1:
                print(a[:x])