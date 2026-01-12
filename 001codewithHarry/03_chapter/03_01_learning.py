# ch3 STRINGS
# we can't perform any change in a string
general_string = "Jerry\\"
print(general_string)
# remember that there is no charater (char) data type in Python

# topic 01 String Slicing

name = "Mahendra Singh Dhoni"

print(name[1]) #will print char at index 01
print(name[:]) 

# if there's nothing then it will be [0,len(name)+1] , its include the first index , but not the last index 
print(name[0:7]) 

# here it will only go to the 6th indexing not the 7th, the indexing starts from 0.

print(name[-8:-1])
# to perform indexing from the end we can use negative numbers , its indexing will start from -1, -1 corresponds to '' len(name) - 1 ''
print(name[::2]) # 2 is here the skip value 

# syntax name[starting index : ending index : skip value]
# where ending index is not included

#topic 02 , length of a string

ex01 = "this is a \'string\' , 22, since numbers are written in strings , you cant find numbers here"

print(len(ex01))

# performing other operation on string
print(ex01.endswith("by by")) #will check the string ending
print(ex01.count("i")) # will count occurance of i
print(ex01.capitalize())#capatilise 1st alphabet
print(ex01.find("is"))# return 1st occ. index
print(ex01.find("22"))
print(ex01.replace("a","the").replace("22", "333"))