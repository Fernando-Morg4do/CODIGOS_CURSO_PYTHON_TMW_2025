#%%
# 07 - Faça um programa que vende água:
# Se o cliente pedir água natural será cobrado R$ 1.50
# Se o cliente pedir água com gás, será cobrado R$ 2.50
# Ofereça a opção para comprar mais que uma garrafa.
# Apresente o valor total no final da compra.
aguanatural = 1.50
aguagas = 2.50
print("""Escolha e digite o número da sua opção:
      
    1 para Água Natural
    2 para Água com Gás""")

escolha = input("Digite a sua opção:")
qtd = input("Digite a quantidade:")

escolha = float(escolha)
qtd = int(qtd)

if escolha == 1:
    print("""
          
Você escolheu Água Natural""")
elif escolha == 2:
    print("""
          
Você escolheu Água com Gás, sua conta é R$""",aguagas)
else:
    print("""
          
          
Você Digitou uma opção INVÀLIDA !""")