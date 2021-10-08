#input and other variables

x = float(input("Enter length of edge1: "))
y = float(input("Enter length of edge2: "))
z = float(input("Enter length of edge3: "))

Perimeter = x + y + z

#ifelse and output

if x + y > z and x + z > y and z + y > x:
    print(f"The perimeter is {Perimeter}")
else:
    print("Input is invalid so the perimeter cannot be calculated.")