# a="banana"
# i=0
# while i<len(a):
#     print(a[i],end="")
#     i=i+1


# for i in range (1,100):
#     print()
a=[1,2,3,4]
b=input("insert num")
c=int(input("entre"))
i=0
while i<len(a):
    d=ind(b,c)
    a.append(d)
    print(a)