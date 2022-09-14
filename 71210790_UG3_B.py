
n = int(input('Masukkan nilai n: '))
faktorial = 1
dic = []
lis = []
for i in range(1, n):
    faktorial *= i
    if i == 1:
        dic.append(faktorial)
    if i % 2 == 0:
        dic.append(faktorial)
    else: 
        continue
    
for i in range(n):
    if i % 2 == 0:
        lis.append(i)

print(dic)
print(lis)
