from unicodedata import name


def main():

    while True:
        val = int(input())

        if val == 42:
            break
        else:
            print(val)


if __name__ == 'main':
    main()
