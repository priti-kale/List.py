# second smallest number in a list

a=[12,97,53,23,1,85]
i=0
min=a[0]
sec_min=a[0]
while i<len(a):
    if a[i]<min:
        min=a[i]
    if a[i]<sec_min and a[i]!=min:
        sec_min=a[i]
    i=i+1
print(min)
print(sec_min)
