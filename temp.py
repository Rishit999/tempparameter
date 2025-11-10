temp = float(input("Enter the Temperature in Celsius:"))
print(f"{temp}")

fahrenheit = temp * (9/5) + 32
print(f"{fahrenheit}")
if temp <= 0:
    print("Temperature is COLD!")
elif temp > 24:
    print("Temperature is HOT")

else :
    print("Temperature is Normal")
