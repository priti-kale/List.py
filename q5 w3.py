# a=['abc', 'xyz', 'aba', '1221']
# c=0
# for i in a:
#     if i[0]==i[-1]:
#         c+=1
# print(c)        



# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result=sorted(a,key=lambda x:x[1])
print(sorted(a))
r=sorted(a,key=lambda i:i[1])
print(r)