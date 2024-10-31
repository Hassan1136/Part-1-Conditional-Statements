
# 9. Take three sides of a triangle as input and check if they form a valid triangle.

side1 = int(input("Enter a first side of a triangle: "))
side2 = int(input("Enter a second side of a triangle: "))
side3 = int(input("Enter a third side of a triangle: "))

if side1 == side2 == side3:
    print("This is a valid triangle")
else:
    print("This is not a valid triangle")