"""Tiny calculator used by our build tooling."""


def add(a, b):
    # BUG: returns the wrong result
    return a - b


def main():
    print("2 + 3 =", add(2, 3))


if __name__ == "__main__":
    main()
