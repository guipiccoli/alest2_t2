import conversion as cvs
#1010
#Superior: Parede
#Direita: Sem parede
#Inferior: Parede
#Esquerda: Sem parede
class Node:
    def __init__(self,superior,direita,inferior,esquerda):
        self.superior = superior
        self.direita = direita
        self.inferior = inferior
        self.esquerda = esquerda
        self.flag = 0
        self.entrada = False
        self.saida = False
    def __repr__(self):
     return str(self.__dict__)


lst_nodos = []

node_entrada = None
node_saida = None

def labirinto(list):
    global node_entrada
    global node_saida
    global lst_nodos
    for i in range(len(list)):
        for elem in list[i]:
            nodo = Node(elem[0],elem[1],elem[2],elem[3])
            lst_nodos.append(nodo)
            #Achar entrada e saida do labirinto <-- recebe None e seta o booleano do construtor
            if i == 0:
                #Vazio para todos nodos na primeira linha
                if nodo.superior == '0':
                    #nodo.entrada = True
                    node_entrada = nodo
                nodo.superior = None

            elif i == len(list)-1:
                #Vazio para todos nodos na ultima linha
                if nodo.inferior == '0':
                    #nodo.saida = True
                    node_saida = nodo
                nodo.inferior = None

            elif nodo.esquerda == '0' and list[0]:
                #Vazio para todos na coluna da esquerda
                nodo.esquerda = None
                if node_entrada == None:
                    #nodo.entrada = True
                    node_entrada = nodo
                else:
                    #nodo.saida = True
                    node_saida = nodo

            elif nodo.direita == '0' and list[len(list)-1]:
                #Vazio para todos na coluna da direita
                nodo.direita = None
                if node_entrada == None:
                    #nodo.entrada = True
                    node_entrada = nodo
                else:
                    #nodo.saida = True
                    node_saida = nodo
            

    #print(lst_nodos)
    #print(list)
    #print(node_entrada)
    #print(node_saida)
    lista_adjacencia(lst_nodos)
    print(caminha(node_saida, node_entrada))


def lista_adjacencia(lst_nodos):
    global node_saida
    global node_entrada
    for i in range(len(lst_nodos)):
        #Se superior não tiver parede recebe o nodo acima ou None
        if lst_nodos[i].superior == '1':
            lst_nodos[i].superior = None
        else:
            if(lst_nodos[i].superior != None):
                lst_nodos[i].superior = lst_nodos[i-int(nm)]

        #Se esquerda não tiver parede recebe o nodo a esquerda ou None
        if lst_nodos[i].esquerda == '1':
            lst_nodos[i].esquerda = None
        else:
            lst_nodos[i].esquerda = lst_nodos[i-1]

        #Se direita não tiver parede recebe o nodo a direita ou None
        if lst_nodos[i].direita == '1':
            lst_nodos[i].direita = None
        else:
            if(lst_nodos[i].direita != None):
                lst_nodos[i].direita = lst_nodos[i+1]

        #Se inferior não tiver parede recebe o nodo abaixo ou None
        if lst_nodos[i].inferior == '1':
            lst_nodos[i].inferior = None
        else:
            if(lst_nodos[i].inferior != None):
                lst_nodos[i].inferior = lst_nodos[i+int(nm)]

caminhamento = []
res = 0
def caminha(node, saida):
    global res

    caminhamento.append(node)
    if node == saida:
        print("cheguei")
        return res +1
    node.flag = 1

    if node.superior != None and node.superior.flag == 0:
        res = caminha(node.superior, saida)
        if res > 0:
            print("cima")
            return 1 + res
    if node.direita != None and node.direita.flag == 0:
        res = caminha(node.direita, saida)
        if res > 0:
            print("direita")
            return 1 + res
    if node.inferior != None and node.inferior.flag == 0:
        res = caminha(node.inferior, saida)
        if res > 0:
            print("desce")
            return 1 + res
    if node.esquerda != None and node.esquerda.flag == 0:
        res = caminha(node.esquerda, saida)
        if res > 0:
            print("esquerda")
            return 1 + res

    node.flag = 2
    return res

nm = 0
def main ():
    f = open('t2-casos/teste.txt', 'r')
    data = f.readlines()
    elem = []
    global nm
    elementos = []
    binary_string =[]
    nm = data[0].split(' ')[0]
    for i in range (1,(int(nm)+1)):
        data[i] = data[i].strip('\n')
        elem.append(data[i].split(' '))
        elementos.append(elem[i-1])
        binary_string.append(list(map(lambda x:cvs.hex2bin(x),elem[i-1])))
    labirinto(binary_string)

    #print(caminhamento)
if __name__ == "__main__": main()
