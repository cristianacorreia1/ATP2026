def computador_comeca():
    total=1
    print(f"O computador jogou:1. Total atual:{total}")
    while total<100:  
      jogador=int(input("Introduza um número de 1 a 10:"))
      total=total+jogador
      print(f"Total atual:{total}")
      computador=11-jogador
      total=total+computador
      print (f"O computaodor jogou:{computador}. Total atual:{total}")
    if total==100:    
       print("O computador venceu!")

def jogador_comeca():
   total=0
   while total<100:
      jogador=int(input("Introduza um número de 1 a 10:"))
      total=total+jogador
      print(f"Total atual:{total}")
      if total < 100:
            computador=11-jogador
            total=total+computador
            print(f"O computador jogou:{computador}. Total atual:{total}")
   if total==100:
        print ("O computador venceu!")
   else:
       print ("Parabéns, venceste!")
    
   

n=input("Que modalidade deseja jogar?\n Deseja que o computador comece?(c)\n Deseja começar?(v)")
if n=="c":
    computador_comeca()
else:
    jogador_comeca()
