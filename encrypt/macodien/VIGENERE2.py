from encrypt.macodien import d, dd

if __name__ == "__main__":
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
