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


def tich(a, b, x, y, n):
    """

    :param a:
    :param b:
    :param x:
    :param y:
    :param n:
    :return:
    """
    c = habac(a, x, n)
    d = habac(b, y, n)
    return (c * d) % n


# hàm chính
def DSA(HM, p, q, h, xA, k):
    output = []
    # khóa công khai A
    g = habac(h, (p - 1) / q, p)
    yA = habac(g, xA, p)
    output.append(yA)
    # chữ kí số A
    r = habac(g, k, p) % q
    output.append(r)
    s = (euclid(k, q) * (HM + xA * r) % q) % q
    output.append(s)
    # xác minh
    w = euclid(s, q)
    u1 = (HM * w) % q
    u2 = (r * w) % q
    v = tich(g, yA, u1, u2, p) % q
    output.append(v)
    # v=r thì đúng chữ kí
    return output


if __name__ == "__main__":
    print(DSA(9, 83, 41, 32, 2, 2))
