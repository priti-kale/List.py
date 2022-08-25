# 101. Write a Python program to sort a given matrix in ascending order according to the sum of its rows. Go to the editor
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]


# a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# # b=[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# i=0
# sum=0
# sum1=0
# while i<len(a) or i<len(b):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     s=0
#     while s<len(b[i]):
#         sum1=sum1+b[i][s]
#         s=s+1
#     i=i+1
# print(sum)
# print(sum1)
# if sum==sum1:
#     print("matric")

a=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
a.sort()
print(a)