print("Welcome to the BMI calculator!")
weight=float(input("Enter your weight in Kgs: "))
height=float(input("Enter your height in Meters: "))
bmi = weight/ (height**2)
print("Your BMI is",bmi)
if bmi<=18.5:
    print("You are underweight!")
elif bmi<=24.9:
    print("You are average!")
elif bmi<=29.9:
    print("You are overweight!")
elif bmi<=34.9:
    print("You are obese!")
else:
    print("You are extremely obese!")