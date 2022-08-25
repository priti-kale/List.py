# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists. Go to the editor
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

a=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

b=[]

i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
l=[]
j=0
while j<len(b):
    s=0
    k=[]
    while s<len(a):
        if b[j]==a[s]:
            k.append(a[s])
        else:
            l.append(a[s])
        s=s+1
    l.append(k)
    i=i+1
# pint(k)

