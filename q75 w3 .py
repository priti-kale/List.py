# 75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4.3, 5, 1]
# List reflecting the run-length encoding from the said list:
# [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# Original String:
# automatically
# List reflecting the run-length encoding from the said string:
# [[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
a=[1, 1, 2, 3,4, 4, 4.3, 5, 1]
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)
j=0
l=[]
while j<len(b):
    s=0
    c=0
    k=[]
    while s<len(a):
        if b[j]==a[s]:
            c+=1
        s=s+1
    if c>1:
        k.append(c)
        k.append(b[j])
        b.append(k)
    else:
        l.append(b[j])
    j=j+1
print(l)
