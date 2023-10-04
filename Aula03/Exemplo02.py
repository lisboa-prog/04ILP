pontuacao_time_01 = int(input("Digite a pontuação do 1º time: "))
pontuacao_time_02 = int(input("Digite a pontuação do 2º time: "))

if pontuacao_time_01 > pontuacao_time_02:
    print("T01")
elif pontuacao_time_01 < pontuacao_time_02:
    print("T02")
else:
    print("Empate")
