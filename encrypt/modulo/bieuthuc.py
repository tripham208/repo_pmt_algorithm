from euclid_morong import euclid
from habac import habac


def tong(a, b, x, y, n):
    """
    A1= (a^x+b^y) mod n
    :param a:
    :param b:
    :param x:
    :param y:
    :param n:
    :return: A1
    """
    c = habac(a, x, n)
    d = habac(b, y, n)
    return (c + d) % n


def hieu(a, b, x, y, n):
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
    return (c - d) % n


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


def nghichdao(b, y, n):
    """

    :param a:
    :param b:
    :param x:
    :param y:
    :param n:
    :return:
    """
    c = habac(b, y, n)
    return euclid(c, n)


def thuong(a, b, x, y, n):
    """

    :param a:
    :param b:
    :param x:
    :param y:
    :param n:
    :return:
    """
    c = habac(a, x, n)
    d = nghichdao(b, y, n)
    return (c * d) % n


if __name__ == "__main__":
    a = 71
    b = 83
    x = 596
    y = 375
    n = 239
    print("A1 =", tong(a, b, x, y, n))
    print("A2 =", hieu(a, b, x, y, n))
    print("A3 =", tich(a, b, x, y, n))
    print("A4 =", nghichdao(b, y, n))
    print("A5 =", thuong(a, b, x, y, n))
