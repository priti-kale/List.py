a=[0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]
i=0
d=[]
while i<len(a):
    if type(a[i])==list:
        d.extend(a[i])
    else:
        d.append(a[i])
    i=i+1
print(d)