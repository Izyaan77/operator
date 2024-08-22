a= 5
if(type(a) is int):
    print("True")
else:
    print("False")


b= 36
if(type(b) is float):
    print("True")
else:
    print("False")



z= 5
y= 5
if(z is y):
    print("x and y is same identity")
y= 30
if(z is not y):
    print("x and y have different identity")