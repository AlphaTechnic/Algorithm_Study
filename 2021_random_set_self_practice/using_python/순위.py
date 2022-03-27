from collections import defaultdict


class Graph:
    def __init__(self, n, graph):
        self.V = n
        self.graph = graph
        self.visited = [False for _ in range(self.V + 1)]

        self.indeg = [0 for _ in range(self.V + 1)]
        self.outdeg = [0 for _ in range(self.V + 1)]

    def search(self):
        for i in range(1, self.V + 1):
            self.dfs(i, i)
            self.visited = [False for _ in range(self.V + 1)]

        # return answer
        cnt = 0
        for i in range(1, self.V + 1):
            if self.indeg[i] + self.outdeg[i] == self.V - 1:
                cnt += 1
        return cnt

    def dfs(self, root, cur):
        self.visited[cur] = True
        if root != cur:
            self.outdeg[root] += 1
            self.indeg[cur] += 1
        for nxt in self.graph[cur]:
            if self.visited[nxt]:
                continue
            self.dfs(root, nxt)


def solution(n, results):
    graph = defaultdict(set)
    for a, b in results:  # 'a' is winner
        graph[a].add(b)
    g = Graph(n, graph)
    return g.search()


if __name__ == "__main__":
    print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
