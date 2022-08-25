# for x in range(7):
#     a=(['*'] * x)
#     for y in range(5):
#         b=[a]*y
#         for z in range(4):
#             c=([b]* z)
# # print(a)
# print(b,";")          
i=0
while i<7:
    a=(["*"]*i)
    j=0
    while j<5:
        b=([a]*j)
        s=0
        while s<4:
            c=([b]*s)
            s=s+1
        j=j+1
    i=i+1
print(c)
    
    