print("Select Option")
print("Add_+")
print("Subtraction_-")
print("Multiply_*")
print("Divide_/")

option=str(input("Enter option: "))

while True:
      number_01=str(input("Enter first number: "))
      try:
           number_01=float(number_01)
           break
      except:
           print("Invaliad Number, Please Try Again.")

while True:
      number_02=str(input("Enter second number: ")) 
      try:
           number_02=float(number_02)
           break
      except:
           print("Invaliad Number, Please Try Again.")



if (option=='+'):
     result=number_01+number_02
elif (option=='-'):
     result=number_01-number_02
elif (option=='*'):
     result=number_01*number_02
elif (option=='/'):
     if (number_02==0):
          print("ZeroDivisionError")
          exit()
     else:
          result=number_01/number_02
               

print(number_01,option,number_02,'=',result)

exit()


           
           