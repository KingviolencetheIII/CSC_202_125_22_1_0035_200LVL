# The BMI is calculated by dividing a person's weight(in kg)by the squareof their height(in m)

weight= input("Enter the value of the weight in kg? ")
height= input(" Enter the value of the height in m? ") 

bmi= (float(weight) / float(height)**2)

bmi_as_int=int(bmi)
print(bmi_as_int)

