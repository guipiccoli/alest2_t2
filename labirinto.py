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

entrada = None
saida = None

def labirinto(list):
    global entrada
    global saida
    for i in range(len(list)):
        for elem in list[i]:
            if i == 0:
                Node(elem[0],elem[1],elem[2],elem[3])
                if elem[0] == '0':
                    entrada = elem

            elif i == len(list)-1:
                for elem in list[i]:
                    if elem[2] == '0':
                        saida = elem

            elif elem[3] == '0' and list[0] or (list[len(list)-1] and elem[1] == '0'):
                if entrada == None:
                    entrada = elem
                else:
                    saida = elem
    print(entrada)
    print(saida)

def caminha(node):
    if node == entrada2:
        return 1
    node.flag = 1

    if node.cima != '1' and node.cima.flag == 0:
        res = caminha(node.cima)
        if res > 0:
            return 1 + res
    if node.direita != '1' and node.direita.flag == 0:
        res = caminha(node.direita)
        if res > 0:
            return 1 + res
    if node.baixo != '1' and node.baixo.flag == 0:
        res = caminha(node.baixo)
        if res > 0:
            return 1 + res
    if node.esquerda != '1' and node.esquerda.flag == 0:
        res = caminha(node.esquerda)
        if res > 0:
            return 1 + res

    node.flag = 2
    return 0

def main ():
    f = open('t2-casos/teste.txt', 'r')
    data = f.readlines()
    elem = []
    elementos = []
    binary_string =[]
    nm = data[0].split(' ')[0]
    for i in range (1,(int(nm)+1)):
        data[i] = data[i].strip('\n')
        elem.append(data[i].split(' '))
        elementos.append(elem[i-1])
        binary_string.append(list(map(lambda x:cvs.hex2bin(x),elem[i-1])))
    labirinto(binary_string)
if __name__ == "__main__": main()
