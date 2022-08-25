# 80. Write a Python program to insert an element at a specified position into a given list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]





a=[1, 1, 2, 3, 4, 4, 5, 1]
k=int(input("After inserting an element at kth position:"))
n=int(input("enter the insert num"))
i=0
d=[]
while i<len(a):
    if i==k:
        d.append(n)
    d.append(a[i])
    i=i+1
print(d)
# print(len(d))





