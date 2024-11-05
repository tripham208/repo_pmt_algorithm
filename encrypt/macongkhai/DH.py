import math


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


def DH(q, a, xA, xB):
    """

    :param q:
    :param a:
    :param xA:
    :param xB:
    :return:
    """
    output = []

    output.append(habac(a, xA, q))  # tính yA
    output.append(habac(a, xB, q))  # tính yB
    output.append(habac(output[1], xA, q))  # tính k
    return output


if __name__ == "__main__":
    a = DH(6781, 7, 380, 478)
    print(a)
