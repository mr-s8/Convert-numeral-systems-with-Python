def bi_to_dec(bi):
    num = 0
    exp = 0
    for i in str(bi)[::-1]:
        num += int(i)*(2**exp)
        exp += 1
    return num


def dec_to_bi(dec):
    num = ""
    res = int(dec)
    l = []
    while res > 0:
        l.append(res % 2)
        res = res // 2
    for i in l[::-1]:
        num += str(i)
    return int(num)


def hex_to_dec(hex):
    num = 0
    exp = 0
    n = 10
    for i in str(hex)[::-1]:
        try:
            i = int(i)
        except:
            pass
        if type(i) == str:
            if i == "A":
                n = 10
            elif i == "B":
                n = 11
            elif i == "C":
                n = 12
            elif i == "D":
                n = 13
            elif i == "E":
                n = 14
            elif i == "F":
                n = 15
        else:
            n = i
        num += int(n)*(16**exp)
        exp += 1
    return int(num)


def dec_to_hex(dec):
    num = ""
    res = int(dec)
    l = []
    while res > 0:
        l.append(res % 16)
        res = res // 16
    for i in l[::-1]:
        if i < 10:
            num += str(i)
        elif i == 10:
            num += "A"
        elif i == 11:
            num += "B"
        elif i == 12:
            num += "C"
        elif i == 13:
            num += "D"
        elif i == 14:
            num += "E"
        elif i == 15:
            num += "F"
    return num


def hex_to_bi(hex):
    dec = hex_to_dec(hex)
    bi = dec_to_bi(dec)
    return bi


def bi_to_hex(bi):
    dec = bi_to_dec(bi)
    hex = dec_to_hex(dec)
    return hex


print(bi_to_dec(10111011))
print(dec_to_bi(42))
print(hex_to_dec("5AF3"))
print(dec_to_hex(23283))
print(bi_to_dec(hex_to_bi("5AF3")))
print(hex_to_dec(bi_to_hex(10111011)))

# might have made mistakes
