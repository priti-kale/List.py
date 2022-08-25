
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# print([[i for i in range(1,4)]for _ in range(3)])

i=0 
b=[]
while i<3:
    j=1
    k=[]
    while j<4:
        k.append(j)
        j=j+1
    b.append(k)
    i=i+1
print(b)
