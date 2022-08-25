# 1. Write a Python program to count the number of elements in a list within a specified range.


list1 = [10,20,30,40,40,40,70,80,99]
cnt = 0
for n in list1:
    if n in range(40,100):
        cnt += 1
print(cnt)