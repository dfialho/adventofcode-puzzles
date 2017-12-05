def count_steps(offsets: list) -> int:
    current_position = 0
    step_count = 0

    while 0 <= current_position < len(offsets):
        offset = offsets[current_position]
        offsets[current_position] += -1 if offset >= 3 else +1
        current_position += offset
        step_count += 1

    return step_count


def offsets(path: str):
    with open(path) as file:
        for line in file:
            yield int(line)


def main():
    print("Solution part 2:", count_steps(list(offsets("input.txt"))))


if __name__ == '__main__':
    main()
