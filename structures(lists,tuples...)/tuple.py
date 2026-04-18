# all the obejcts known as elements seprated by comma enclosed in paranthesis().
empty_tuple = ()

int_tuple = (13,56,27,18,11,23)
print(int_tuple)

mixed_tuple = (6,"tpoint",17.43)
print(mixed_tuple)

tuple_1 = ("apple","mango","banana","orange","guava","berries")
print(tuple_1[0]) 

# changing the elements in tuple
# 1. convert tuple to list
# 2. change element
# 3. convert back to tuple

list_1 = list(tuple_1)
list_1[1] = "aam"
fruit_tuple = tuple(list_1)

print(fruit_tuple)

#adding elements in tuple
t = (1,2,3)
lst = list(t)
lst.append(4)
t = tuple(lst)
print(t)