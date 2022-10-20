a=[1.1, 1.2, 3.1, 5, 10.01]
print(a)
b=[]
for i in a:
     if i%1!=0:
        b.append(round(i%1,7))
print(b)
r=max(b)-min(b)
print(f'разница равна : {r}')