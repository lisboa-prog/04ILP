num1 = int(input("Digite 0 1º numero: "))
num2 = int(input("Digite 0 2º numero: "))
num3 = int(input("Digite 0 3º numero: "))

if num1 < num2:
    if num1 < num3:
        print("O primeiro numero é o menor")
    else:
        print("O terceiro numero é o menor")
else:
    if num2 < num3:
        print("O segundo numero é o menor")
    else:
        print("O terceiro numero é o menor")
