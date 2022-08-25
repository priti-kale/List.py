# 100. Write a Python program to extract common index elements from more than one given list. Go to the editor
# Original lists:
# [1, 1, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]

a=[1, 1, 3, 4, 5, 6, 7]
b=[0, 1, 2, 3, 4, 5, 7]
c=[0, 1, 2, 3, 4, 5, 7]
i=0
k=[]
while i<len(a):
    if a[i]==b[i]==c[i]:
        k.append(a[i])
    i=i+1
print(k)
        


# a=[1, 1, 3, 4, 4, 5, 6, 7]
# i=0
# b=[]
# j=i+1
# while i<len(a) and j<len(a): 
#     d=a[j]-a[i]
#     b.append(d)
#     j=j+1
#     i=i+1
# print(b)
    
