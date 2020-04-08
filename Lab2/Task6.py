val = int(input())
i = 1

while i <= val:
    if val % i == 0:
        print(i,end=",")
    i+=1