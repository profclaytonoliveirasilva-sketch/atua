
# Entrada de dados
nome = input("Digite o nome do aluno: ").title()

prova1 = float(input("Digite a nota da Prova 1: ").replace(",", "."))
prova2 = float(input("Digite a nota da Prova 2: ").replace(",", "."))
prova3 = float(input("Digite a nota da Prova 3: ").replace(",", "."))

# Cálculo da média
media = (prova1 + prova2 + prova3) / 3

# Estrutura condicional
if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperação"
else:
    situacao = "reprovado"

# Saída de dados
print("\n===== BOLETIM ESCOLAR =====")
print("Nome do aluno:", nome)
print("Nota da Prova 1:", f"{prova1:.1f}".replace(".", ","))
print("Nota da Prova 2:", f"{prova2:.1f}".replace(".", ","))
print("Nota da Prova 3:", f"{prova3:.1f}".replace(".", ","))
print("Média calculada:", f"{media:.1f}".replace(".", ","))
print("Situação:", situacao.upper())

