rendimento_mensal = float(input("Rendimento mensal: "))
dependentes = float(input("Dependentes: "))
pensao_alimenticia = float(input("Pensao alimenticia: "))
outras_deducoes = float(input("Outras deducoes: "))

deducao_dependentes = 189.59

base_de_calculo = (
    rendimento_mensal
    - (dependentes * deducao_dependentes)
    - pensao_alimenticia
    - outras_deducoes
)

ALIQUOTA_FAIXA1 = 0
ALIQUOTA_FAIXA2 = 0.075
ALIQUOTA_FAIXA3 = 0.15
ALIQUOTA_FAIXA4 = 0.225
ALIQUOTA_FAIXA5 = 0.075
aliquota = ALIQUOTA_FAIXA1


RENDA_FAIXA1 = 1903.98
RENDA_FAIXA2 = 2826.65
RENDA_FAIXA3 = 3751.05
RENDA_FAIXA4 = 4664.68
faixa_rendimento = "Faixa 1"

aliquota = ALIQUOTA_FAIXA1

if base_de_calculo <= RENDA_FAIXA1:
    aliquota = ALIQUOTA_FAIXA1
    faixa_rendimento = "Faixa 1"
    imposto = ALIQUOTA_FAIXA1

elif base_de_calculo <= RENDA_FAIXA2:
    aliquota = ALIQUOTA_FAIXA2
    faixa_rendimento = "Faixa 2"
    imposto = (base_de_calculo - RENDA_FAIXA2) * ALIQUOTA_FAIXA2

elif base_de_calculo <= RENDA_FAIXA3:
    aliquota = ALIQUOTA_FAIXA3
    faixa_rendimento = "Faixa 3"
    imposto = (base_de_calculo - RENDA_FAIXA3) * ALIQUOTA_FAIXA3

elif base_de_calculo <= RENDA_FAIXA4:
    aliquota = ALIQUOTA_FAIXA4
    faixa_rendimento = "Faixa 4"
    imposto = (base_de_calculo - RENDA_FAIXA4) * ALIQUOTA_FAIXA4

else:
    aliquota = ALIQUOTA_FAIXA5
    faixa_rendimento = "Faixa 5"
    imposto = (base_de_calculo - RENDA_FAIXA4) * ALIQUOTA_FAIXA5


print(f"A aliquota é {aliquota:.2f}R$")
print(f"A faixa de rendimento é {faixa_rendimento}")
print(f"O imposto a pagar é {base_de_calculo:.2f}R$")
