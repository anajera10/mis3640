#Exercise 1

weight = input('enter your weight:')
height = input('enter your height:')
weight = float(weight)
height = float(weight)
BMI = weight/height**2


if BMI <= 18.5:
    print ('your BMI is', BMI,)
    print ('you are underweight.')
elif BMI >= 18.5 and BMI <= 24.9:
        print ('your BMI is', BMI)
        print ('your weight is normal.')
elif BMI >= 25 and BMI <= 29.9:
        print ('your BMI is', BMI)
        print ('you are overweight.')
else: 
        print ('your BMI is', BMI)
        print ('you are obese.')
    

    




