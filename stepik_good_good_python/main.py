d = dict(c.split('=') for c in input().split())
for c in d:
  d[c] = int(d[c])
print(*sorted(d.items()))