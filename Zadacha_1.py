a = [2, 3, 5, 9, 3]
print(a)
sum = 0
for i in range(1, len(a), 2):
    sum += a[i]
print(f'сумма элементов на нечетных позициях:  {sum}')