

# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# a=['p','q']
# n=int(input("enter the num"))
# i=1
# b=[]
# while i<=n:
#     j=0`  `
#     while j<len(a):
#         b.append(a[j]+str(i))
#         j=j+1
#     i=i+1
# print(b)


# a=['p','q']
# b=[]
# n=int(input("enter the num"))
# for i in range(1,n+1):
#     for j in a:
#         b.append(j+str(i))
# print(b)

# b=[]
# n=int(input("ente the num:"))
# i=1
# while i<n:
#     j=1
#     while j<len(a):
#         b.append(a[j]+str(i))
#         j=j+1
#     i=i+1
# print(b)

# a=[1,2,3,4,6,0]####[2,1,4,3,0,6] 
# i=0
# b=[]
# j=i+1
# while i<len(a) and j<len(a):
#     b.append(a[j])
#     b.append(a[i])
#     j=j+2
#     i=i+2
# print(b)

a=[2,8,3,2,3,8,6,7,1,9]
i=0
b=[]
k=[]
while i<len(a):
    j=i
    s=[]
    while j<len(a):
        if a[i]!=a[j] :
            s.append(a[j])
        # else:
            # k.append(a[j])
        j=j+1
    b.append(s)
    i=i+1
print(b)
print(k)