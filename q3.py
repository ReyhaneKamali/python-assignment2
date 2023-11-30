a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

if a < b + c and b < a + c and c < a + b:
    print("you can draw a triangle with these numbers.")
else :
    print("it's not possible!")