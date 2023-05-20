a = input().split()
a = [x.split(sep='=') for x in a]
a = [[int(j) if j.isdigit() else j for i,j in enumerate(y)]for y in a]
d = dict(a)
print(*sorted(d.items()))