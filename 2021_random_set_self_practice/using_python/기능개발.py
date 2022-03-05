def get_remains(progresses, speeds):
    remains = []
    for i, progress in enumerate(progresses):
        piv = (100 - progress) // speeds[i]
        if (100 - progress) % speeds[i] == 0:
            remains.append(piv)
        else:
            remains.append(piv + 1)
    return remains


def solution(progresses, speeds):
    remains = get_remains(progresses, speeds)
    if len(remains) == 1:
        return [1]

    ans = []
    pos = 0
    cnt = 1
    i = 1
    while True:
        if remains[pos] >= remains[pos + i]:
            cnt += 1
            i += 1
        else:
            ans.append(cnt)
            pos = pos + i
            cnt = 1
            i = 1

        if pos + i == len(remains):
            ans.append(cnt)
            break

    return ans


if __name__ == "__main__":
    print(solution([95, 90, 99, 99, 80, 99, 98], [1, 1, 1, 1, 1, 1, 1]))
