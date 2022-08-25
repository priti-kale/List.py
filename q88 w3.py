# 




m = [
[1 , 3 , 3],
[1 , 1 , 1],
[1 , 8 , 8],
]

print("La matrix principale : ")
for i in range(l):
    for j in range(l):
        print(m[i][j],end="\t")
print()

s = 0
for i in range(l):
    for j in range(l):
        s += m[i][j]
print(s)

# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)