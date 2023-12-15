# put your python code here
lst = input().lower().split()
#st = {x for x in lst}
d = {key: 0 for key in lst}
d2 = {d2[key] : d[key] + 1 for key in lst}
print(d)
print(d2)