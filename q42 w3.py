

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']

missingintwo = list(set(list1) - set(list2))
additionalintwo = list(set(list2)-set(list1))

print("missing values in second list: " + str(missingintwo))
print("aditional values in second list: " + str(additionalintwo))