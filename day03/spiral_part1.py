from math import sqrt, ceil


def moves(n: int) -> int:
    ra = sqrt(n)
    r = int(ra)

    if r % 2 == 0:
        r += 1
    elif ra > r:
        r += 2

    l = r // 2
    q = [pow((r - 2), 2) + l + (r - 1) * i for i in range(4)]

    return l + min(abs(n - qi) for qi in q)


def moves2(n: int) -> int:
    if n == 1:
        return 0

    ra = sqrt(n)
    r = int(ra)
    r += int(r % 2) + ceil(ra - r)
    l = r // 2
    q = [pow((r - 2), 2) + l + (r - 1) * i for i in range(4)]

    return l + min(abs(n - qi) for qi in q)


def main():
    print("Solution part 1:", moves(368078))
    # print("Solution part 2:", sum_captcha(captcha, len(captcha) // 2))


if __name__ == '__main__':
    main()
