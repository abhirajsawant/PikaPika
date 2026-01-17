hindi = int(input("hindi marks : "))
maths = int(input("maths marks : "))
physics = int(input("physics marks : "))
maxmarks = int(input("max marks: "))
per_hindi = (hindi/(maxmarks)) *100
per_maths = (maths/(maxmarks)) *100
per_phy = (physics/(maxmarks)) *100
totalper = ((hindi+maths+physics)/maxmarks*3) * 100

if (totalper>= 40 and per_hindi>=33 and per_maths>=33 and per_phy>=33):
    print("PASS",totalper//1)
else: 
    print("fail")