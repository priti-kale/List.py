# 85. Write a Python program to create a multidimensional list (lists of lists) with zeros. Go to the editor
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

# a=[[0, 0], [0, 0], [0, 0]]
i=0
b=[]
while i<3:
    j=0
    s=[]
    while j<2:
        s.append(0)
        j=j+1
    i=i+1
    b.append(s)
print(b)
        
