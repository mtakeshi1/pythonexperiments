def lps(pattern):
    r = [0] * len(pattern)
    prev = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[prev]:
            prev += 1
            r[i] = prev
            i += 1
        else:
            if prev != 0:
                prev = r[prev-1]
            else:
                r[i] = 0
                i += 1
    return r


def kmp_search(pattern, phrase):
    lps_array = lps(pattern)
    i, j = 0, 0
    while (len(phrase) - i) >= (len(pattern) - j):
        if pattern[j] == phrase[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(phrase) and pattern[j] != phrase[i]:
            if j != 0:
                j = lps_array[j-1]
            else:
                i += 1
    return -1


if __name__ == '__main__':
    print(kmp_search('aaabbaa', 'aabaabb'))
