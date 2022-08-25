# 79. Write a Python program to remove the K'th element from a given list, print the new list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]



a=[1, 1, 2, 3, 4, 4, 5, 1]
k=int(input("enter:"))
# element=int(input("enter:"))
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=k:
#         b.append(a[i])
#     i=i+1
# print(b)
a.remove(k)
print(a)