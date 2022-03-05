def merge(txt, pos, scale):
    if pos + scale >= len(txt):
        return len(txt[pos:]), len(txt)

    pat = txt[pos: pos + scale]
    pos += scale
    cnt = 1
    while pos < len(txt) and pat == txt[pos: pos + scale]:
        cnt += 1
        pos += scale

    if cnt == 1:
        return len(pat), pos
    else:
        if cnt < 10:
            return len(pat) + 1, pos
        if cnt < 100:
            return len(pat) + 2, pos
        if cnt < 1000:
            return len(pat) + 3, pos
        if cnt == 1000:
            return len(pat) + 4, pos


def solution(s):
    minval = len(s)
    for scale in range(1, len(s) // 2 + 1):
        pos = 0
        tot = 0
        # print(f"scale = {scale}")
        while pos < len(s):
            merged_length, pos = merge(s, pos, scale)
            tot += merged_length
            # print(tot, pos)
        minval = min(minval, tot)

    return minval


if __name__ == "__main__":
    s = "xxxxxxxxxxyyy"
    print(solution(s))
