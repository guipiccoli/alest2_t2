import conversion as cvs
#1010
#Superior: Parede
#Direita: Sem parede
#Inferior: Parede
#Esquerda: Sem parede

def labirinto(list):
    for i in range(len(list)):
        if i == 0:
            for elem in list[i]:
                if elem.find('0') == 0:
                    print(elem)
                    
        if i == len(list)-1:
            for elem in list[i]:
                if elem.find('0') == 2:
                    print(elem)

def main ():
    f = open('t2-casos/caso500a.txt', 'r')
    data = f.readlines()
    elem = []
    elementos = []
    binary_string =[]
    nm = data[0].split(' ')[0]
    for i in range (1,(int(nm)+1)):
        elem.append(data[i].split(' '))
        binary_string.append(list(map(lambda x:cvs.hex2bin(x),elem[i-1][:-1])))
    labirinto(binary_string)
if __name__ == "__main__": main()
