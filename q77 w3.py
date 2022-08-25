# 77. Write a Python program to decode a run-length encoded given list. Go to the editor
# Original encoded list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
a=[[2,1],2,3,[2,4],5]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=1
        while j>=0:
            b.append(a[i][1])
            j=j-1
    else:
        b.append(a[i])
    i=i+1
print(b)

 




# a=[0,1,0,1,1,0]
# i=0
# k=[]
# while i<len(a):
#     j=0
#     c=0
#     b=a[:i]
#     while j<len(b):
#         if a[j]==0:
#             c=c+1
#         j=j+1
#         print(c)
#     k.append(c)
#     i=i+1
# print(k)

                      


