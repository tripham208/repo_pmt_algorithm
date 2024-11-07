from encrypt.macodien import d, dd

if __name__ == "__main__":
    a = "ITSASMALLWORLDIT"
    k = 22
    for i in a:
        for j in d.keys():
            if i == j:
                print(dd[(d[j] + k) % 26], end="")  # in ra vị trí sau khi dịch
