def hex2bin(hex):
    if hex == '0':
        return '0000'
    elif hex == '1':
        return '0001'
    elif hex == '2':
        return '0010'
    elif hex == '3':
        return '0011'
    elif hex == '4':
        return '0100'
    elif hex == '5':
        return '0101'
    elif hex == '6':
        return '0110'
    elif hex == '7':
        return '0111'
    elif hex == '8':
        return '1000'
    elif hex == '9':
        return '1001'
    elif hex == 'A' or hex == 'a' :
        return '1010'
    elif hex == 'B' or hex == 'b' :
        return '1011'
    elif hex == 'C' or hex == 'c' :
        return '1100'
    elif hex == 'D' or hex == 'd' :
        return '1101'
    elif hex == 'E' or hex == 'e' :
        return '1110'
    elif hex == 'F' or hex == 'f'  :
        return '1111'
    else:
        return 'erro'
