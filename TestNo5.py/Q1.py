li=[2000,500,200,100,50,20,10,5]
amount=int(input("Enter amount"))
count=0
for i in li:
    n=amount//i
    if n > 0:
        print(i,":",n)
        count=count+n
        amount=amount%i
print("Monimun number of notes",count)
if amount > 0:
    print("Remaining amount",amount)

