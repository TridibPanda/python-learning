# User Input for BMI Calculation
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height**2)

# Determine BMI status
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 24.9:
    status = "Normal"
elif 25 <= bmi < 29.9:
    status = "Overweight"
else:
    status = "Obese"

# Print BMI Report
print("-" * 30)
print("BMI Report")
print("-" * 30)
print(f"\nName: {name}")
print(f"\nBMI: {bmi:.1f}")
print(f"\nStatus: {status}")
