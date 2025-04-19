#%%
import random

sorteio = 5#random.randint(1, 15)
count = 3
num: int

def get_num():


    while True:

        try:
            num = input('Entre com um numero entre 1 e 15:')
            num = int(num)

            if 1 <= num <= 15:
                return num
            else:
                print('O numero {}, não um número entre 01 e 15!'.format(num))

        except:
            print('{} não é um número valido!'.format(num))

def compar_num(n1,n2):
    
    if n1 == n2:
        print('Parabéns, você acertou!')
        return True
    
    elif n1 > n2:
        print(f'Você escolheu o número {n1} o numero sorteado é menor:')
       
    
    else:
        print(f'Você escolheu o número {n1} o numero sorteado é maior:')
       
while count > 0:

    num = get_num()

    count -= 1

    if compar_num(num, sorteio):
        break
    elif count == 0 :
        print('Acabaram as suas chances, mais sorte da proxima vez!')
    else:
        print('Você ainda tem {} chance(s)'.format(count))


