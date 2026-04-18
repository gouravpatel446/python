l = [20,20.5,'hello',[1,2,3]]
print(l)
#mutable , ordered , can hold multiple dtypes


#mutable
l[0] = 1
print(l)

#can store duplicate value
empty_list =[]
numbers =[11.11,11,11,11,11]
print(empty_list)
print(numbers)

# accessing list elements 
print(numbers[0])
print(numbers[-1])


# adding elements  in list
list = [1,2,3]

list.append(4) # append after last element of list
print(list)

list.insert(1,1.1) # insert - add value at the specific index 
print(list)

list.extend([6,7,8]) # extend - extends the list from the last element 
print(list)



# updating elements into a list

list_1 = [17,23,35]
list_1[1] = 2.1
print(list_1)

#removing elements from the list
lst = [14,25,43,2,33]

lst.remove(2) # value based deletion
print(lst) #[14,25,43,33]
lst.pop(0) # index  based deletion 
print(lst) #[25,43,33]
del lst[0]
print(lst) #delete the zeroth index can also delete the whole list 


#sorting
list_2 = [2,1,3,4,5,8,9,6]
list_2.sort()
print(list_2)

#reverse
list_2.reverse()
print(list_2)
