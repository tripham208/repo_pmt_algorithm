import math


# hàm phụ
def ha_bac(a, m, n):
    """
    tính a^m mod n
    :param a:
    :param m:
    :param n:
    :return:
    """
    arr = []
    x = 0
    while m > 3:
        if m % 2 == 0:
            m = int(m / 2)
            arr.append(0)
        else:
            m = int(m / 2)
            arr.append(1)
        x += 1
    t = math.pow(a, m) % n
    for i in range(x - 1, -1, -1):
        if arr[i] == 0:
            t = math.pow(t, 2) % n
        else:
            t = math.pow(t, 2) * a % n
    return int(t)


def euclid(a, n):
    """
    tìm nghịch đảo
    :param a:
    :param n:
    :return: x = a^-1 mod n
    """
    a1 = 1
    a2 = 0
    a3 = n
    b1 = 0
    b2 = 1
    b3 = a
    while b3 > 1:
        q = int(a3 / b3)

        t1 = a1 - q * b1
        t2 = a2 - q * b2
        t3 = a3 - q * b3

        a1 = b1
        a2 = b2
        a3 = b3

        b1 = t1
        b2 = t2
        b3 = t3
    if b3 == 0:
        return -1
    else:
        if b2 > 0:
            return b2
        else:
            return n + b2


# tích nguyên tố
def nguyen_to(n):
    a = []
    i = 2
    while i * i <= n:
        # print(i," ",n)
        if n % i == 0:
            # phân tách n -> tích các số nt

            n /= i

            a.append(i)
        i += 1
    a.append(int(n))
    return a


# trung hoa
def luy_thua(a, k, n):
    """

    :param a:
    :param k:
    :param n:
    :return: a^k mod n
    """
    ds = nguyen_to(n)  # n -> tích nguyên tố :m
    C = []
    M = []
    A = []
    output = 0
    # tính Mi=M/m
    for i in ds:
        m = n / i
        M.append(int(m))
    # tính C =M*M^-1
    for i in range(0, len(M)):
        c = M[i] * euclid(M[i], ds[i])
        C.append(c)
    # tính ai =A mod mi
    for i in range(0, len(M)):
        A.append(ha_bac(a, k, ds[i]))
    # out = tổng ai*ci mod n
    for i in range(0, len(M)):
        output += A[i] * C[i]
    print(ds)
    print(M)
    print(C)
    print(A)
    return output % n


def he_phuong_trinh(m1, m2, m3, a1, a2, a3):
    """
    x mod m1 = a1
    x mod m2 = a2
    x mod m3 = a3
    :param m1:
    :param m2:
    :param m3:
    :param a1:
    :param a2:
    :param a3:
    :return: x
    """
    # tính M ,M1,M2,M3
    M = m1 * m2 * m3
    M1 = M / m1
    M2 = M / m2
    M3 = M / m3
    # TÍNH C
    c1 = M1 * euclid(M1, m1)
    c2 = M2 * euclid(M2, m2)
    c3 = M3 * euclid(M3, m3)
    return (a1 * c1 + a2 * c2 + a3 * c3) % M


if __name__ == "__main__":
    print(luy_thua(179, 53, 41477))
    print(he_phuong_trinh(17, 19, 11, 16, 18, 7))
    # print(nguyento(79663))
