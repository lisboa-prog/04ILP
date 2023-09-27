Nota1 = float(input("Digite a 1ª nota: "))
Nota2 = float(input("Digite a 2ª nota: "))
Nota3 = float(input("Digite a 3ª nota: "))
Nota4 = float(input("Digite a 4ª nota: "))

media= (Nota1+Nota2+Nota3+Nota4)/4
print(f"Media = {media:.2f}")
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")