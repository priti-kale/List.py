# 2. Write a Python program to check if a nested list is a subset of another
#  nested list. Go to the editor
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# [[1, 3], [13, 15, 17]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# False



a=[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
b=[[1, 3], [13, 15, 17]]
# i=0
# while i<len(a):
#     j=0
#     c=0
#     while j<len(b):
#         if a[i]==b[j]:
#             c=c+1
#         j=j+1
#     i=i+1
# if c>=1:
#     print("true")
# else:
#     print("false")



c=0
for i in a:
    for j in b:
        if i==j:
            c=c+1
if c>=1:
    print("true")
else:
    print("false")