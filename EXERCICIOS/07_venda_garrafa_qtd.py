#%%
# 07 - Faça um programa que vende água:
# Se o cliente pedir água natural será cobrado R$ 1.50
# Se o cliente pedir água com gás, será cobrado R$ 2.50
# Ofereça a opção para comprar mais que uma garrafa.
# Apresente o valor total no final da compra.

dic = {"1":[1,1.50,"Água Natural",],
       "2":[2,2.50,"Água com Gás"],
       }

while True:
    print("""Escolha entre as opções abaixo:
             
          Água Natural R$ 1,50 -> Digire 1

          Água com Gás R$ 2,50 -> digite 2
          
          
          """)
    tipo = input("Entre com a opção desejada:  ")
    if tipo == "1" or tipo == "2":
        break
    else:
        print("Entre com uma opção valida!")

while True:

    try:
        qtd = int(input("Informe a quantidade: "))
        break
    except ValueError : print(" Valor inválido!")

preco = 0
agua = ""
tipo = int(tipo)

for i in dic:
    if tipo == dic[i][0]:
        preco = qtd * dic[i][1]
        agua = dic[i][-1]
        print("Você escolheu",qtd," -> ",agua,"Sua conta é R$",preco)