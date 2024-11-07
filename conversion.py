response = input("Do you and to enter a distance in meters (yes/no): ")
if (response == "yes"):
    distance = int(input("What is the distance in meters: "))
    inches = int(distance * 39.3701)
    feet = inches // 12
    inches = inches % 12
    print(str(distance) + " meters is " + str(feet) + " feet " + str(inches) + " inches.")
else:
    distance = int(input("What is the distance in feet: "))
    inches = distance * 12
    meters = int(inches / 39.3701)
    print(str(distance) + " feet is " + str(meters) + " meters.")
print("Thank you")