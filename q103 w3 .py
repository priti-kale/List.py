# 103. Write a Python program to extract specified number of elements from a given list, which follows each other continuously. Go to the editor
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Extract 2 number of elements from the said list which follows each other continuously:
# [1, 4]
# Original lists:
# [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# Extract 4 number of elements from the said list which follows each other continuously:
# [4]


a=[1, 1, 3, 4, 4, 5, 6, 7]
i=0
b=[]
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]==a[j]:
            b.append(a[i])
        j=j+1
    i=i+1
print(b)