# 104. Write a Python program to find the difference between consecutive numbers in a given list. Go to the editor
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Difference between consecutive numbers of the said list:
# [0, 2, 1, 0, 1, 1, 1]
# Original list:
# [4, 5, 8, 9, 6, 10]
# Difference between consecutive numbers of the said list:
# [1, 3, 1, -3, 4]

# a=[4, 5, 8, 9, 6, 10]

a=[1, 1, 3, 4, 4, 5, 6, 7]
i=0
b=[]
j=i+1
while i<len(a) and j<len(a): 
    d=a[j]-a[i]
    b.append(d)
    j=j+1
    i=i+1
print(b)
    