# Project 3 - Basic temperature converter

temp = float(input("Enter the current temperature: "))
unit = input("Enter the unit of the aforementioned temperature (c, f): ")

if unit == "c":
    temp = (temp * 9 / 5) + 32
    unit = "F"
    print(f"The current temperature is {round(temp, 1)} {unit} !")
elif unit == "f":
    temp = (temp - 32) * 5 / 9
    unit = "C"
    print(f"The current temperature is {round(temp, 1)} {unit} !")
else:
    print("Invalid input !")

