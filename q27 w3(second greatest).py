a=[34,85,94,23,54,34]
mx=max(a[0],a[1])
sec_max=min(a[0],a[1])
i=0
while i<len(a):
    if a[i]>sec_max and a[i]!=mx:
        sec_max=mx
        mx=a[i]
    i=i+1
print(sec_max)



# a=[1,2,3,4,5,6,7,8,9,]
# i=0
# mx=max(a[0],a[1])
# sec=min(a[0],a[1])
# while i<len(a):
#     if a[i]>sec and mx!=a[i]:
#         sec=mx
#         mx=a[i]
#     i=i+1
# print(sec)
