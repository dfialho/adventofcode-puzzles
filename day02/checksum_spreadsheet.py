from collections import Iterator


def checksum(rows: Iterator, row_sum) -> int:
    return sum(row_sum(row) for row in rows)


# Part 1
def difference(row: Iterator):
    values = list(row)
    return max(values) - min(values)


# Part 2
def even_division(row: list):
    sorted_row = list(sorted(row, reverse=True))
    for i, x in enumerate(sorted_row):
        for y in sorted_row[i + 1:]:
            if x % y == 0:
                return x // y

    return 0


def input_values(path: str):
    with open(path) as file:
        for line in file:
            yield map(int, line.split(","))


def main() -> None:
    print("Solution part 1:", checksum(input_values("input.txt"), difference))
    print("Solution part 2:", checksum(input_values("input.txt"), even_division))


if __name__ == '__main__':
    main()
