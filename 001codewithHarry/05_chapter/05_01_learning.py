# Dictionary and set

# dictionary
#its unorderd , mutable i.e. can perform changes ,indexed ,can't contain dublicate keys
dictionary_syntax = {"key" : "value"}
ex_dict = {
    "jerry" : "best",
    "berry" : "fruit",
    "alist" : [3, 6 ,9]
}

print(dictionary_syntax["key"]) #op : "value"
print(ex_dict["alist"]) # o/p: [3,6,9]

print(ex_dict.items()) #returns list of (key, value) tuples
print(ex_dict.keys()) # returns a list contain dictionary keys
print(ex_dict.update({"friends":3})) # updates the dictionary with  supplied key value pairs
print(ex_dict.get("jerry")) # return value of specified key
print(ex_dict.items()) #returns list of UPDATED (key, value) tuples

# SETS : collection of non-repetitive Elements i.e UNIQUE values
# they are Unordered , and Unindexed , and we cant perform change si in it

print('''
        ####################################
                        Sets
        ####################################
''')

ex_set1 = set()
ex_set1.add(1)
ex_set1.add(3)

print(ex_set1)

ex_set2 = {3,8,5,3,7,2,1,9}
print(len(ex_set2)) # will take in count of unique elements only
ex_set2.remove(8)
print(ex_set2)
print(ex_set2.pop()) # random element will get removed
print(ex_set2.union({8,11}))  # all items from both set
print(ex_set2.intersection({8,11,1})) # common item from both set
ex_set2.clear()
print(ex_set2)