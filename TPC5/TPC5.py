

def opcao1():
    return []

def opcao2(turma):
    nome = input("Nome: ")
    id = int(input("ID: "))
    notaTPC = float(input("Nota TPC: "))
    notaProj = float(input("Nota Projeto: "))
    notaTeste = float(input("Nota Teste: "))
    turma.append((nome, id, [notaTPC, notaProj, notaTeste]))
    return turma

def opcao3(turma):
    if len(turma) == 0:
        print("A turma está vazia.")
    for aluno in turma:
        print(aluno)


def opcao4(turma):
    id = int(input("ID do aluno: "))
    encontrado = None
    for aluno in turma:
        if aluno[1] == id:
            encontrado = aluno
    return encontrado
    


def opcao8(turma):
    nomef = input("Nome do ficheiro: ")
    f = open(nomef, "w")
    for aluno in turma:
        f.write(f"{aluno[0]},{aluno[1]},{aluno[2][0]},{aluno[2][1]},{aluno[2][2]}\n")
    f.close()



def opcao9():
    res= []
    f = open(turma, "r")
    for linha in f:
        campos = linha.strip().split(",")
        nome = campos[0]
        id_aluno = int(campos[1])
        notaTPC = float(campos[2])
        notaProj = float(campos[3])
        notaTeste = float(campos[4])
        aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
        res.append(aluno)
    f.close()
    return res



n = -1
turma = []
while n != 0:
  n = int(input("\n(1) Criar uma turma\n(2) Inserir um aluno na turma\n(3) Listar a turma\n(4) Consultar um aluno por id\n(8) Guardar a turma em ficheiro\n(9) Carregar uma turma dum ficheiro\n(0) Sair da aplicação\nOpção: "))
  if n == 1:
    turma = opcao1()
    print("Turma criada")
  elif n == 2:
    turma = opcao2(turma)
  elif n == 3:
    opcao3(turma)
  elif n == 4:
    aluno = opcao4(turma)
    if aluno != None:
      print(aluno)
    else:
      print("Aluno não encontrado")
  elif n == 8:
    opcao8(turma)
    print("Turma guardada")
  elif n == 9:
    turma = opcao9()
    print("Turma carregada")
if n == 0:
    print("Até à próxima!")