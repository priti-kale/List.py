# 70. Write a Python program to find the items starts with specific character from a given list. Go to the editor
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']




a=['abcd','dbcd','bkie','cder','cdsw','sdfsd','dagfa','acid']
b=input("insert input ")
i=0
s=[]
while i<len(a):
    j=0
    while j<1:
        if a[i][j]==b:
            s.append(a[i])
        j=j+1
    i=i+1
print(s)
