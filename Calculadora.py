print("---------------------------------------------------------------------------------------------------------")
name = input("Welcome, please enter your name: ")
print("---------------------------------------------------------------------------------------------------------")
print(f"Welcome! {name}")
x = 0
veri = "Y"
while veri == "Y":
    chooseTheOperation = int(input("Press 1 to add, press 2 to subtract, press 3 to multiply, or press 4 to divide.\n"))
    numero1 = int(input("Enter the first number: "))
    numero2 = int(input("Enter the second number: "))

#Suma
    if  chooseTheOperation == 1:
            x = numero1 + numero2
            print(f"The result is: {x}") #Resultado de la operación
#Resta
    if chooseTheOperation == 2:
            x = numero1 - numero2
            print(f"The result is: {x}") #Resultado de la operación
#Multiplicar
    if chooseTheOperation == 3:
            x = numero1 * numero2
            print(f"The result is: {x}") #Resultado de la operación
#Dividir
    if chooseTheOperation == 4:
            x = numero1 / numero2
            print(f"The result is: {x}") #Resultado de la operación
    
    veri = input("Do you want to use the calculator again? Enter [Y/N]").upper()
print("Thank you for use the calculator!. Nice to meet you!")