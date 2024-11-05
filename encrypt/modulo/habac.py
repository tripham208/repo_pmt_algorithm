import math


def habac(a, m, n):
    """
    tính a^m mod n
    :param a:
    :param m:
    :param n:
    :return:
    """
    arr = []  # mảng lưu phần dư
    x = 0
    while m > 3:  # hạ bậc
        if m % 2 == 0:
            m = int(m / 2)
            arr.append(0)
        else:
            m = int(m / 2)
            arr.append(1)
        x += 1
    t = math.pow(a, m) % n  # tính phần sau hạ
    for i in range(x - 1, -1, -1):  # tính ngược lại
        if arr[i] == 0:
            t = math.pow(t, 2) % n
        else:
            t = math.pow(t, 2) * a % n
    return int(t)


if __name__ == "__main__":
    print(habac(317, 6221, 6221))
