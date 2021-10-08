import math

#input

ta= float(input("Enter the temperature in Fahrenheit: "))
v= float(input("Enter the wind speed in miles per hour: "))

#input validation

while not -58 < ta < 41:
    print("Please enter a temperature between -58 degrees Fahrenheit and 41 degrees Fahrenheit.")
    ta = float(input("The temperature in Fahrenheit was out of range, please enter an accepted value: "))
while not v >= 2:
    print("please enter a wind speed greater than or equal to 2 mph.")
    v= float(input("The wind speed in miles per hour was out of range, please enter an accepted value: "))

#calculation

twc = 35.74 + (0.6215*ta) - (35.75*math.pow(v, 0.16)) + (0.4275*ta*math.pow(v, 0.16))

#output

print("The wind chill index is", format(twc, ".3f"))