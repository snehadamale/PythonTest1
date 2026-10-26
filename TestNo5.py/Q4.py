a=[1,2,3,1,2,3,5,4,7,4,5,9,0,1]
f={}
for i in a:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1
print(f)