def splitlist(string, lst):
    a = []
    for chars in lst:
        a.append(x for x in string.split(chars))
        a.append(chars)
        print(a)
    return a


if __name__ == '__main__':
    print(splitlist('hello, world!', ['he', ',', 'or']))