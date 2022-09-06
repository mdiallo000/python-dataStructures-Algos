from unicodedata import name


def main():

    while True:
        val = int(input())

        if val == 42:
            break
        else:
            print(val)


# if __name__ == '__main__':
#     main()
def anagrams(S):
    d = {}
    for word in S:
        s = "".join(sorted(word))
        if s in d:
            d[s].append(word)
        else:
            d[s] = [word]

    return [d[s] for s in d if len(d[s]) > 1]
