# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


a=['p','q']
n=int(input("enter the num"))
i=1
b=[]
while i<=n:
    j=0
    while j<len(a):
        b.append(a[j]+str(i))
        j=j+1
    i=i+1
print(b)

