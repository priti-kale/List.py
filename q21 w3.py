

# # 21. Write a Python program to convert a list of characters into a string.
a=["g","a","u","r","a","v"]
i=0
s=""
while i<len(a):
    s=s+a[i]
    i=i+1
print(str(s))


a=['g','a','u','r','a','v']
b=''.join(s)
print(b)