# a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # Expected Output : ['Green', 'White', 'Black']
# i=0
# h=[]
# while i<len(a):
#     if i==0 or i==4 or i==5:
#         a.remove(a[i])
#     i=i+1
# print(a)


li1=[2,23,312]
li2=[12,12,31]
def common(li1,li2):
    for i in li1:
        if i in li2:
            return True
        else:
            return False
print(common(li1,li2))