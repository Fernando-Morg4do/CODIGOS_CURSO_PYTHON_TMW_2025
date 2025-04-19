#%%
# import random

# def jogo_sorteio():
#     numero_sorteado = random.randint(1, 15)
#     print("Tente adivinhar o número entre 1 e 15. Você tem 3 chances!")

#     for tentativa in range(1, 4):  # 3 tentativas
#         palpite = int(input(f"Tentativa {tentativa}: Qual o seu palpite? "))

#         if palpite == numero_sorteado:
#             print("Parabéns! Você acertou o número!")
#             break
#         elif palpite > numero_sorteado:
#             print("Seu palpite foi maior que o número sorteado.")
#         else:
#             print("Seu palpite foi menor que o número sorteado.")

#     else:  # Executa se o laço terminar sem o usuário acertar
#         print(f"Que pena! O número sorteado era {numero_sorteado}.")

# jogo_sorteio()

# %%
import random

def validar_input(prompt):
    while True:
        try:
            palpite = int(input(prompt))
            if 1 <= palpite <= 15:
                return palpite
            else:
                print("Por favor, insira um número entre 1 e 15.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

def jogo_sorteio():
    numero_sorteado = random.randint(1, 15)
    print("Tente adivinhar o número entre 1 e 15. Você tem 3 chances!")

    for tentativa in range(1, 4):  # 3 tentativas
        palpite = validar_input(f"Tentativa {tentativa}: Qual o seu palpite? ")

        if palpite == numero_sorteado:
            print("Parabéns! Você acertou o número!")
            break
        elif palpite > numero_sorteado:
            print("Seu palpite foi maior que o número sorteado.")
        else:
            print("Seu palpite foi menor que o número sorteado.")
    else:  # Executa se o laço terminar sem o usuário acertar
        print(f"Que pena! O número sorteado era {numero_sorteado}.")

jogo_sorteio()