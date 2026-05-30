# Inicio do codigo - Menu 

print ("=" * 40)
print ("           Imobíliaria RM        ")
print ("=" * 40)

print ("[1] Apartamento")
print ("[2] Casa")
print ("[3] Estudio")

print ("=" * 40)

tipo = input("Escolha a opçao desejada: ")
aluguel = 0
descriçao = ""

#Tipo de Residencia e Calculo do aluguel

#tipo 1

if tipo == "1":
    descriçao = "Apartamento"
    aluguel = 700

    quartos = int(input("Quantos quartos ?, 1 ou 2: "))
    if quartos == 2:
        aluguel += 200
        
    garagem = input("Deseja vaga na garagem ?, (s/n:) ")
    if garagem.lower() == "s":
        aluguel += 300
    
    criancas = input("Possui crianças ?, s ou n :")
    if criancas.lower() == "n":
        desconto = aluguel * 0.05
        aluguel -= desconto


#Tipo 2

elif tipo == "2":
    descriçao = "Casa"
    aluguel = 900

    quartos = int(input("Quantos quartos ?, 1 ou 2: "))
    if quartos == 2:
        aluguel += 250
        
    garagem = input("Deseja vaga na garagem ?, (s/n:) ")
    if garagem.lower() == "s":
        aluguel += 300
    

#Tipo 3

elif tipo == "3":
    descriçao = "Estudio"
    aluguel = 1200

    estacionamento = input("Deseja vaga de estacionamento ? (s/n): ") 
    if estacionamento.lower() == "s":
        aluguel += 250

    vagas_extras = int(input("Quantas vagas extras deseja adicionar? "))
    aluguel += vagas_extras * 60

    
    print("Opção invalida")
    exit()


#Calculo do contrato

valor_contrato = 2000
parcelas = int(input("Parcerlar contrato em até 5x. Quantas parcelas deseja ?: "))

if parcelas < 1 or  parcelas > 5:
    print ("Numero de parcelas invalido")
    exit ()

valor_parcela = valor_contrato / parcelas
#Tela final

print ("=" * 40)
print ("           Orçamento Final        ")
print ("=" * 40)


print(f"Imóvel escolhido: {descriçao}")
print(f"Valor do aluguel mensal: R$ {aluguel:.2f}")
print(f"Contrato imobiliário: R$ {valor_contrato:.2f}")
print(f"Parcelamento do contrato: {parcelas}x de R$ {valor_parcela:.2f}")

print ("=" * 40)


#CSV
import csv 
gerar_csv = input("\nDeseja gerar arquivo CSV com 12 parcelas do aluguel? (s/n): ")

if gerar_csv.lower() == "s":

    with open("orcamento_imobiliaria.csv", mode="w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(["Mês", "Valor do Aluguel"])

        for mes in range(1, 13):
            escritor.writerow([f"Mês {mes}", f"R$ {aluguel:.2f}"])

    print("Arquivo 'orcamento_imobiliaria.csv' gerado com sucesso!")

#Fim do Programa

print("\nSistema finalizado.")
