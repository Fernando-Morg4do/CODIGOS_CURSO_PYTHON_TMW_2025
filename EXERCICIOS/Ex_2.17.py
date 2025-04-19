# faça um programa que solicite ao usuário frases. Para parar as solicitações
# ele pode apenas apertar o "ENTER"

# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida
#%%
dic_frases = {"oi":0,"ola":4,"eu":2,"nos":4,}

while True:
    frase = input("Digite uma frase")

    if frase == "":
        break
    if frase not in dic_frases:
        dic_frases[frase] = 1
    else:
        dic_frases[frase] += 1
for i in dic_frases:
    print(i, "->", dic_frases[i])


for i in dic_frases:
    dic_frases["oi"] += 1
print('oi -> ',dic_frases["oi"])
