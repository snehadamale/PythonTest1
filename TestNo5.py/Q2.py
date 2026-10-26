n=int(input("Enter number of coins"))
a=list(map(int,input("Enter coin numbers").split()))
f={}
for i in a:
    if i in f:
        f[i]=f[i]+1
    else:
        f[i]=1
for i in f:
    if f[i] % 2 !=0:
        print("Missing coin number",i)
        break