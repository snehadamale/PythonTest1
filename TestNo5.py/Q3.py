data=[
    [
        [101,"A",4500],
        [102,"B",5500],
        [103,"C",6500],
        [104,"D",7500]
    ]
]
n=len(data)
for i in range(n):
    for j in range(i+1,n):
        if data[i][2]>data[j][2]:
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
for i in range(n):
    print(data[i])