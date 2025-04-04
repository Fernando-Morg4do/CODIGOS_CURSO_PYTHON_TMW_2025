#%%
# 06 - Faça um programa que vende água:
# Se o cliente pedir água natural será cobrado R$ 1.50
# Se o cliente pedir água com gás, será cobrado R$ 2.50
aguanatural = 1.50
aguacgas = 2.50
print("""Escolha e digite o número da sua opção:
      
    1 para Água Natural
    2 para Água com Gás""")

escolha = input("Digite a sua opção")

escolha = float(escolha)

if escolha == 1:
    print("""
          
Você escolheu Água Natural, sua conta é R$""",aguanatural)
elif escolha == 2:
    print("""
          
Você escolheu Água com Gás, sua conta é R$""",aguacgas)
else:
    print("""
          
          
Você Digitou uma opção INVÀLIDA !""")
# %%
