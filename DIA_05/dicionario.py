#%%

lista = [2, 132, "teo",["ds","de","da"], True]

lista[-2][0]
# %%


# Dicionários são pares de chave/valor


dados_teo ={
    "sobrenome":"Calvo",
    "nome":"teo",
    "filhos": True,
    "formacao":["estatistica","bigdata","datascience"],
    "cargos":[
        {"nome": "ds jr.", "empresa": "tapps"},
        {"nome": "ds pl.", "empresa": "sas"},
        {"nome": "ds sr.", "empresa": "boticario"},
        {"nome": "ds espec.", "empresa": "via varejo"},
    ]
    }
#%%

print(dados_teo)
print(dados_teo["formacao"][-1])
print(dados_teo["cargos"][-1]["empresa"])

#%%

dados_teo["estado civil"] = "casado" 


# %%
print("chaves:",dados_teo.keys())
print("valores:",dados_teo.values())
print("itens:",dados_teo.items())


# %%


for i in dados_teo:
    print(i,"->", dados_teo[i])


# %%


