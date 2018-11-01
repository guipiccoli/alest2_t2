
def lista_adjacencia(lst_nodos):
    global file
    for i in range(len(lst_nodos)):
        #Se superior não tiver parede recebe o nodo acima ou None
        if(lst_nodos[i].entrada == False and lst_nodos[i].saida == False):
            if lst_nodos[i].superior == '0':
                    lst_nodos[i].superior = lst_nodos[i-int(nm)]

            #Se esquerda não tiver parede recebe o nodo a esquerda ou None
            if lst_nodos[i].esquerda == '0':
                lst_nodos[i].esquerda = lst_nodos[i-1]

            #Se direita não tiver parede recebe o nodo a direita ou None
            if lst_nodos[i].direita == '0':
                    lst_nodos[i].direita = lst_nodos[i+1]

            #Se inferior não tiver parede recebe o nodo abaixo ou None
            if lst_nodos[i].inferior == '0':
                    lst_nodos[i].inferior = lst_nodos[i+int(nm)]

            if lst_nodos[i].entrada == True:
                print("entrada")
            if lst_nodos[i].saida == True:
                print("saida")
        else:
            if lst_nodos[i].superior == '0':
                if(lst_nodos[i].saida == 'N' or lst_nodos[i].entrada == 'N' ):
                    lst_nodos[i].superior = None
                else:
                    lst_nodos[i].superior = lst_nodos[i-int(nm)]
            if lst_nodos[i].esquerda == '0':
                if(lst_nodos[i].saida == 'O' or lst_nodos[i].entrada == 'O' ):
                    lst_nodos[i].esquerda = None
                else:
                    lst_nodos[i].esquerda = lst_nodos[i-1]

            if lst_nodos[i].direita == '0':
                if(lst_nodos[i].saida == 'L' or lst_nodos[i].entrada == 'L' ):
                    lst_nodos[i].direita = None
                else:
                    lst_nodos[i].direita = lst_nodos[i+1]

            if lst_nodos[i].inferior == '0':
                if(lst_nodos[i].saida == 'S' or lst_nodos[i].entrada == 'S' ):
                    lst_nodos[i].inferior = None
                else:
                    lst_nodos[i].inferior = lst_nodos[i+int(nm)]
















def lista_adjacencia(lst_nodos):
    global file
    for i in range(len(lst_nodos)):
        #Se superior não tiver parede recebe o nodo acima ou None
        if lst_nodos[i].superior == '1':
            #file.write(svgline(i, i%int(nm), i+1, i%int(nm)))
            lst_nodos[i].superior = None
        else:
            if(lst_nodos[i].superior != None):
                lst_nodos[i].superior = lst_nodos[i-int(nm)]

        #Se esquerda não tiver parede recebe o nodo a esquerda ou None
        if lst_nodos[i].esquerda == '1':
            #file.write(svgline(i, i%int(nm), i, i%int(nm)+1))
            lst_nodos[i].esquerda = None
        else:
            lst_nodos[i].esquerda = lst_nodos[i-1]

        #Se direita não tiver parede recebe o nodo a direita ou None
        if lst_nodos[i].direita == '1':
            #file.write(svgline(i+1, i%int(nm), i+1, i%int(nm)+1))
            lst_nodos[i].direita = None
        else:
                #e diferente da saida ou entrada
            if(lst_nodos[i].direita != None):
                lst_nodos[i].direita = lst_nodos[i+1]

        #Se inferior não tiver parede recebe o nodo abaixo ou None
        if lst_nodos[i].inferior == '1':
            #file.write(svgline(i, i%int(nm)+1, i+1, i%int(nm)+1))
            lst_nodos[i].inferior = None
        else:
                #e diferente da saida ou entrada
            if(lst_nodos[i].inferior != None):
                lst_nodos[i].inferior = lst_nodos[i+int(nm)]

        if lst_nodos[i].entrada == True:
            print("entrada")
        if lst_nodos[i].saida == True:
            print("saida")



























def labirinto(list):
    node_entrada = None
    node_saida = None
    global lst_nodos
    for l in range(len(list)):
        c = 0
        for elem in list[l]:
            nodo = Node(elem[0],elem[1],elem[2],elem[3])
            #print(nodo)
            if elem[0] == '1':
                file.write(svgline(c, l , c + 1, l))
            if elem[1] == '1':
                file.write(svgline(c+1, l , c+1, l+1))
            if elem[2] == '1':
                file.write(svgline(c , l+1 , c +1 , l + 1))
            if elem[3] == '1':
                file.write(svgline(c, l , c, l + 1))

            lst_nodos.append(nodo)
            #Achar entrada e saida do labirinto <-- recebe None e seta o booleano do construtor
            if l == 0:
                #Vazio para todos nodos na primeira linha
                if nodo.superior == '0':
                    if node_entrada == None:
                        nodo.entrada = True
                        node_entrada = nodo
                    elif node_saida == None:
                        nodo.saida = True
                        node_saida = nodo
                nodo.superior = None

            if l == len(list)-1:
                #Vazio para todos nodos na ultima linha
                if nodo.inferior == '0':
                    if node_entrada == None:
                        nodo.entrada = True
                        node_entrada = nodo
                    elif node_saida == None:
                        nodo.saida = True
                        node_saida = nodo
                nodo.inferior = None

            if nodo.esquerda == '0' and c == 1:
                #Vazio para todos na coluna da esquerda
                if node_entrada == None:
                    nodo.entrada = True
                    node_entrada = nodo
                elif node_saida == None:
                    nodo.saida = True
                    node_saida = nodo
                nodo.esquerda = None

            if nodo.direita == '0' and c == len(list)-1:
                #Vazio para todos na coluna da direita
                if node_entrada == None:
                    nodo.entrada = True
                    node_entrada = nodo
                elif node_saida == None:
                    nodo.saida = True
                    node_saida = nodo
                nodo.direita = None

            if(nodo.entrada == True):
                print(list[l][c])
            if(nodo.saida == True):
                print(list[l][c])

            c = c + 1

    #print(lst_nodos)
    #print(list)
    #print(node_entrada)
    #print(node_saida)
    lista_adjacencia(lst_nodos)
    print(caminha(node_entrada))
