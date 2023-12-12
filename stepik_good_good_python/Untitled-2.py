def find_mms(lst):
    v_min = min(lst)
    v_max = max(lst)
    v_sum = sum(lst)
    print(f"Min = {v_min}, max = {v_max}, sum = {v_sum}")

lst = list(map(int, input().split()))
find_mms(lst)