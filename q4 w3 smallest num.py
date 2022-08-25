a=[8,-3,22,12,-6]
small_num=a[0]
i=0
while i<len(a):
    if a[i]<small_num:
        small_num=a[i]
    i=i+1
print(small_num)
