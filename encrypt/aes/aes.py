import numpy as np

sBox = [
    [
        0x63,
        0x7C,
        0x77,
        0x7B,
        0xF2,
        0x6B,
        0x6F,
        0xC5,
        0x30,
        0x01,
        0x67,
        0x2B,
        0xFE,
        0xD7,
        0xAB,
        0x76,
    ],
    [
        0xCA,
        0x82,
        0xC9,
        0x7D,
        0xFA,
        0x59,
        0x47,
        0xF0,
        0xAD,
        0xD4,
        0xA2,
        0xAF,
        0x9C,
        0xA4,
        0x72,
        0xC0,
    ],
    [
        0xB7,
        0xFD,
        0x93,
        0x26,
        0x36,
        0x3F,
        0xF7,
        0xCC,
        0x34,
        0xA5,
        0xE5,
        0xF1,
        0x71,
        0xD8,
        0x31,
        0x15,
    ],
    [
        0x04,
        0xC7,
        0x23,
        0xC3,
        0x18,
        0x96,
        0x05,
        0x9A,
        0x07,
        0x12,
        0x80,
        0xE2,
        0xEB,
        0x27,
        0xB2,
        0x75,
    ],
    [
        0x09,
        0x83,
        0x2C,
        0x1A,
        0x1B,
        0x6E,
        0x5A,
        0xA0,
        0x52,
        0x3B,
        0xD6,
        0xB3,
        0x29,
        0xE3,
        0x2F,
        0x84,
    ],
    [
        0x53,
        0xD1,
        0x00,
        0xED,
        0x20,
        0xFC,
        0xB1,
        0x5B,
        0x6A,
        0xCB,
        0xBE,
        0x39,
        0x4A,
        0x4C,
        0x58,
        0xCF,
    ],
    [
        0xD0,
        0xEF,
        0xAA,
        0xFB,
        0x43,
        0x4D,
        0x33,
        0x85,
        0x45,
        0xF9,
        0x02,
        0x7F,
        0x50,
        0x3C,
        0x9F,
        0xA8,
    ],
    [
        0x51,
        0xA3,
        0x40,
        0x8F,
        0x92,
        0x9D,
        0x38,
        0xF5,
        0xBC,
        0xB6,
        0xDA,
        0x21,
        0x10,
        0xFF,
        0xF3,
        0xD2,
    ],
    [
        0xCD,
        0x0C,
        0x13,
        0xEC,
        0x5F,
        0x97,
        0x44,
        0x17,
        0xC4,
        0xA7,
        0x7E,
        0x3D,
        0x64,
        0x5D,
        0x19,
        0x73,
    ],
    [
        0x60,
        0x81,
        0x4F,
        0xDC,
        0x22,
        0x2A,
        0x90,
        0x88,
        0x46,
        0xEE,
        0xB8,
        0x14,
        0xDE,
        0x5E,
        0x0B,
        0xDB,
    ],
    [
        0xE0,
        0x32,
        0x3A,
        0x0A,
        0x49,
        0x06,
        0x24,
        0x5C,
        0xC2,
        0xD3,
        0xAC,
        0x62,
        0x91,
        0x95,
        0xE4,
        0x79,
    ],
    [
        0xE7,
        0xC8,
        0x37,
        0x6D,
        0x8D,
        0xD5,
        0x4E,
        0xA9,
        0x6C,
        0x56,
        0xF4,
        0xEA,
        0x65,
        0x7A,
        0xAE,
        0x08,
    ],
    [
        0xBA,
        0x78,
        0x25,
        0x2E,
        0x1C,
        0xA6,
        0xB4,
        0xC6,
        0xE8,
        0xDD,
        0x74,
        0x1F,
        0x4B,
        0xBD,
        0x8B,
        0x8A,
    ],
    [
        0x70,
        0x3E,
        0xB5,
        0x66,
        0x48,
        0x03,
        0xF6,
        0x0E,
        0x61,
        0x35,
        0x57,
        0xB9,
        0x86,
        0xC1,
        0x1D,
        0x9E,
    ],
    [
        0xE1,
        0xF8,
        0x98,
        0x11,
        0x69,
        0xD9,
        0x8E,
        0x94,
        0x9B,
        0x1E,
        0x87,
        0xE9,
        0xCE,
        0x55,
        0x28,
        0xDF,
    ],
    [
        0x8C,
        0xA1,
        0x89,
        0x0D,
        0xBF,
        0xE6,
        0x42,
        0x68,
        0x41,
        0x99,
        0x2D,
        0x0F,
        0xB0,
        0x54,
        0xBB,
        0x16,
    ],
]
mix = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]
rc = [0, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]


# hàm phụ
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


def hex2int(x):
    """
    :param x: chuỗi hex đầu vào
    :return: chuỗi int
    """
    switcher = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    return switcher.get(x)


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


def str2matrix(plain):
    plain_matrix = np.array([[0] * 4] * 4, dtype=int)
    k = 0

    for i in range(4):
        for j in range(4):
            plain_matrix[i][j] = int(plain[k : k + 2], 16)
            k += 2
    return plain_matrix


def show_Matrix_Int2Hex(x):
    out = np.array([["        "] * 4] * 4, dtype=str)
    for i in range(4):
        for j in range(4):
            out[i][j] = bin(x[i][j])[2:10].zfill(8)
            out[i][j] = bin2hex(out[i][j])
    print(out)


def xor8(l8, r8):
    """
    xor 8 bit
    :param l8:
    :param r8:
    :return: chuỗi xor
    """
    output = ""
    for i in range(0, 8):
        o = ord(l8[i]) ^ ord(r8[i])
        output += str(o)
    return output


def leftShift(x):
    """
    dịch trái 1 bit
    :param x:
    :return:
    """
    output = ""
    for i in range(1, len(x)):
        output += x[i]
    output += "0"
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


def w4_matrix_int(w, i):
    out = np.array([[0] * 4] * 4, dtype=int)
    for hang in range(4):
        for cot in range(4):
            out[hang][cot] = int(w[i * 4 + hang][cot * 8 : cot * 8 + 8], 2)
    return out


# hàm chính
def sub_bytes(x):
    """

    :param x: int
    :return:    int tương ứng sbox
    """

    hang = int(bin(x)[2:10].zfill(8)[0:4], 2)
    cot = int(bin(x)[2:10].zfill(8)[4:8], 2)
    return sBox[hang][cot]


def sub_bytes_all(x):
    out = np.array([[0] * 4] * 4, dtype=int)
    for i in range(4):
        for j in range(4):
            out[i][j] = sub_bytes(x[i][j])
    return out


def shift_rows(x):
    """

    :param x: ma trận
    :return: ma trận
    """
    k = 0

    for i in range(4):
        # print(i)
        a = x[i]
        """
                if k == 1:
            p1 = x[i][0]
            x[i][0] = x[i][1]
            x[i][1] = x[i][2]
            x[i][2] = x[i][3]
            x[i][3] = p1
        if k == 2:
            p1 = x[i][0]
            p2 = x[i][1]
            x[i][0] = x[i][2]
            x[i][1] = x[i][3]
            x[i][2] = p1
            x[i][3] = p2
        if k == 3:
            p1 = x[i][0]
            p2 = x[i][1]
            p3 = x[i][2]
            x[i][0] = x[i][3]
            x[i][1] = p1
            x[i][2] = p2
            x[i][3] = p3
        """
        # dịch cột
        if k == 1:
            p1 = x[0][i]
            x[0][i] = x[1][i]
            x[1][i] = x[2][i]
            x[2][i] = x[3][i]
            x[3][i] = p1
        if k == 2:
            p1 = x[0][i]
            p2 = x[1][i]
            x[0][i] = x[2][i]
            x[1][i] = x[3][i]
            x[2][i] = p1
            x[3][i] = p2
        if k == 3:
            p1 = x[0][i]
            p2 = x[1][i]
            p3 = x[2][i]
            x[0][i] = x[3][i]
            x[1][i] = p1
            x[2][i] = p2
            x[3][i] = p3
        k += 1
    return x


def mix_columns2(x):
    """
    mix 1 ma trận
    :param x:
    :return:
    """
    out = np.array([[0] * 4] * 4, dtype=int)

    for i in range(4):
        h = 0
        for j in range(4):

            t = []
            for k in range(4):
                if mix[h][k] == 1:
                    t.append(bin(x[i][k])[2:10].zfill(8))
                if mix[h][k] == 2:
                    ls = leftShift(bin(x[i][k])[2:10].zfill(8))

                    # print("[0]:",bin(x[i][j])[2:10].zfill(8)[0])
                    if int(bin(x[i][k])[2:10].zfill(8)[0]) == 1:
                        # print("chưa xor:",ls)
                        ls = xor8(ls, "00011011")
                    # print(ls)
                    t.append(ls)
                if mix[h][k] == 3:
                    ls = leftShift(bin(x[i][k])[2:10].zfill(8))
                    # print(ls)
                    if int(bin(x[i][k])[2:10].zfill(8)[0]) == 1:
                        # print("trc xor 2",ls)
                        ls = xor8(ls, "00011011")
                    # print("trc xỏ ket :",ls)
                    ls = xor8(ls, bin(x[i][k])[2:10].zfill(8))
                    t.append(ls)
            h += 1
            # print(t)
            xo = xor8(t[0], xor8(t[1], xor8(t[2], t[3])))
            # nó thay giá trị gốc nếu gán out = x
            out[i][j] = int(xo, 2)
    return out


def add_round_key(a, b):
    out = np.array([[0] * 4] * 4, dtype=int)
    for i in range(4):
        for j in range(4):
            out[i][j] = int(
                xor8(bin(a[i][j])[2:10].zfill(8), bin(b[i][j])[2:10].zfill(8)), 2
            )
    return out


def g(w, round):
    """

    word 8 kí tự:48bit
    :param w:
    :return: w'
    """
    print(round, bin2hex(w))
    b = w[8:48] + w[0:8]
    b2 = ""
    print("ROT:", bin2hex(b))
    for i in range(4):
        bi = b[8 * i : 8 * (i + 1)]
        bi2 = sub_bytes(int(bi, 2))
        b2 += bin(bi2)[2:10].zfill(8)
    print("sub:", bin2hex(b2))
    rcon = bin(rc[int(round / 4)])[2:10].zfill(8) + "0000" * 6
    print("rcon:", bin2hex(rcon))
    x = xor32(b2, rcon)
    print("after:", bin2hex(x))
    # print("after:", bin2hex(xor32(x,hex2bin("EAD27321"))))
    return x


def key_epansion(key_matrix):
    w = []
    for i in range(4):
        s = ""
        # lấy hàng dọc
        s += (
            bin(key_matrix[i][0])[2:10].zfill(8)
            + bin(key_matrix[i][1])[2:10].zfill(8)
            + bin(key_matrix[i][2])[2:10].zfill(8)
            + bin(key_matrix[i][3])[2:10].zfill(8)
        )
        w.append(s)
    for i in range(4, 44):
        temp = w[i - 1]
        ##print(i,temp)
        if i % 4 == 0:
            temp = g(temp, i)
        # print(i,temp)
        w.append(xor32(w[i - 4], temp))
    j = 0
    for i in w:
        print(j, bin2hex(i))
        j += 1
    return w


if __name__ == "__main__":
    # plain = "0123456789ABCDEFFEDCBA9876543210"
    plain = "58A89BB7073DAA060FF436751C46674C"
    # plain2 = "87F24D976E4C90EC46E74AC3A68CD895"
    # key = "0F1571C947D9E8590CB7ADD6AF7F6798"
    key = "344E74129CD8D1D127FC62A01EF147B7"
    # key = "AC19285777FAD15C66DC2900F321416A"

    # ma trận int
    plain_matrix = str2matrix(plain)
    key_matrix = str2matrix(key)

    show_Matrix_Int2Hex(key_matrix)
    w = key_epansion(key_matrix)

    state = add_round_key(plain_matrix, key_matrix)
    # 1->9
    for i in range(1, 10):
        state = sub_bytes_all(state)
        # show_Matrix_Int2Hex(state)
        state = shift_rows(state)
        # show_Matrix_Int2Hex(state)
        state = mix_columns2(state)
        # show_Matrix_Int2Hex(state)
        state = add_round_key(state, w4_matrix_int(w, i))
        # show_Matrix_Int2Hex(state)
    # 10
    state = sub_bytes_all(state)
    state = shift_rows(state)
    state = add_round_key(state, w4_matrix_int(w, 10))

    for i in state:
        for j in i:
            print(bin2hex(bin(j)[2:10].zfill(8)), end="")
