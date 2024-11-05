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


def dinh_nghia(a, n):
    for i in range(1, n - 1):
        if (i * a) % n == 1:
            return i
    return -1


if __name__ == "__main__":
    print(euclid(1125, 3739))
    print(dinh_nghia(103, 127))
