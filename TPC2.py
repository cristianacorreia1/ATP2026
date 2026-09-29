
import random
def computador_pensa():
 if n=="c":
    número=random. randint(0,100)
    tentativa=int(input("Qual é o seu palpite?:"))
    tentativas=0
    while tentativa!=número:
        if tentativa>número:
            print("O número que pensei é menor")
        else:
            print("O número que pensei é maior")
        tentativa=int(input("Qual é o seu novo palpite?:"))
        tentativas=tentativas+1
    print ("Acertou. O número de tentativas:",tentativas)

def utilizador_pensa():
    maior=100
    menor=0
    tentativas=0
    while True:
         tentativa=(maior+menor)//2
         tentativas=tentativas+1
         print("o seu número é:", tentativa)
         resposta=input("O seu número é maoior, menor ou acertei?")
         if resposta=="maior":
            menor=tentativa+1
         elif resposta=="menor":
            maior=tentativa-1
         else:
            print ("Acertou")
            print("O número de tentativas:",tentativas)
            break
   

while True:
   n=input("Que modalidade deseja jogar?(p/c)")
   if n == "c":
    computador_pensa()
   else:
    utilizador_pensa()
   novamente=input("Deseja jogar novamente?(s/n):")
   if novamente!="s":
    print("Obrigada por jogares!Até à próxima!")
    break
 

