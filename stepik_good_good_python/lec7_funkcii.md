Функции можно объявлять внутри условия

Perimentr = True
if Perimetr:
    def get_rect(x, y, z):
        return x * y * z
else:
    def get_rect(a, b):
        return a + b    