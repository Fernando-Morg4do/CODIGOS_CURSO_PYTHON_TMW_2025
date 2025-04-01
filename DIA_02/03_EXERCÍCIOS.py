#%%
#1- Faça um programa que de bom dia!
print("Bom dia!")
# %%
#2- Faça um programa que de bom dia, e pergunte o nome
# e reponde que é um pre=azer conhecer ela

nome = input("Bom dia, qual é o seu nome?")
print("Bom dia", nome,", é um prazer conhecer você")
# %%
#3- Crie uma historia simples.
# Adicione essa historia em um programa.
# A cada paragrafo a historia devera aguardar o 
# usuario apertar "ENTER" para dar continuidade
p1 = "Era uma vez, em uma cidade não muito longe, um jovem chamado Lucas."
print("Era uma vez, em uma cidade não muito longe, um jovem chamado Lucas.")
p2 = "Ele era conhecido por sua curiosidade"
p3 = "Um dia, enquanto explorava uma antiga biblioteca, Lucas encontrou um livro"
p4 = "O livro ensinava a programar em Python e Lucas virou programador"
p5 = "FIM"
input(p1)
input(p2)
input(p3)
input(p4)
input(p5)
# %%
#4- Faça um programa que receba um numero inteiro, 
# calcule a sua raiz quadraada e deppis exiba o resultado
num = input("Informe um numero inteiro, para saber a sua raiz quadrada")
num = int(num)
raiz = num**0.5
print("A raiz de", num,"é",raiz)
# %%
#5- Faça um programa que exiba o dobro de um numero
# inserido pelo usuário.
num = input("Insira um número para mostrar o seu dobro")
num = int(num)
dobro = num*2
print("O dobro de", num,"é igual a",dobro,"!")