val = int(input())
res = 0

while val > 0:
    res += val % 10
    val = val // 10
print(res)
