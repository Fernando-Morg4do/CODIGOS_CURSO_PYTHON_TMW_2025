#%%
#atribui a variavel arquivo o nome do arquiva que posteriormente será aberto e lido
arquivo = "data.csv"
#abre o arquivo o nomeia como open_file e atribui a variavel lines os registros do arquivo
#em formato de lista
with open(arquivo) as open_file:
    lines = open_file.readlines()
print(lines)
# for l in lines:
#     print(l)
# Cria as chaves que serão adicionadas a um dicionário utilizando o 1º indice da lista 
chaves = lines[0].strip("\n").split(";")

# Formas de criar um dicionário vazio
# dados = {}
# Tambem cria um  dicionario vazio
# dados = dict()

dados = dict()

#atribui as chaves ao dicionario
for c in chaves:
    dados[c]=[]


#%%

for l in lines[1: ]:
    valores = l.strip("\n").split(";")
    for i in range(0, len(valores)):
        dados[chaves[i]].append(valores[i])

dados
# %%
#criar uma lista nova vazia
idades = list()
#pegar os dados do dicionário relacionados a chave idade e converter para inteiros 
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades)/len(idades)
maior = max(idades)
menor = min(idades)
print("\n","Média:",media,"\n",
      "Maior:",maior,"\n",
      "Menor:",menor)