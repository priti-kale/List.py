a=[1,2,3,4,5,7]
b=[6,7,8,9,2]
i=0
h=[]
while i<len(a) :
    if a[i] in b:
        h.append(a[i])
    i=i+1
print(h)


