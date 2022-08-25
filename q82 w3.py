# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. Go to the editor
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct 

a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
i=0
b=[]
while i<len(a):
    j=i+1
    s=[]
    while j<len(a):
        d=[a[i],a[j]]
        s.append(d)
        j=j+1
    i=i+1
    b.extend(s)
    # i=i+1
print(b)


    

