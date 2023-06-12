s = input()
# print(len(s))
def gameOfThrones(s):
    dictnary = {}
    counter = 0
    if (len(s) % 2) == 0:
        for i in s:
            if i in dictnary.keys():
                dictnary[i] += 1
            else:
                dictnary[i] = 1
        # print("Dictnary", dictnary)
        for i in dictnary:
            if (dictnary[i] % 2) == 0:
                counter = counter
            else:
                counter += 1
        if counter < 1:
            return 'YES'
        else:
            return 'NO'
    else:
        for i in s:
            if i in dictnary.keys():
                dictnary[i] += 1
            else:
                dictnary[i] = 1
        # print("Dictnary", dictnary)
        for i in dictnary:
            if (dictnary[i] % 2) == 0:
                counter = counter
            else:
                counter += 1
        if len(dictnary) == counter:
            return 'NO'
        elif float(counter)%2 != 0:
            return 'YES'
        else:
            return 'NO'
result = gameOfThrones(s)
print(result)