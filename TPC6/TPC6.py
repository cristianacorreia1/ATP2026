import matplotlib.pyplot as plt
def menu(lista):
    for op in lista:
        print(op) 
menuOpcoes=[
        "(1)-Carregar do ficheiro",
        "(2)-Gravar no ficheiro",
        "(3)-Imprimir a tabela",
        "(4)-Temperatura média por dia",
        "(5)-Temperatura mínima",
        "(6)-Amplitude térmica",
        "(7)-Dia com maior precipitação",
        "(8)-Dias em que a precipitação foi superior a um limite",
        "(9)-Desenhar gráfico da temperatura máxima, mínima e pluviosidade",
        "(0)-Sair"
    ]

def carregaTabMeteo(fnome):
     res = []
     f=open(fnome, "r")
     for linha in f:
        campos=linha.split(',')
        data=campos[0].split('|')
        ndata=(int(data[0]),int(data[1]), int(data[2]))
        res.append((ndata, float(campos[1]), float(campos[2]),float(campos[3])))
     f.close()
     return res

def guardaTabMeteo(t, fnome):
    f = open(fnome, "w")
    for registo in t:
        f.write(f"{registo[0][0]}|{registo[0][1]}|{registo[0][2]},{registo[1]},{registo[2]},{registo[3]}\n")
    f.close()

def medias(tabMeteo):
    res = []
    for registo in tabMeteo:
        data, tmin, tmax, _ = registo
        res.append((data, (tmax + tmin) / 2))
    return res

def minMin(tabMeteo):
    if not tabMeteo: 
        return None
    min_val = tabMeteo[0][1]
    for registo in tabMeteo[1:]:
        if min_val>registo[1]:
            min_val=registo[1]
    return min_val

def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, _ in tabMeteo:
        res.append((data, tmax - tmin))
    return res

def maxChuva(tabMeteo):
    if not tabMeteo:
        return None
    max_data = tabMeteo[0][0]
    max_prec = tabMeteo[0][3]
    for data, _, _, prec in tabMeteo[1:]:
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res = []
    for data, _, _, prec in tabMeteo:
        if prec > p:
            res.append((data,prec))
    return res


def maxPeriodoCalor(tabMeteo, p):
    i = 0
    imax = 0
    for _ , _ , _ , prec in tabMeteo:
        if prec < p:
           i = i + 1
        else:
           i = 0
        if i > imax:
           imax = i
    return imax


def grafTabMeteo(t):
    y_min = [tmin for _, tmin, _, _ in t]
    y_max = [tmax for _, _, tmax, _ in t]
    y_plu = [plu for _, _, _, plu in t]
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data,_,_,_ in t]
    plt.plot(x, y_min, color = "green", marker="o", label="Temperatura mínima")
    plt.plot(x, y_max, color = "red", marker="o", label="Temperatura máxima")
    plt.plot(x, y_plu, color = "blue", marker="o", label="Pluviosidade")
    plt.xlabel("Data")
    plt.ylabel("Valor")
    plt.title("Temperaturas e pluviosidade")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return

tabMeteo1=[]
menu(menuOpcoes)
op=int(input("Qual é a opção pretendida?"))
while op!=0:
    if op==1:
        ficheiro=input("Introduza o nome do ficheiro")
        tabMeteo1=carregaTabMeteo(ficheiro)
    elif op==2:
        ficheiro = input("Nome do ficheiro para gravar: ")
        guardaTabMeteo(tabMeteo1, ficheiro)
    elif op==3:
        print(tabMeteo1)
    elif op == 4:
        print(f"Temperaturas Médias: {medias(tabMeteo1)}")
    elif op == 5:
        print(f"Temperatura mínima mais baixa: {minMin(tabMeteo1)}°C")
    elif op == 6:
        print(f"Amplitude Térmica:{amplTerm(tabMeteo1)}")
    elif op == 7:
        data_m, prec_m = maxChuva(tabMeteo1)
        print(f"Dia com maior precipitação: {data_m} com {prec_m}mm")
    elif op == 8:
        lim =int(input("Insira o Limite que pretende usar"))
        print(f"Dias chuvosos: {diasChuvosos(tabMeteo1, lim)}")
    elif op == 9:
        grafTabMeteo(tabMeteo1)
    else:
        print("Operação não reconhecida")

    print("\n")
    menu(menuOpcoes)
    op = int(input("Qual é a opção pretendida? "))
print("A sair do programa.")


