import json

def opcao1():
    return []

def opcao2(turma):
    nome = input("Nome: ")
    id_aluno = int(input("ID: "))
    notaTPC = float(input("Nota TPC: "))
    notaProj = float(input("Nota Projeto: "))
    notaTeste = float(input("Nota Teste: "))
    turma.append((nome, id_aluno, [notaTPC, notaProj, notaTeste]))
    return turma

def opcao3(turma):
    if len(turma) == 0:
        print("A turma está vazia.")
    for aluno in turma:
        print(aluno)


def opcao4(turma):
    id_aluno = int(input("ID do aluno: "))
    encontrado = 0
    for aluno in turma:
        if aluno[1] == id_aluno:
            encontrado = aluno
    return encontrado
    


def opcao8(turma):
    nome_ficheiro = input("Nome do ficheiro: ")
    f = open(nome_ficheiro, "w", encoding="utf-8")
    json.dump(turma, f, ensure_ascii=False)
    f.close()


def opcao9():
    nome_ficheiro = input("Nome do ficheiro: ")
    f = open(nome_ficheiro, "r", encoding="utf-8")
    dados = json.load(f)
    f.close()
    turma = []
    for nome, id_aluno, notas in dados:
        turma.append((nome, id_aluno, notas))
    return turma


n = -1
turma = []
while n != 0:
  n = int(input("\n(1) Criar uma turma\n(2) Inserir um aluno na turma\n(3) Listar a turma\n(4) Consultar um aluno por id\n(8) Guardar a turma em ficheiro\n(9) Carregar uma turma dum ficheiro\n(0) Sair da aplicação\nOpção: "))
  if n == 1:
    turma = opcao1()
    print("Turma criada.")
  elif n == 2:
    turma = opcao2(turma)
  elif n == 3:
    opcao3(turma)
  elif n == 4:
    aluno = opcao4(turma)
    if aluno != None:
      print(aluno)
    else:
      print("Aluno não encontrado.")
  elif n == 8:
    opcao8(turma)
    print("Turma guardada.")
  elif n == 9:
    turma = opcao9()
    print("Turma carregada.")
if n == 0:
    print("Até à próxima!")