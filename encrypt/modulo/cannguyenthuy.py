import math


# HÀM PHỤ
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


def euler_luythua(a, m, n):
    """
    tính lũy thừa b = a^m mod n
    :param a:
    :param m:
    :param n:
    :return: a^m mod n
    """

    if math.gcd(a, n) == 1:
        m = m % phi(n)
        return habac(a, m, n)

    return -1


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


# HÀM CHÍNH
def cannguyenthuy(a, n):
    """

    :param a:
    :param n:
    :return: true/false
    """
    # print(math.gcd(a,n))
    if math.gcd(a, n) != 1:  # ĐỊNH LÝ EULER -> gcd=1
        return 0
    # print(phi(n))
    # duyệt lần lượt các mũ
    for i in range(1, phi(n)):
        # print(euler_luythua(a,i,n))
        if euler_luythua(a, i, n) == 1:
            return 0
    return 1


if __name__ == "__main__":
    print(cannguyenthuy(7, 449))
