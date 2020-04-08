temp = int(input())
i = 0
res = 0
while(i <= temp):
    if i % 2 != 0:
        res += i**2
    i+=1
print(res)
