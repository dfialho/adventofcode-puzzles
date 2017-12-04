from collections import Iterator


def is_passphrase_valid(passphrase: str) -> bool:
    words = passphrase.split(' ')
    distinct_words = set(str(sorted(word)) for word in words)
    return len(words) == len(distinct_words)


def check_passphrases(passphrases: Iterator) -> int:
    return sum(1 for passphrase in passphrases if is_passphrase_valid(passphrase))


def passphrases(path: str):
    with open(path) as file:
        for line in file:
            yield line.strip()


def main():
    print("Solution part 1:", check_passphrases(passphrases("input.txt")))


if __name__ == '__main__':
    main()
