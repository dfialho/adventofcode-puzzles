def sum_captcha(captcha: str, step_size: int) -> int:
    solution = 0
    digit_count = len(captcha)

    for i, digit in enumerate(captcha):
        forward_position = (i + step_size) % digit_count
        if digit == captcha[forward_position]:
            solution += int(digit)

    return solution


def input(path: str) -> str:
    with open(path) as file:
        return file.read()


def main():
    captcha = input("input.txt")

    print("Solution part 1:", sum_captcha(captcha, 1))
    print("Solution part 2:", sum_captcha(captcha, len(captcha) // 2))


if __name__ == '__main__':
    main()
