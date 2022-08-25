# a = [1, 2, 2, 3, 3, 3]
# i=0
# count=0
# s=[]
# while i < len(a):
#     if a[i] not in s:
#         s.append(a[i])
#     i=i+1
# print(s)


list1 = [1,2,3,2,2,3,1,3,445,445,445,32,32,1,1,76,87,98,89,78,6,5,78,87,87]
lst = []
for x in list1:
    if x not in lst:
        lst.append(x)
print(lst)