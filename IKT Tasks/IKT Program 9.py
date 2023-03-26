# Verilmis massivi bir massive getiren proqram yaz.
# Mes, nums = [1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12]]]]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

nums = [1, 2, [3,4], 5]


def myOpen(array:list, new = []):
    for i in array:
        if type(i) == list:
            myOpen(i, new)
        else:
            new.append(i)
    return new


print(myOpen(nums))
