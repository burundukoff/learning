Функции можно объявлять внутри условия

Perimentr = True
if Perimetr:
    def get_rect(x, y, z):
        return x * y * z
else:
    def get_rect(a, b):
        return a + b    


# put your python code here
# put your python code here
def lench_str(str):
    return str, len(str)

lst = input().split()
d = {}
d = dict(lench_str(x) for x in lst)

#print(d)
a = sorted(d, key=lambda x: d[x])
print(*a)        