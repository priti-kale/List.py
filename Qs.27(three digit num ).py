######The task is to find all the possible combinations from these digits###
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=[]
d.append(a)
d.append(b)
d.append(c)
# print(d)
i=0
while i<len(d):
    j=0
    while j<len(d):
        k=0
        while k<len(d):
            if i!=j and j!=k and k!=i:
                print(d[i],d[j],d[k])
            k=k+1
        j=j+1
    i=i+1
    
