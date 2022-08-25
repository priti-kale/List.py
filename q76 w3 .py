# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
a=[1, 1, 2, 3, 4, 4, 5, 1]
print(a)
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
i=0
k=[]
while i<len(b):
    j=0
    c=0
    while j<len(a):
        if b[i]==a[j]:
            c+=1
        j+=1
    if c>1:
        k.append([c,b[i]])
    else:
        k.append(b[i])
    i=i+1
print(k)
