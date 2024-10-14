def main():
    N = int(input())
    if N < 99:
        return 99

    l = (N // 100 - 1) * 100 + 99
    r = N // 100 * 100 + 99

    dl = abs(l - N)
    dr = abs(r - N)
    if dr == dl or dl > dr:
        return r
    else:
        return l


print(main())
