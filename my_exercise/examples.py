# response = input("What do you wand? ")
# print(response[0].upper())

# add = int(input("Enter a number to double: ")) * 2
# print(add)
# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# product = float(num1 * num2)
# print(f'the product of {num1} and {num2} is {product}')

total_miles = 0
total_gallon = 0
miles_per_gallon = 0.0
total_miles_per_gallon = 0.0
gallons = 0
counter = 0

miles = int(input("Enter miles driven or -1 to exit: "))
if miles != -1:
    gallons = int(input('Enter gallon used for the trip: '))
    counter += 1
while miles != -1:
    total_miles += miles
    total_gallon += gallons
    miles_per_gallon = float(miles / gallons)
    total_miles_per_gallon = float(total_miles / total_gallon)
    print(f'Total miles per gallon for your trip is {miles_per_gallon:.2f}')
    if counter > 1:
        print('')
        print(f'Total miles for your {counter} trips is {total_miles}')
        print(f'Total gallon for your {counter} trips is {total_gallon}')
        print(f'Total miles per gallon for your {counter} trips is {total_miles_per_gallon: .2f}')
    counter += 1
    miles = int(input(f"Enter trip {counter} mileage or -1 to exit: "))
    if miles != -1:
        gallons = int(input(f'Enter trip {counter} gallon used: '))

if total_miles != 0:
    print('')
    print(f'Total trip is {counter - 1}')
    print(f'Total miles driven is {total_miles}')
    print(f'Total gallons used is {total_gallon}')
    print(f'Total miles per gallon is {total_miles_per_gallon:.2f}')
else:
    print('No trip information found')
