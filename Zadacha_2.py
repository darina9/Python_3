a = [4, 6, 8, 2,7, 9]
print(a)
if len(a) % 2 != 0:
    b = len(a)//2+1
else:
    b=len(a)//2    
list=[]       
for i in range(b):
    list.append(a[i]*a[-i-1])
print(f'произведения пар чисел: {list}')