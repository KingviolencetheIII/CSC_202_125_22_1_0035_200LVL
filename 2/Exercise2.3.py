# Create a program using maths and f-strings that tells us 
# how many days,weeks,months we have left if we live 90years old

age= input('what is your current age? ')

age_as_int= int(age)

years_remaining= (90 - age_as_int)

days_remaining= years_remaining * 365
weeks_remaining= years_remaining *52
months_remaining= years_remaining* 12

messages= (f'You have {days_remaining} days,{weeks_remaining} weeks and {months_remaining }months left ')
print( messages)

