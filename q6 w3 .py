# In Python, lambda is a keyword used to define anonymous functions(functions 
# with no name) and that's why they are known as lambda functions. Basically it 
# is used for defining anonymous functions that can/can't take argument(s) 
# and returns value of data/expression



# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# result=sorted(Sample_List,key=lambda x:x[1])
# print(result)
r=sorted(a,key=lambda i:i[1])
print(r)
