i=int(input("enter the num"))
j=int(input("enter the num"))
s=int(input("enter the num"))
for i in range(1,4):
    for j in range(1,4):
        for s in range(1,4):
            if i!=j and j!=s and s!=i:
                print(i,j,s)
