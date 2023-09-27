# Elaborar um algoritmo que solicita o nome de um produto, seu valor e
# quantidade, informando o valor de compra calculado.

nome_cliente = input("Digite o seu nome: ")
valor_produto = float(input("Digite o valor do produto: "))
quantidade_de_produto = int(input("Digite a quantidade de Produto: "))

valor_total_da_compra = valor_produto*quantidade_de_produto

print("\n\nDados de compra")
print('\nNome: ',nome_cliente)
print(f'\nValor total: ,{valor_total_da_compra:.2fff}')

