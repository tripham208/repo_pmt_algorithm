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


def euler_luythua(a, m, n):
    """
    tính lũy thừa b = a^m mod n
    :param a:
    :param m:
    :param n:
    :return: a^m mod n
    """

    if math.gcd(a, n) == 1:
        m = m % phi(n)  # tìm phi
        return habac(a, m, n)  # tính lũy thừa bằng hạ bậc

    return -1


if __name__ == "__main__":
    print(phi(4533))
    print(euler_luythua(36, 3918, 287))
