"""
input :
4 4
1 4 L
2 3 T
4 1 L
3 1 L

output :
4
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def group_update(group_name):
    for nd in groups[group_name]:
        if node_val[nd] == 0:
            node_val[nd] = 1
        elif node_val[nd] == 1:
            node_val[nd] = 0


def group_merge(gr1, gr2):
    for i, name in enumerate(group_name):
        if name == gr1:
            group_name[i] = gr2
    groups[gr2] += groups[gr1]
    groups[gr1].clear()


if __name__ == "__main__":
    V, M = map(int, input().rstrip().split())

    cnt = 0
    groups = [[] for _ in range(M + 1)]
    group_name = [-1 for _ in range(V + 1)]
    node_val = [-1 for _ in range(V + 1)]
    for _ in range(M):
        a, b, c = input().rstrip().split()
        a, b = map(int, (a, b))

        if group_name[a] == -1 and group_name[b] == -1:
            # 항상 성공. 노드 값을 새롭게 부여
            group_name[a] = group_name[b] = cnt
            groups[cnt].append(a)
            groups[cnt].append(b)

            if c == 'T':
                node_val[a] = node_val[b] = 1
            elif c == 'L':
                node_val[a] = 0
                node_val[b] = 1

        elif group_name[a] == -1 and group_name[b] != -1:
            # 항상 성공. 노드 값 이미 있는 놈한테 맞춰서 설정하면 됨.
            group_name[a] = group_name[b]
            groups[group_name[b]].append(a)

            if c == 'T':
                node_val[a] = node_val[b]
            elif c == 'L':
                if node_val[b] == 1: node_val[a] = 0
                elif node_val[b] == 0: node_val[a] = 1

        elif group_name[a] != -1 and group_name[b] == -1:
            # 항상 성공. 노드 값 이미 있는 놈한테 맞춰서 설정하면 됨.
            group_name[b] = group_name[a]
            groups[group_name[a]].append(b)

            if c == 'T':
                node_val[b] = node_val[a]
            elif c == 'L':
                if node_val[a] == 1: node_val[b] = 0
                elif node_val[a] == 0: node_val[b] = 1

        elif group_name[a] != group_name[b]:
            # 서로 다른 그룹에 대한 쿼리. 항상 성공. 나머지 하나의 그룹을 group update하여 merge
            if c == 'T':
                if node_val[a] != node_val[b]:
                    group_update(group_name[a])
            elif c == 'L':
                if node_val[a] == node_val[b]:
                    group_update(group_name[b])
            group_merge(group_name[a], group_name[b])

        elif group_name[a] == group_name[b]:
            # 쿼리가 모순이 없는 쿼리인지 곧장 판정 가능
            if c == 'T':
                if node_val[a] != node_val[b]:
                    break
            elif c == 'L':
                if node_val[a] == node_val[b]:
                    break

        cnt += 1
    print(cnt)