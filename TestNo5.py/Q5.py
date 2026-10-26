a=[1,2,3,4]
b=[2,4,6,5]
union=[]
for i in a:
    if i not in union:
        union.append(i)
for i in b:
    if i not in union:
        union.append(i)
print(union)