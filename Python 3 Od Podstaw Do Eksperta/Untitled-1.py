A = 1233243465475679869
binA = bin(A)
strA = str(binA[2:])
print(strA)
count_zero = 0
zero_in_row_list = list()
for item in strA:
    if item == '0':
        count_zero += 1
    if item == '1':
        zero_in_row_list.append(count_zero)
        count_zero = 0
print(zero_in_row_list)
print(max(zero_in_row_list))



A % 2