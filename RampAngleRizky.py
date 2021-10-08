import math

#input and constant g

Mass = float(input("Enter the mass of the cart (in kg): "))
Force = float(input("Enter the force used to push the cart(in N): "))
Gravity = 9.8

#calculations. sin^-1 (F/mg) = Angle

Angle = math.asin( Force / (Mass*Gravity) )
AngleDegrees = round(math.degrees(Angle), 1)

#Output

print(f"The angle of the ramp is {AngleDegrees} degrees")