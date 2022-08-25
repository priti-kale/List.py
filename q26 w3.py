# 26. Write a python program to check whether two lists are circularly identical.

list1 = [10, 10, 0, 0, 10]
list1.sort()
list2 = [10, 10, 10, 0, 0]
list2.sort()
if list1==list2:
    print('Identical')
else:
    print("not identical")