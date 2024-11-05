if __name__ == "__main__":
    a = "DONTTROUBLETROUBLE"  # input
    k = 7  # key
    b = []  # bảng : input -> k hàng
    for i in range(0, k):
        b.append([])
    j = 0  # input -> bảng
    for i in a:
        if j == k:
            j = 0
        b[j].append(i)
        j += 1
    # in bảng mã
    for i in b:
        for j in i:
            print(j, end="")
