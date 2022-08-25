# 32. Write a Python program to check whether a list contains a sublist. 


# a=[2,4,3,5,7]
# c=[3,7]
# b=[4,3]

# if ''.join(map(str,b)) in ''.join(map(str,a)):
#     print('true')
# else:
#     print('false')




lst = ['X','Y','Z']
lst1= [[]]
for x in range(len(lst)):
    count = x+1
for y in range(count,len(lst)+1):
    sub = lst[x:y]
    lst1.append(sub)
count+=1
r=lst1
