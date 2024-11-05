import math


# hàm phụ
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


def habac(a, m, n):
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


def phi(n):
    result = n
    i = 2
    while i * i <= n:
        # print(i," ",n)
        if n % i == 0:
            # phân tách n -> tích các số nt
            while n % i == 0:
                n /= i
                # print("   ", i, " ", n)
            # print(result)
            result -= result / i
            # print(result)
        i += 1
    if n > 1:
        result -= result / n
    result = int(result)
    return result


# hàm chính
def RSA1(p, q, e, M):
    """

    :param p:
    :param q:
    :param e:
    :return:    PU = {e, n}
                PR = {d, n}
                An mã: C
                Ba giải mã C: M’
    """
    output = []
    n = p * q
    if math.gcd(e, n) != 1:
        return -1
    d = euclid(e, phi(n))
    # khóa công khai
    output.append(e)
    output.append(n)
    # khóa riêng
    output.append(d)
    output.append(n)
    # Amã hóa
    c = habac(M, d, n)
    output.append(c)
    # Bgiải mã
    m2 = habac(c, e, n)
    output.append(m2)
    return output


def RSA2(p, q, e, M):
    """

    :param p:
    :param q:
    :param e:
    :param M:
    :return:
    """
    output = []
    n = p * q
    if math.gcd(e, n) != 1:
        return -1
    d = euclid(e, phi(n))
    # khóa riêng/khoá công khai
    output.append(e)
    output.append(n)
    output.append(d)
    output.append(n)
    # B mã hóa
    c = habac(M, e, n)
    output.append(c)
    # A giải mã
    m2 = habac(c, d, n)
    output.append(m2)
    return output


if __name__ == "__main__":
    p = 47
    q = 53
    e = 71
    M = 67
    a = RSA1(p, q, e, M)
    print(a)
    a = RSA2(p, q, e, M)
    print(a)
