def labirinto(list):
    global node_entrada
    global node_saida
    global lst_nodos
    cont = 0
    for i in range(len(list)):
        for elem in list[i]:
            nodo = Node(elem[0],elem[1],elem[2],elem[3])
            lst_nodos.append(nodo)
            #Achar entrada e saida do labirinto <-- recebe None e seta o booleano do construtor
            if i == 0:
                #Vazio para todos nodos na primeira linha
                if nodo.superior == '0':
                    if node_entrada == None:
                        nodo.entrada = True
                        node_entrada = nodo
                    elif node_saida == None:
                        nodo.saida = True
                        node_saida = nodo

            elif i == len(list)-1:
                #Vazio para todos nodos na ultima linha
                if nodo.inferior == '0':
                    if node_entrada == None:
                        nodo.entrada = True
                        node_entrada = nodo
                    elif node_saida == None:
                        nodo.saida = True
                        node_saida = nodo

            elif nodo.esquerda == '0' and list[0]:
                #Vazio para todos na coluna da esquerda
                if node_entrada == None:
                    if node_entrada == None:
                        nodo.entrada = True
                        node_entrada = nodo
                    elif node_saida == None:
                        nodo.saida = True
                        node_saida = nodo

            elif nodo.direita == '0' and list[len(list)-1]:
                #Vazio para todos na coluna da direita
                    if node_entrada == None:
                        nodo.entrada = True
                        node_entrada = nodo
                    elif node_saida == None:
                        nodo.saida = True
                        node_saida = nodo
            if(nodo.entrada == True):
                print(nodo)
            if(nodo.saida == True):
                print(nodo)
                cont = cont + 1
            
    print(cont)
    #print(lst_nodos)
    #print(list)
    #print(node_entrada)
    #print(node_saida)
    lista_adjacencia(lst_nodos)
    print(caminha(node_entrada, node_saida))
