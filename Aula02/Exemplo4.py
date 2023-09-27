ano_nascimento = int(input("Digite a data de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual-ano_nascimento

resp=input("Você já fez aniversario esse ano? [s,n]: ")
if resp == 'n':
    idade = idade - 1
    print(f"Você tem {idade} anos de idade")
else:
    idade = idade
    print(f"Você tem {idade} anos de idade")