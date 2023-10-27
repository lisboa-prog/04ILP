# import csv

# file_path = "amazon2.csv"

# with open("amazon2.csv", mode="r", encoding="utf-8") as arquivo2:
#     leitor = csv.reader(arquivo2, delimiter=";")

# for colu in leitor:
#     print(colu)

# import csv

# file_path = "amazon2.csv"

# with open(file_path, encoding="latin-1") as arquivo:
#     reader = csv.DictReader(arquivo, delimiter=";")
#     for row in reader:
#         print(row)

import pandas as pd

file_path = "amazon2.csv"

df = pd.read_csv(file_path)


ano_maior_mediana = df['year'][df['number'].idmax()]
ano_menor_mediana = df['year'][df['number'].idmin()]
valor_maior_meiana = df['number'].max()
valor_maior_meiana = df['number'].min()

print(f"maior foi {ano_maior_mediana}")
print(f"menor foi {ano_menor_mediana}")

for column in df.columns[3:]:
    print(f"{column}: qdt{df[column].mean():.2f}")
