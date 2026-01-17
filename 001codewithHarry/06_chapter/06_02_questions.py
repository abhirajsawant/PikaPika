var1 = int(input("enter a no."))
var2 = int(input("enter a no."))
var3 = int(input("enter a no."))
var4 = int(input("enter a no."))

if (var1>var2 and var1>var3 and var1>var4):
    print("var1 is greatest", var1)
elif (var1<var2 and var2>var3 and var2>var4):
    print("var2 is greatest",var2)
elif (var3>var2 and var3>var1 and var3>var4):
    print("var3 is greatest",var3)
else :
     print("var4 is greatest",var4)