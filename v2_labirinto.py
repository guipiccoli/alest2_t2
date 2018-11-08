import conversion as cvs
#1010
#0 -Superior: Parede
#1 - Direita: Sem parede
#2 -Inferior: Parede
#3 -Esquerda: Sem parede

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.flag = 0
        self.entrada = False
        self.saida = False
    def __repr__(self):
     return str(self.__dict__)

file = open("draw_lab.svg", "w")

def svgline(x1,y1,x2,y2 ):
     return "<polyline points='{}, {} {}, {}'/>".format(x1, y1, x2, y2)

def svgCircle(x,y):
     return "<circle cx='{}' cy='{}' r='0.1' stroke='red' fill='red' />".format(x+0.5,y+0.5)

def entrada_saida(list):
    node_entrada = None
    node_saida = None
    for l in range(len(list)):
        c = 0
        for elem in list[l]:
            if elem[0] == '1':
                file.write(svgline(c, l , c + 1, l))
            if elem[1] == '1':
                file.write(svgline(c+1, l , c+1, l+1))
            if elem[2] == '1':
                file.write(svgline(c , l+1 , c +1 , l + 1))
            if elem[3] == '1':
                file.write(svgline(c, l , c, l + 1))

            node = Node(elem)
            list[l][c] = node
            #linha 0
            if l == 0:
                if elem[0] == '0':
                    if node_entrada == None:
                        node.entrada = True
                        node_entrada = node
                        linha, coluna = l,c
                    else:
                        node.saida = True
                        node_saida = node

            #coluna 0 e não linha 0 ou ultima linha
            if c == 0 and l > 0 and l != len(list)-1:
                if elem[3] == '0':
                    if node_entrada == None:
                        node.entrada = True
                        node_entrada = node
                        linha, coluna = l,c
                    else:
                        node.saida = True
                        node_saida = node

            #ultima coluna e não linha 0 ou ultima linha
            if c == len(list)-1 and l > 0 and l != len(list)-1:
                if elem[1] == '0':
                    if node_entrada == None:
                        node.entrada = True
                        node_entrada = node
                        linha, coluna = l,c
                    else:
                        node.saida = True
                        node_saida = node

            #ultima linha
            if l == len(list)-1:
                if elem[2] == '0':
                    if node_entrada == None:
                        node.entrada = True
                        node_entrada = node
                        linha, coluna = l,c
                    else:
                        node.saida = True
                        node_saida = node

            c = c + 1

    #print(lst_nodes)
    print(labirinto(list, linha, coluna))

res = 0
def labirinto(list, linha, coluna):
    global res
    node = list[linha][coluna]
    if node.saida == True :
        file.write(svgCircle(coluna,linha))
        return 1

    if node.flag == 1 or node.flag == 2:
        return 0

    node.flag = 1

    if(node.elem[0] == '0'):
        if linha!=0:
            res = labirinto(list, linha-1, coluna)
            if res >= 1:
                file.write(svgCircle(coluna,linha))
                return res + 1
    if(node.elem[1] == '0'):
        if coluna!=len(list)-1:
            res = labirinto(list, linha, coluna+1)
            if res >= 1:
                file.write(svgCircle(coluna,linha))
                return res + 1
    if(node.elem[2] == '0'):
        if linha!=len(list)-1:
            res = labirinto(list, linha+1, coluna)
            if res >= 1:
                file.write(svgCircle(coluna,linha))
                return res + 1
    if(node.elem[3] == '0'):
        if coluna!=0:
            res = labirinto(list, linha, coluna-1)
            if res >= 1:
                file.write(svgCircle(coluna,linha))
                return res + 1

    node.flag = 2
    return 0




nm = 0
def main ():
    f = open('t2-casos/teste.txt', 'r')
    global nm
    data = f.readlines()
    elem = []
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
    #print(binary_string)
    file.write("<?xml version='1.0' standalone='no'?>");
    file.write("<svg xmlns='http://www.w3.org/2000/svg' width='{}cm' height='{}cm' viewBox='-0.1 -0.1 {} {}'>".format(int(nm), int(nm), int(nm)+0.2, int(nm)+0.2));
    file.write ("<g style='stroke-width:.1; stroke:black; stroke-linejoin:miter; stroke-linecap:butt;'>");

    entrada_saida(binary_string)

    file.write( "</g>" )
    file.write( "</svg>" )
    file.close()

    #print(caminhamento)
if __name__ == "__main__": main()
