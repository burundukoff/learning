a = list(map(int, input().split()))
for i in range(len(a[:-1])):
    min_ind = a.index(min(a[i+1:]), i+1)
    if a[i] > a[min_ind]:

        a[i], a[min_ind] = a[min_ind], a[i]
    
print(*a)