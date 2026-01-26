# question 01

username = input("writ eyour name: ")
print(f"good affternoon, \n\t {username}")

# question 02

letter = '''
Dear <|name|>,
    You are Seleted!
    Meet us on at <|date|>
'''
name = input("write your name: ")
date = input("choose your preferred date: ")

print(letter.replace("<|name|>", name).replace("<|date|>", date))


#question 03 

sample_text = "this is a semple test  so thatbwe cam find  double space occurance in this string"

print(sample_text.find("  "))

# question 04

print(sample_text.replace("  "," "))

# question 05

sample_text2 = "this is a semple test,\n\tso thatbwe cam find double space occurance\n\tin this string"
print(sample_text2)