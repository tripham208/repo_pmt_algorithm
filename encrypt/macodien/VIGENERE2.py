if __name__ == "__main__":
    d = {
        "A": 0,
        "C": 2,
        "B": 1,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 2,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25,
    }  # char -> số
    dd = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
        7: "H",
        8: "I",
        9: "J",
        10: "K",
        11: "L",
        12: "M",
        13: "N",
        14: "O",
        15: "P",
        16: "Q",
        17: "R",
        18: "S",
        19: "T",
        20: "U",
        21: "V",
        22: "W",
        23: "X",
        24: "Y",
        25: "Z",
    }  # số-> char
    a = "BETTERSAFETH"
    k = "ITSASM"
    ar = []  # list char-> số
    ar2 = []  # list số-> char
    # chuyển input-> list số
    for i in a:
        for j in d.keys():
            if i == j:
                ar.append(d[j])
    ck = 0
    # chuyển key -> list số
    for i in k:
        for j in d.keys():
            if i == j:
                ar2.append(d[j])
    # key < input thì thêm input vào key
    if len(ar2) < len(a):
        ck = len(ar2)
        while ck < len(a):
            for i in a:
                for j in d.keys():
                    if i == j:
                        ar2.append(d[j])
                        ck += 1

    for i in range(0, len(a)):
        print(dd[(ar[i] + ar2[i]) % 26], end="")  # vị trí sau khi thay đổi
        # d:3 + w:22 -> z:25
