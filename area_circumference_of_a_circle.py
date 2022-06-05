import math
radius = int(input("Enter radius: "))
circumference = round(2 * (math.pi * radius))
area = round(math.pi * (radius ** 2))
print("The area and circumference of a circle with radius", radius, "is", area,  "and", circumference)
