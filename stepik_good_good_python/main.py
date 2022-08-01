st = '1234567890'
a = list(set([y for x,y in enumerate (input()) if y in st]))
a.sort()
print(*a if a else ['НЕТ'])
