
import random
def computador_pensa():
    número=random. randint(0,100)
    tentativa=int(input("Qual é o seu palpite?:"))
    tentativas=1
    while tentativa!=número:
        if tentativa>número:
            print("O número que pensei é menor")
        else:
            print("O número que pensei é maior")
        tentativa=int(input("Qual é o seu novo palpite?:"))
        tentativas=tentativas+1
    print ("Acertou! O número de tentativas:",tentativas)

def utilizador_pensa():
    maior=100
    menor=0
    tentativas=0
    resposta = ""
    while resposta != "acertou":
        tentativa = (maior + menor) // 2
        tentativas = tentativas + 1
        print("O seu número é:", tentativa)
        resposta = input("O seu número é maior, menor ou acertei?: ")
        
        if resposta == "maior":
            menor = tentativa + 1
        elif resposta == "menor":
            maior = tentativa - 1
    print("O número de tentativas:", tentativas) 

n=input("Que modalidade deseja jogar?(p/c)")
if n == "c":
    computador_pensa()
else:
    utilizador_pensa()


 

