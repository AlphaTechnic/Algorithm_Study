"""
input :
3 6
antarctica
antahellotica
antacartica

output :
2
"""
import sys
from itertools import combinations

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def get_score(ref_txts, combi):
    cnt = 0
    for txt in ref_txts:
        flag = True
        for ch in txt:
            if ch not in combi:
                flag = False
                break
        if flag:
            cnt += 1
    return cnt


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    if K < 5:
        print(0)
        exit(0)
    elif K == 26:
        print(N)
        exit(0)

    default = {'a', 'n', 't', 'i', 'c'}
    ref_txts = [set(input().rstrip()[4:-4]) - default for _ in range(N)]
    new_chs = set()
    for ref_txt in ref_txts:
        new_chs = new_chs.union(ref_txt)

    mxv = 0
    if len(new_chs) >= K - 5:
        for combi in combinations(new_chs, K - 5):
            score = get_score(ref_txts, combi)
            mxv = max(mxv, score)
    else:
        score = get_score(ref_txts, new_chs)
        mxv = max(mxv, score)
    print(mxv)
