# python automatically identified the data type(int,float,string,booleans)
# char data type is not available in Python


# opertaors in Python 
# 01 Arithmetic  ( + , - , * , / , etc)
# 02 Assignment  ( = , += , -= , etc)
# 03 Comparision ( == , > , >= , < , !=(not) )
# 04 LOgical ( and , or , not )

# to know the type of a data
var1 = 32
var2 = "jerry"
var3 = True 
var4 = 9.33
print(type(var1),"\n",type(var2),"\n",type(var3),"\n",type(var4))

# how to get input from the user
# "input" generally take 'string' as the data type

print("")
userip01 = input("write the string : ")
print(f"what you wrote :{userip01}") 

#its called TYPECASTING , used to change the data type of the input

userip02 = int(input("choose a number : "))
userip03 = float(input("choose a float : "))

print(f"the integer you choose : {userip02} \nthe float value you choos : {userip03}")