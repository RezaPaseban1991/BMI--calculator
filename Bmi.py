a = float (input(' how many KG is your weight:'))
b = float (input('how many meter is your hight:'))
bmi = a / b**2
if bmi < 15:
    d = 'very severely under weight'
elif bmi >= 15 and bmi < 16:
    d = 'severely under weight'
elif bmi >= 16 and bmi < 18.5:
    d =  'under weight'
elif bmi >= 18.5 and bmi < 25:
    d = 'normal'
elif bmi >= 25 and bmi < 30: 
    d = 'over weight'
elif bmi >= 30 and bmi < 35:
    d = 'moderteky obese'
elif bmi >= 35 and bmi < 40:
    d = 'severely obese'
elif bmi >= 40:
    d = 'very severely obese'
x = round (bmi, 2)
print('Your BMI is ' + str(x) + ' so your are in ' + d + ' level.' )
    
    