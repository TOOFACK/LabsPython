val = int(input())
list = [0]*10
for i in range(0,10):
    t = val
    while t > 0:
        if t % 10 == i:
            list[i]+=1
        t = t // 10
print("[", end="")
for i in range(0,10):

    print(i,"", end =" ")

print()
print(list)