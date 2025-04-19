#%%

def soma_1(a:float,b:float):
    
    return a+b

def media_1(a=int,b=int):

    return soma_1(a,b)/2

a = float(input("digite um numero"))
b = float(input("digite outro numero"))

print("A soma de",a,"mais",b,"é",soma_1(a,b))
print("A media de", a, "e", b,"é", media_1(a,b))

#%%

valores = [1,2,3,4,5]

def soma_2 (valores:list) -> float:

    return sum(valores)


print(soma_2(valores))
# %%
# # 
a = float(5)
b = float(4)
c =[40,7,8,2,11]

print(soma_2(c),"e",soma_1(a,b))
# %%

def par_impar(a:int):
    if a%2 == 0:
        print(a,"é par!")
    else:
        print(a,"é impar!")

while True :
    try:
        a = int(input("Entre com um número inteiro"))
        par_impar(a)
    except:
        print("Você entrou com um valor inválido!")
        break
  
# %%
def soma (a:float, b:float, *args) -> float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)-> float:
    media_total = soma(a,b,*args)/(len(args)+2)
    return media_total

a = float(2)
b = float(2)
c = float(3)
d = float(5)
e = float(11)


# a = float(input("Numero a:"))
# b = float(input("Numero b:"))
# c = float(input("Numero c:"))
# d = float(input("Numero d:"))
# e = float(input("Numero e:"))

print("Média",media(a,b,c,d,e))
print("Soma:",soma(a,b,c,d,e))

# %%
def calc_impostos(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    return imposto


#%%
impostos_gerais = {
    "Municipal":0.01,
    "Estadual":0.05,
    "Nacional": 0.001,
    "Internacional": 0.1,

}

calc_impostos(100,0.03, **impostos_gerais)