"""
input :
4 3
1 4 L
2 3 T
4 1 T

output :
2
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(p, val):
    st = list()
    st.append(p)
    visited[p] = val

    while st:
        cur = st.pop()
        for nxt in range(1, V + 1):
            if adj_mat[cur][nxt] == '-1': continue
            if adj_mat[cur][nxt] == 'L':
                if not visited[nxt]:
                    visited[nxt] = visited[cur] * (-1)
                    st.append(nxt)
                else:
                    if visited[nxt] != visited[cur] * (-1):
                        return False
            elif adj_mat[cur][nxt] == 'T':
                if not visited[nxt]:
                    visited[nxt] = visited[cur]
                    st.append(nxt)
                else:
                    if visited[nxt] != visited[cur]:
                        return False
    return True


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    adj_mat = [['-1' for _ in range(V + 1)] for _ in range(V + 1)]

    cnt = 0
    visited = [0 for _ in range(V + 1)]
    for _ in range(E):
        a, b, ANS = input().rstrip().split()
        a, b = map(int, (a, b))

        if adj_mat[a][b] == '-1':
            adj_mat[a][b] = ANS
            adj_mat[b][a] = ANS
        elif adj_mat[a][b] != ANS:
            break
        elif adj_mat[a][b] == ANS:
            pass

        if not dfs(a, -1):
            break
        else:
            cnt += 1
    print(cnt)
