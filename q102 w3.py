# 102. Write a Python program to extract specified size of strings from a give list of string values. Go to the editor
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']

a=['Python', 'list', 'exercises', 'practice', 'solution']
i=0
# k=int=input("enter the length of the string to extract:")

b=[]
while i<len(a):
    
    k=int=input("enter the length of the string to extract:")
    s=len(a[i])
    if len(a[i])==k:
        b.append(a[i])
        print(a[i])
    i=i+1
print(b)