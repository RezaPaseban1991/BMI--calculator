#this program calculate BMI 
#input
weight = int(input( 'If you know your weight in pound enter 1, if you know it in KG enter 2: '))

if weight == 1:
    
    weight_p = float (input(' How many pound is your weight:'))
    main_weight = weight_p * 0.453592
else:
    weight_k = float (input(' How many KG is your weight:'))
    main_weight = weight_k
    

hight = int(input( 'If you know your hight in foot enter 1, if you konw it in meter enter 2: '))

if hight == 1:
    hight_f = float (input('How many foot is your hight:'))
    main_hight = hight_f * 0.3048
    
else:
    hight_m = float (input('How many meter is your hight:'))
    main_hight = hight_m

#cal   
bmi = main_weight / main_hight ** 2
if bmi < 15:
    result = 'very severely under weight'
elif bmi >= 15 and bmi < 16:
    result = 'severely under weight'
elif bmi >= 16 and bmi < 18.5:
    result =  'under weight'
elif bmi >= 18.5 and bmi < 25:
    result = 'normal'
elif bmi >= 25 and bmi < 30: 
    result = 'over weight'
elif bmi >= 30 and bmi < 35:
    result = 'moderteky obese'
elif bmi >= 35 and bmi < 40:
    result = 'severely obese'
elif bmi >= 40:
    result = 'very severely obese'
bmi_round = format(bmi, '.2f')

#output
print('Your BMI is ',bmi_round,' so your are in ' + result + ' level.' )

    
    
