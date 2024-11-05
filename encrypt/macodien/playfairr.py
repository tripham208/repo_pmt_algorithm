if __name__ == "__main__":
    a = "ITSANILLBIRD"
    k = "NOROSEW"
    b = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    d = [[], [], [], [], []]  # ma tran khoa
    hang = 0
    cot = 0
    dap_an = ""
    # loai ki tự bi lap trong key
    f = ""
    for i in k:
        if i not in f:
            f += i

    # key -> ma trân khóa
    for i in f:
        ck = 0
        for j in range(0, 5):
            if i in d[j]:
                ck = 1
        if ck == 1:
            ck = 0
            continue
        if i == "I" or i == "J":
            b = b.replace("I", "")
        if cot == 5:
            hang += 1
            cot = 0
        d[hang].append(i)
        cot += 1
    # bảng chữ cái -> ma trận khóa
    for i in b:
        if i not in k:
            if cot == 5:
                hang += 1
                cot = 0
            d[hang].append(i)
            cot += 1

    dd = {}  # map :char -> vị trí trong ma trận khóa
    for i in range(0, 5):
        for j in range(0, 5):
            dd[d[i][j]] = (i + 1) * 10 + j

    # mã hóa từng kí tự bằng ma trận khóa
    i = 0
    while i < len(a) - 1:
        if a[i] == a[i + 1]:
            print(a[i], "X")
            x1 = int(dd[a[i]] / 10)
            y1 = int(dd[a[i]] % 10)
            print(x1, y1)
            x2 = int(dd["X"] / 10)
            y2 = int(dd["X"] % 10)
            print(x2, y2)
            if x1 == x2:  # cùng hàng
                if y1 == 4:  # cột cuối
                    dap_an += d[x1 - 1][0]  # cuộn về đầu
                else:
                    dap_an += d[x1 - 1][y1 + 1]
                if y2 == 4:  # cột cuôis
                    dap_an += d[x2 - 1][0]
                else:
                    dap_an += d[x2 - 1][y2 + 1]
            elif y1 == y2:  # cùng cột
                if x1 == 5:  # cột cuối cuộn về đầu
                    dap_an += d[0][y1]
                else:
                    dap_an += d[x1][y1]
                if x2 == 5:
                    dap_an += d[0][y2]
                else:
                    dap_an += d[x2][y2]
            else:
                dap_an += d[x1 - 1][y2]
                dap_an += d[x2 - 1][y1]
            i += 1
        else:
            print(a[i], a[i + 1])
            x1 = int(dd[a[i]] / 10)
            y1 = int(dd[a[i]] % 10)
            print(x1, y1)
            x2 = int(dd[a[i + 1]] / 10)
            y2 = int(dd[a[i + 1]] % 10)
            print(x2, y2)
            if x1 == x2:  # cùng hàng
                if y1 == 4:  # cột cuối
                    dap_an += d[x1 - 1][0]  # cuộn về đầu
                else:
                    dap_an += d[x1 - 1][y1 + 1]
                if y2 == 4:  # cột cuôis
                    dap_an += d[x2 - 1][0]
                else:
                    dap_an += d[x2 - 1][y2 + 1]
            elif y1 == y2:  # cùng cột
                if x1 == 5:  # cột cuối cuộn về đầu
                    dap_an += d[0][y1]
                else:
                    dap_an += d[x1][y1]
                if x2 == 5:
                    dap_an += d[0][y2]
                else:
                    dap_an += d[x2][y2]
            else:
                dap_an += d[x1 - 1][y2]
                dap_an += d[x2 - 1][y1]
            i += 2
    # thiếu kí tự cuối
    if i == len(a) - 1:
        print(a[i], "X")
        x1 = int(dd[a[i]] / 10)
        y1 = int(dd[a[i]] % 10)
        print(x1, y1)
        x2 = int(dd["X"] / 10)
        y2 = int(dd["X"] % 10)
        print(x2, y2)
        if x1 == x2:  # cùng hàng
            if y1 == 4:  # cột cuối
                dap_an += d[x1 - 1][0]  # cuộn về đầu
            else:
                dap_an += d[x1 - 1][y1 + 1]
            if y2 == 4:  # cột cuôis
                dap_an += d[x2 - 1][0]
            else:
                dap_an += d[x2 - 1][y2 + 1]
        elif y1 == y2:  # cùng cột
            if x1 == 5:  # cột cuối cuộn về đầu
                dap_an += d[0][y1]
            else:
                dap_an += d[x1][y1]
            if x2 == 5:
                dap_an += d[0][y2]
            else:
                dap_an += d[x2][y2]
        else:
            dap_an += d[x1 - 1][y2]
            dap_an += d[x2 - 1][y1]

    print(dap_an)
