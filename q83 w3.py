# print(sum)

# 3. Write a Python program to round every number of a given list of numbers 
# and print the total sum multiplied by the length of the list. Go to the editor
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# Result:
# 243


a= [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
i=0
sum=1
while i<len(a):
    sum=sum+a[i]
    i=i+1
print(int(sum)*len(a))

