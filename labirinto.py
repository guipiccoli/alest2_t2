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

file = open("draw_lab.svg", "w")

def svgline(x1,y1,x2,y2 ):
     return "<polyline points='{}, {} {}, {}'/>".format(x1, y1, x2, y2);

lst_nodos = []
node_entrada = None
node_saida = None

def labirinto(list):
    global node_entrada
    global node_saida
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

            c = c + 1
            lst_nodos.append(nodo)
            #Achar entrada e saida do labirinto <-- recebe None e seta o booleano do construtor
            if l == 0:
                #Vazio para todos nodos na primeira linha
                if nodo.superior == '0':
                    #nodo.entrada = True
                    node_entrada = nodo
                nodo.superior = None

            elif l == len(list)-1:
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
            #print("cima")
            return 1 + res
    if node.direita != None and node.direita.flag == 0:
        res = caminha(node.direita, saida)
        if res > 0:
            #print("direita")
            return 1 + res
    if node.inferior != None and node.inferior.flag == 0:
        res = caminha(node.inferior, saida)
        if res > 0:
            #print("desce")
            return 1 + res
    if node.esquerda != None and node.esquerda.flag == 0:
        res = caminha(node.esquerda, saida)
        if res > 0:
            #print("esquerda")
            return 1 + res

    node.flag = 2
    return res

nm = 0
def main ():
    f = open('t2-casos/caso50a.txt', 'r')
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

    file.write("<?xml version='1.0' standalone='no'?>");
    file.write("<svg xmlns='http://www.w3.org/2000/svg' width='{}cm' height='{}cm' viewBox='-0.1 -0.1 {} {}'>".format(int(nm), int(nm), int(nm)+0.2, int(nm)+0.2));
    file.write ("<g style='stroke-width:.1; stroke:black; stroke-linejoin:miter; stroke-linecap:butt;'>");

    labirinto(binary_string)

    #file.write("<circle cx='11.5' cy='0.5' r='0.2' stroke='red' fill='red' />")
    file.write( "</g>" )
    file.write( "</svg>" )
    file.close()

    #print(caminhamento)
if __name__ == "__main__": main()
