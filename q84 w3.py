# 84. Write a Python program to round the numbers of a given list, print the 
# minimum and maximum numbers and multiply the numbers by 5. Print the unique 
# numbers in ascending order separated by space. Go to the editor
# Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# Minimum value: 4
# Maximum value: 22
# Result:
# 20 25 45 55 60 70 80 90 110

a= [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

i=0
b=[]
d=[]
while i<len(a):
    s=int(a[i])
    b.append(s)
    d.append(s*5)
    i=i+1
print(b)
d.sort()
print(d)
i=0
min=a[0]
max=0
while i<len(b):
    if b[i]>max:
        max=b[i]
    if b[i]<min:
        min=b[i]
    i=i+1
print(min)
print(max)

