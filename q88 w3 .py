# 88. Write a Python program to read a square matrix from console and 
# print the sum of matrix primary diagonal. Accept the size of the square
#  matrix and elements for each column separated with a space (for every row) 
# as input from the user. Go to the editor
# Input the size of the matrix: 3
# 2 3 4
# 4 5 6
# 3 4 7
# Sum of matrix primary diagonal:
# 14

a=[[2,3,4],
[4,5,6],
[3,4,7]]
i=0
sum=0
while i <len(a):
    j=i
    while j<=i:
        sum=sum+a[i][j]
        j=j+1
    i=i+1
print(sum)

