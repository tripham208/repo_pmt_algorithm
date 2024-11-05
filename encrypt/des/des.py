iP = [
    [58, 50, 42, 34, 26, 18, 10, 2],
    [60, 52, 44, 36, 28, 20, 12, 4],
    [62, 54, 46, 38, 30, 22, 14, 6],
    [64, 56, 48, 40, 32, 24, 16, 8],
    [57, 49, 41, 33, 25, 17, 9, 1],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [61, 53, 45, 37, 29, 21, 13, 5],
    [63, 55, 47, 39, 31, 23, 15, 7],
]
E = [
    [32, 1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8, 9],
    [8, 9, 10, 11, 12, 13],
    [12, 13, 14, 15, 16, 17],
    [16, 17, 18, 19, 20, 21],
    [20, 21, 22, 23, 24, 25],
    [24, 25, 26, 27, 28, 29],
    [28, 29, 30, 31, 32, 1],
]
P = [
    [16, 7, 20, 21, 29, 12, 28, 17],
    [1, 15, 23, 26, 5, 18, 31, 10],
    [2, 8, 24, 14, 32, 27, 3, 9],
    [19, 13, 30, 6, 22, 11, 4, 25],
]
iP_1 = [
    [40, 8, 48, 16, 56, 24, 64, 32],
    [39, 7, 47, 15, 55, 23, 63, 31],
    [38, 6, 46, 14, 54, 22, 62, 30],
    [37, 5, 45, 13, 53, 21, 61, 29],
    [36, 4, 44, 12, 52, 20, 60, 28],
    [35, 3, 43, 11, 51, 19, 59, 27],
    [34, 2, 42, 10, 50, 18, 58, 26],
    [33, 1, 41, 9, 49, 17, 57, 25],
]
pC1 = [
    [57, 49, 41, 33, 25, 17, 9, 1],
    [58, 50, 42, 34, 26, 18, 10, 2],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [60, 52, 44, 36, 63, 55, 47, 39],
    [31, 23, 15, 7, 62, 54, 46, 38],
    [30, 22, 14, 6, 61, 53, 45, 37],
    [29, 21, 13, 5, 28, 20, 12, 4],
]
pC2 = [
    [14, 17, 11, 24, 1, 5, 3, 28],
    [15, 6, 21, 10, 23, 19, 12, 4],
    [26, 8, 16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55, 30, 40],
    [51, 45, 33, 48, 44, 49, 39, 56],
    [34, 53, 46, 42, 50, 36, 29, 32],
]
s1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
]
s2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
]
s3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
]
s4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
]
s5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
]
s6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
]
s7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
]
s8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
d = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def hex2bin(plain):
    """
    :param plain: chuỗi hex đầu vào
    :return: chuỗi nhị phân
    """
    output = ""
    switcher = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    for i in plain:
        output += switcher.get(i)
    return output


def bin2hex(plainText_bin):
    """
    :param plainText_bin: chuỗi nhị phân đầu vào
    :return: chuỗi hex
    """
    output = ""
    switcher = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    for i in range(0, len(plainText_bin), 4):
        # print(i, char2bin(i), sep="\t")
        txt = plainText_bin[i]
        txt += plainText_bin[i + 1]
        txt += plainText_bin[i + 2]
        txt += plainText_bin[i + 3]
        # plainText_bin += hex2bin(i)
        output += switcher.get(txt)
    return output


def initial_p(p64, iP):
    output = ""
    for i in iP:
        for j in i:
            output += p64[j - 1]
    # print(output)
    # print(len(output))
    return output


def inverse_ip(p64, iP_1):
    output = ""
    for i in iP_1:
        for j in i:
            # print(j,end=" ")
            output += p64[j - 1]
    # print(output)
    # print(len(output))
    return output


def p_table(p32, P):
    output = ""
    for i in P:
        for j in i:
            # print(j)
            output += p32[j - 1]
    # print(len(plain48))
    # print(plain48)
    # print(len(output))
    return output


def xor32(l32, r32):
    """
    xor 32 bit
    :param l32:
    :param r32:
    :return: chuỗi xor
    """
    output = ""

    # print(l32)
    # print(r32)

    for i in range(0, 32):
        o = ord(l32[i]) ^ ord(r32[i])
        output += str(o)
        # output+=ord(l32[i])^ord(r32[i])+''
    # print(output)
    return output


def xor48(l48, r48):
    """
    xor 48 bit
    :param l48:
    :param r48:
    :return: chuỗi xor
    """
    output = ""

    for i in range(0, 48):
        o = ord(l48[i]) ^ ord(r48[i])
        output += str(o)
    return output


def key_choice1(k64, pC1):
    """
    chọn hoán vị 1

    :param k64: key 64 bit
    :param pC1: bảng chọn hoán vị 1 / bỏ bội của 8
    :return: key 56 bit
    """
    k56 = ""

    for i in pC1:
        for j in i:
            k56 += k64[j - 1]

    """
    for i in range(0,63):
        if ((i+1)%8)==0:
            continue
        else:
            output+=k64[i]
    """
    return k56


def key_choice2(k56, pC2):
    """
    :key 56 bit -> 48bit
    :param k56: key 56 bit
    :param pC2: bang hoán vị chọn 2
    :return: key 48 bit
    """
    k48 = ""
    for i in pC2:
        for j in i:
            k48 += k56[j - 1]
    return k48


def s_box(i6, box):
    o4 = ""
    # print(i6)
    hang = i6[0] + i6[5]
    cot = i6[1:5]
    # print(hang ," ", cot)
    hang = int(hang, 2)
    cot = int(cot, 2)
    # print(hang, " ", cot)
    # print(box[hang][cot])
    switcher = {
        0: "0000",
        1: "0001",
        2: "0010",
        3: "0011",
        4: "0100",
        5: "0101",
        6: "0110",
        7: "0111",
        8: "1000",
        9: "1001",
        10: "1010",
        11: "1011",
        12: "1100",
        13: "1101",
        14: "1110",
        15: "1111",
    }
    # print(switcher.get(box[hang][cot]))
    o4 = switcher.get(box[hang][cot])
    return o4


def left_shift(k28, shift):
    output = ""
    for i in range(shift, len(k28)):
        output += k28[i]
    output += k28[0:shift]
    return output


def e_table(plain32, E):
    # print(len(plain32))
    plain48 = ""
    for i in E:
        for j in i:
            plain48 += plain32[j - 1]
    # print(len(plain48))
    # print(plain48)
    return plain48


def des(plain, key):
    print("đầu vào:")
    print("M =", plain)
    plainText_bin = hex2bin(plain)
    print("M-bin ", len(plainText_bin), "= ", plainText_bin)
    print("K =", key)
    key_bin = hex2bin(key)
    print("K-bin ", len(key_bin), "= ", key_bin)
    # tiền xử lý
    print("\ntiền mã hóa:")
    plainText_bin = initial_p(plainText_bin, iP)
    print("M-bin-IP ", len(plainText_bin), ": ", plainText_bin)
    key56 = key_choice1(key_bin, pC1)
    print("K56-PC1 ", len(key56), ":", key56)

    # print(plainText_bin)
    l32 = plainText_bin[0:32]
    # print(len(l32))
    # print(l32)
    print("L-0 ", len(l32), ": ", l32)
    r32 = plainText_bin[32:64]
    # print(len(r32))
    # print(r32)
    # print(key56)
    print("R-0 ", len(r32), ": ", r32)
    c28 = key56[0:28]
    # print(len(c28))
    # print(c28)
    print("C-0 ", len(c28), ": ", c28)
    d28 = key56[28:56]
    # print(len(d28))
    # print(d28)

    # mã hóa
    print("D-0 ", len(d28), ": ", d28)
    for round in range(1, 17):
        print("\nvòng ", round, ":")
        c28 = left_shift(c28, d[round - 1])
        d28 = left_shift(d28, d[round - 1])
        print("dịch ", d[round - 1])
        print("C-", round, " ", len(c28), ": ", c28)
        print("D-", round, " ", len(d28), ": ", d28)

        key56 = c28 + d28
        key48 = key_choice2(key56, pC2)

        print("K56-", round, len(key56), ": ", key56)
        print("K48-", round, len(key48), ": ", key48)

        l32next = r32
        r48 = e_table(r32, E)
        print("E[R]        :", r48)

        r48 = xor48(r48, key48)
        print("XOR  R-K", round, ":", r48)
        r32 = (
            s_box(r48[0:6], s1)
            + s_box(r48[6:12], s2)
            + s_box(r48[12:18], s3)
            + s_box(r48[18:24], s4)
            + s_box(r48[24:30], s5)
            + s_box(r48[30:36], s6)
            + s_box(r48[36:42], s7)
            + s_box(r48[42:48], s8)
        )
        print("Sbox   ", len(r32), ": ", r32)
        r32 = p_table(r32, P)
        print("Ptable ", len(r32), ": ", r32)
        r32 = xor32(l32, r32)
        print("L-1    ", len(l32), ": ", l32)
        print("XOR L-R", len(r32), ": ", r32)
        l32 = l32next

        print("L-", round, len(l32), ": ", l32)
        print("R-", round, len(r32), ": ", r32)

    cipher = r32 + l32
    print("\ncp-bin    :", cipher)
    cipher = inverse_ip(cipher, iP_1)
    print("cp-bin-iv :", cipher)
    cipher = bin2hex(cipher)
    return cipher


if __name__ == "__main__":
    key = "E35CB18E63EEED18"
    plainText = "B71127D233E316C3"

    cipher = des(plainText, key)
    print("\ncipher :", cipher)
