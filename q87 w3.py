# 87. Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user. Go to the editor
# Input rows: 2
# Input columns: 2
# Input number of elements in a row (1, 2, 3):
# 1 2
# 3 4
# sum for each column:
# 4 6 

row=int(input("enter the row:"))
col=int(input("enter the col: "))
i=0
k=[]
while i<=row:
    j=i+1
    b=[]
    while j<=col:
        b.append(i)
        j=j+1
    k.append(b)
    i=j+1
print(k)
