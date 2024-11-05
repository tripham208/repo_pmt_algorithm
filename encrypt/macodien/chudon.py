if __name__ == "__main__":
    d = {}
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # bảng chữ cái gốc
    b = "WBXGIHOVSYMFUAKZJNCPQLTRED"  # bảng chữ cái mới
    for i in range(0, 26):  # map chuyển đổi cũ -> mới
        d[a[i]] = b[i]
    c = "ONESWALLOWDOESNT"  # input
    print(d)
    for i in c:
        for j in d.keys():
            if i == j:
                print(d[j], end="")
