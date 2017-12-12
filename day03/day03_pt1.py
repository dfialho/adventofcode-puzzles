from math import sqrt, ceil


def count_moves(n: int) -> int:
    if n == 1:
        return 0

    ra = sqrt(n)
    r = int(ra)
    r += int(r % 2) + ceil(ra - r)
    l = r // 2
    q = [pow((r - 2), 2) + l + (r - 1) * i for i in range(4)]

    return l + min(abs(n - qi) for qi in q)


def main():
    print("Solution part 1:", count_moves(368078))


if __name__ == '__main__':
    main()
