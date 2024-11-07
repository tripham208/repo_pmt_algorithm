from encrypt.macodien import d, dd

if __name__ == "__main__":
    a = "BETTERSAFETH"
    k = "ITSASM"
    ar = []  # list input -> số
    ar2 = []  # list key ->số
    # chuyển input -> chuỗi số
    for i in a:
        for j in d.keys():
            if i == j:
                ar.append(d[j])
    ck = 0
    while ck < len(a):  # đến khi độ dài key ~ input
        for i in k:
            for j in d.keys():
                if i == j:
                    ar2.append(d[j])
                    ck += 1
    for i in range(0, len(a)):
        print(dd[(ar[i] + ar2[i]) % 26], end="")  # vị trí sau khi thay đổi
        # d:3 + w:22 -> z:25
