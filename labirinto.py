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
        self.entrada = None
        self.saida = None
    def __repr__(self):
     return str(self.__dict__)

file = open("draw_lab.svg", "w")

def svgline(x1,y1,x2,y2 ):
     return "<polyline points='{}, {} {}, {}'/>".format(x1, y1, x2, y2)

def svgCircle(x,y):
     return "<circle cx='{}' cy='{}' r='0.1' stroke='red' fill='red' />".format(x,y)


lst_nodos = []
# node_entrada = None
# node_saida = None

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
                        nodo.entrada = 'N'
                        node_entrada = nodo
                    elif node_saida == None:
                        nodo.saida = 'N'
                        node_saida = nodo

            elif l == len(list)-1:
                #Vazio para todos nodos na ultima linha
                if nodo.inferior == '0':
                    if node_entrada == None:
                        nodo.entrada = 'S'
                        node_entrada = nodo
                    elif node_saida == None:
                        nodo.saida = 'S'
                        node_saida = nodo

            elif nodo.esquerda == '0' and c == 1:
                #Vazio para todos na coluna da esquerda
                if node_entrada == None:
                    nodo.entrada = "O"
                    node_entrada = nodo
                elif node_saida == None:
                    nodo.saida = "O"
                    node_saida = nodo


            if nodo.direita == '0' and c == len(list)-1:
                #Vazio para todos na coluna da direita
                if node_entrada == None:
                    nodo.entrada = "L"
                    node_entrada = nodo
                elif node_saida == None:
                    nodo.saida = "L"
                    node_saida = nodo
                nodo.direita = None

            if(nodo.entrada != None):
                print("Entrada: ", list[l][c], nodo.entrada)
            if(nodo.saida != None):
                print("Saida: ", list[l][c], nodo.saida)

            c = c + 1

    #print(lst_nodos)
    #print(list)
    #print(node_entrada)
    #print(node_saida)
    lista_adjacencia(lst_nodos)
    print(caminha(node_entrada))


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

        if lst_nodos[i].entrada == True:
            print("entrada")
        if lst_nodos[i].saida == True:
            print("saida")


caminhamento = []
res = 0
def caminha(node):
    global res

    if node.saida != None :
        print("cheguei")
        return res +1

    node.flag = 1

    if node.superior == 0 and node.superior.flag == 0:
        res = caminha(node.superior)
        if res > 0:
            print("cima")
            return 1 + res
    if node.direita == 0 and node.direita.flag == 0:
        res = caminha(node.direita)
        if res > 0:
            print("direita")
            return 1 + res
    if node.inferior == 0 and node.inferior.flag == 0:
        res = caminha(node.inferior)
        if res > 0:
            print("desce")
            return 1 + res
    if node.esquerda == 0 and node.esquerda.flag == 0:
        res = caminha(node.esquerda)
        if res > 0:
            print("esquerda")
            return 1 + res

    node.flag = 2
    return res

nm = 0
def main ():
    f = open('t2-casos/caso25a.txt', 'r')
    data = f.readlines()
    elem = []
    global nm
    elementos = []
    binary_string =[]
    nm = data[0].split(' ')[0]
    for i in range (1,(int(nm)+1)):
        data[i] = data[i].strip('\n').split(' ')
        if '' in data[i]:
            data[i].remove('')
        elem.append(data[i])
        elementos.append(elem[i-1])
        binary_string.append(list(map(lambda x:cvs.hex2bin(x),elem[i-1])))

    #print(elementos[:-1])
    print(binary_string)
    file.write("<?xml version='1.0' standalone='no'?>");
    file.write("<svg xmlns='http://www.w3.org/2000/svg' width='{}cm' height='{}cm' viewBox='-0.1 -0.1 {} {}'>".format(int(nm), int(nm), int(nm)+0.2, int(nm)+0.2));
    file.write ("<g style='stroke-width:.1; stroke:black; stroke-linejoin:miter; stroke-linecap:butt;'>");

    labirinto(binary_string)

    file.write( "</g>" )
    file.write( "</svg>" )
    file.close()

    #print(caminhamento)
if __name__ == "__main__": main()
