# bmi calculation formula:
# bmi=(weight in kilograms)/((height in centimeters/100) to the power of 2)
# below 18.5 is underweight
# between 18.5 and 24.9 is healthy
# between 25 and 29.9 is overweight
# of 30 or over is obese

def bmiCalculator():
    weight=input("Enter your weight in kilograms: ")
    height=input("Enter your height in centimeters: ")
    weight=float(weight)
    height=float(height)
    bmi=(weight)/((height/100)**2)
    if bmi>0:
        if bmi<18.5:
            print("Your BMI is "+f"{bmi:.2f}"+" and you are underweight.")
        elif bmi>=18.5 and bmi<=24.9:
            print("Your BMI is "+f"{bmi:.2f}"+" and you are healthy.")
        elif bmi>=25 and bmi<=29.9:
            print("Your BMI is "+f"{bmi:.2f}"+" and you are overweight.")
        elif bmi>=30 and bmi<=100:
            print("Your BMI is "+f"{bmi:.2f}"+" and you are obese!")
        else:
            print("Please check that you have entered the correct information.")           
    else:
        print("Please check that you have entered the correct information.")

bmiCalculator()