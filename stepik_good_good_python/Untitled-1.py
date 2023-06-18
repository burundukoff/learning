# s = "   fly me   to   the moon  "
# lst=s.split()
# print(lst,s)
# a = len(lst[-1])
# print(a)
# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# print(lst_in)

# def get_sub_eq(eq_str):
#     st = []
#     res = []

#     for i, x in enumerate(eq_str):
#         if x == "(":
#             st.append(i)
#         elif x == ")":
#             res.append(eq_str[st.pop()+1: i])

#     return res


# s = "2 + 3 * (1 - 5 - (3 * x - 5)) + (a - b)"
# res = get_sub_eq(s)

a = {1:2, 2:3, 4:5}
b=a.values()
print(b)
