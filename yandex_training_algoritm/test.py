s = input()
answer = ''
count = 0
dct = {}
for i in s:
    if i not in dct:
        dct[i] = 0
    dct[i] += 1
    if dct[i] > count:
        count = dct[i]
        answer = i
print(count)       
print(answer)         

