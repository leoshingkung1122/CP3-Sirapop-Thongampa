def summarize(x, y):
    print(x + y)

def decrease(x,y):
    print(x - y)

def multiple(x,y):
    print(x * y)

def divide(x,y):
    print(x/y)

print("Select your Method :")
print("There are 1,2,3,4")
print("1) Summarize")
print("2) Decrease")
print("3) Multiple")
print("4) Divide")
z = int(input("Answer : "))

x = float(input("Type 1st value : "))
y = float(input("Type 2nd value : "))

if z == 1:
    summarize(x,y)
if z == 2:
    decrease(x,y)
if z == 3:
    multiple(x,y)
if z == 4:
    divide(x,y)