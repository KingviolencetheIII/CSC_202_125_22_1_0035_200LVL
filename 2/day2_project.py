# A tip calcultor 
print(" Wellcome to the tip calculator ")

# get value from user
bill= float(input('What was the total bill? $') )
tip= int(input("what percentage tip would you like to give? "))
people= int(input('How many people to split the bill? '))
bill_with_tip= tip/100 * bill + bill 
bill_per_person = bill_with_tip / people
final_Amount= round(bill_per_person,2)
print(f'Each person should pay: $ {final_Amount}' )
