# LIST AND TUPLES
# list stores a set of values of any data type
# indexing is possible on string

# list are changable i.e mutable
#topic 01 list 
# idexing 
list01 = [2,"samosa",4,6,3,2,3,4,3,33,44,3,3334,"jerry","tom"]

print(list01[0])
print(list01[1])
# print(list01[55]) # error
print(list01[2:5]) # slicing of list
 
list02 = [2,4,6,3,2,3,4,3,33,44,3,3334]
# list methods
list02.sort()
print("sort" ,list02) 

list02.reverse()
print("reverse", list02)

list02.append(8) # adds 8 at the end
print("append",list02)

list02.insert(3,8)# adds 8 at 3rd index 
print("insert",list02)

print(list02.pop(2)) # delete the element at index 2nd and return its value
print("pop",list02)

list02.remove(3) # remove 3 from the list2
print("removing 3",list02)


print('''



''')

# tiple ,it is immutable i.e. not chnge_able

empty_tuple = ()
tuple_of_single_element = (2,)
general_tupule = (3 ,3,1,1,1,1,1,3,4)

print(general_tupule.count(1)) # return counts of occ. of 1 in that tuple
print(general_tupule.index(1)) # return index of 1st occurance of 1 in general_tuple