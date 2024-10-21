my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
q = 0
while q < len(my_list):
    if my_list[q] > 0 or my_list[q] == 0:
        print(my_list[q])
        q += 1