

# 51. Write a Python program to split a list every Nth element. Go to the editor
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
i=0
k=[]
while i<3:
    j=i
    b=[]
    while j<len(a):
        if a[j] not in b:
            b.append(a[j])
        j=j+3
    k.append(b)
    i=i+1
print(k)