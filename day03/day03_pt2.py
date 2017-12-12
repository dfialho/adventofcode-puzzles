from math import sqrt, ceil


def level(n: int) -> int:
    """
    Returns the level for the given position.

    The first square contains only 1 - the level 1
    The second square contains value 2 to 9 - the level 3 (level 3)
    The third square contains value 10 to 25 - the level 5
    The fourth square contains value 26 to 49 - the level 7
    """
    ra = sqrt(n)
    r = int(ra)

    if r % 2 == 0:
        r += 1
    elif ra > r:
        r += 2

    return r


def backward_square(n: int, i: int) -> int:
    """ Computes the backward square """
    # Can be simplified to: backward_i = (r(n) - 1) * (r(n) - 2 + i)
    backward_i = (level(n) - 1) * (level(n) - 2) + (level(n) - 1) * i

    if i == 3:
        backward_i += 1

    return backward_i


def corner_square(n: int, i: int) -> int:
    if i == 0:
        return pow((level(n) - 2), 2) + 1
    else:
        return backward_square(n, i - 1) + 1


def forward_square(n: int, i: int) -> int:
    return corner_square(n, i) + 1


def side_index(n: int) -> int:
    for i in range(4):
        if n - backward_square(n, i) <= 0:
            return i

    return 3


def is_backward_square(n: int, i: int) -> bool:
    return n == backward_square(n, i)


def is_corner_square(n: int, i: int) -> bool:
    return n == corner_square(n, i)


def is_forward_square(n: int, i: int) -> bool:
    return n == forward_square(n, i)


def diff(n: int, i: int) -> int:
    return 1 + (level(n) - 2) // 2 * 8 + 2 * i


def backward_value(grid: list, n: int, i: int) -> int:
    return grid[n - 1] + grid[n - diff(n, i)] + grid[n - diff(n, i) - 1]


def corner_value(grid: list, n: int, i: int) -> int:
    return grid[n - 1] + grid[n - diff(n, i) + 1]


def forward_value(grid: list, n: int, i: int) -> int:
    return grid[n - 1] + grid[n - 2] + grid[n - diff(n, i)] + grid[n - diff(n, i) + 1]


def middle_value(grid: list, n: int, i: int) -> int:
    return grid[n - 1] + grid[n - diff(n, i) - 1] + grid[n - diff(n, i)] + grid[n - diff(n, i) + 1]


def backward_and_forward_value(grid: list, n: int, i: int) -> int:
    return grid[n - 1] + grid[n - 2] + grid[n - diff(n, i)]


def value_function(n: int, i: int):
    if is_corner_square(n, i):
        return corner_value
    elif is_forward_square(n, i) and is_backward_square(n, i):
        return backward_and_forward_value
    elif is_forward_square(n, i):
        return forward_value
    elif is_backward_square(n, i):
        return backward_value
    else:
        return middle_value


def process(bound: int) -> int:
    if bound == 1:
        return 1

    n = 3  # 'n' always holds the position in the spiral
    grid = [None, 1, 1]
    while True:
        side_i = side_index(n)
        square = value_function(n, side_i)
        square_value = square(grid, n, side_i)

        if square_value > bound:
            return square_value

        grid.append(square_value)
        n += 1


def main():
    print("Solution part 2:", process(368078))


if __name__ == '__main__':
    main()
