def main(num: int | float, iterations: int):
    # input: 6.25
    # output: 2.5

    # implementing Newton's method for finding square roots
    root = num / 2
    count = 0
    while count < iterations:
        root = (root + num / root) / 2

        count += 1
    print(root)


main(6.25, 100000)
