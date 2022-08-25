a=['be','have','do','say','get','make','go','know','take','see','come','think',
'look','want','give','use','find','tell','ask','work','seem','feel','leave','call','abc','ab']
n=input("enter: ")
b=[]
count=0
# for i in a:
#     if i[0]==n:
#         b.append(i)
# print(b)
i=0
while i<len(a):
    if a[i][0]==n:
        b.append(a[i])
    i=i+1
print(b)