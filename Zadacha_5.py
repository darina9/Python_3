a= int(input('введите целое число'))
f=[0,1]
nega_f=[1,0]
for i in range (2, a+1):
    f.append(f[i-1]+f[i-2])
    nega_f.insert(0, nega_f[1]-nega_f[0])
nega_f.extend(f[1:])  
print(nega_f)  