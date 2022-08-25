# a=[1,2,-8,0]
# i=0
# largest_num=0
# while i<len(a):
#     if a[i]>largest_num:
#         largest_num=a[i]
#     i=i+1
# print(largest_num)
    
a=[11,222,597,21]
i=0
b=[]
while i<len(a):
    b=str(a[i])
    j=0
    sum=0
    while j<len(b):
        sum=sum+int(b[j])
        j=j+1
    b.append(str(sum))
    i=i+1
print(b)

