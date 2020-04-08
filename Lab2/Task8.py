val = input()
r = 9
for i in val:
    s = 9 - int(i)
    val = val.replace(i,str(s))
print(val)

