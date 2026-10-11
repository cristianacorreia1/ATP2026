
listaint=[]
import random

def opcao1(listaint):
    lista=[]   
    m = int(input("Quantos números quer na lista? "))
    for i in range(m):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista     



def opcao2(listaint):
    lista=[]
    q=int(input("Quantos números quer na lista?"))
    while q>0:
        num=int(input("Introduza um número"))
        lista.append(num)
        q=q-1 
    return lista


def opcao3(listaint):
    somar=0
    for n in listaint:
        somar=somar+n
    return somar



def opcao4(listaint):
    soma=0
    for n in listaint:
        soma=soma+n
    media=soma/len(listaint)
    return media



def opcao5(listaint):
    maior=listaint[0]
    for n in listaint:
        if n>maior:
            maior=n
    return maior


def opcao6(listaint):
    menor=listaint[0]
    for n in listaint:
        if menor>n:
            menor=n
    return menor



def opcao7(listaint):
   res=True
   for n in range(len(listaint)-1):
      if listaint[n]>listaint[n+1]:
       res=False
   return res



def opcao8(listaint):
    res=True
    for n in range(len(listaint)-1):
        if listaint[n]<listaint[n+1]:
            res=False
    return res



def opcao9(listaint):
    elemento=int(input("Que elemento quer procurar na lista?"))
    res=-1
    i=0
    while i<len(listaint) and res==-1:
        if listaint[i]==elemento:
         res=i
        else:
         i=i+1
    return res


n=-1
while n!=0:
  n=int(input("(1) Criar Lista\n""(2) Ler Lista\n""(3) Soma\n(4) Média\n(5) Maior\n(6) Menor\n(7) estaOrdenada por ordem crescente\n(8) estaOrdenada por ordem decrescente\n(9) Procura um elemento\n(0) Sair"))
  if n == 1:
    listaint = opcao1(listaint)
    print(listaint)  
  elif n==2:
    listaint=opcao2(listaint)
    print (listaint)
  elif n==3:
    resultado=opcao3(listaint)
    print(f"A soma dos elementos da lista é {resultado}")
  elif n==4:
    resultado=opcao4(listaint)
    print(f"A média dos elementos da lista é {resultado}")
  elif n==5:
    Maior=opcao5(listaint)
    print(f"O maior elemento da lista é {Maior}")
  elif n==6:
    Menor=opcao6(listaint)
    print(f"O menor elemento da lista é {Menor}")
  elif n==7:
    crescente=opcao7(listaint)
    if crescente==True:
        print("Sim. A lista está em ordem crescente")
    else:
        print("Não. A lista não está em ordem crescente")           
  elif n==8:
    decrescente=opcao8(listaint)
    if decrescente==True:
        print("Sim. A lista está em ordem decrescente")
    else:
        print("Não. A lista não está em ordem decrescente")
  elif n==9:
    posicao=opcao9(listaint)
    if posicao!=-1:
        print(f"O elemento está na posição {posicao}")
    else:
       print("O elemento não está na lista.")
if n==0:
   print(f"A lista final é: {listaint}")