
# 89. Write a Python program to Zip two given lists of lists. Go to the editor
# Original lists:
# [[1, 3], [5, 7], [9, 11]]
# [[2, 4], [6, 8], [10, 12, 14]]
# Zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]

a=[[1, 3], [5, 7], [9, 11]]
b=[[2, 4], [6, 8], [10, 12, 14]]
i=0
k=[]
while i<len(a) :
    a[i].extend(b[i])
    i+=1
print(a)    


        