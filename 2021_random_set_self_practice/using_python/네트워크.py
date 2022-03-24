class DFS(object):
    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.visited = [False for _ in range(len(adj_list))]
        self.scc_num = 0

    def dfs(self, cur):
        self.visited[cur] = True
        for nxt in range(len(self.adj_list[cur])):
            if not self.visited[nxt] and self.adj_list[cur][nxt]:
                self.dfs(nxt)

    def visited_chk(self, cur):
        return self.visited[cur]

    def network_cnt_up(self):
        self.scc_num += 1

    def how_many_network(self):
        return self.scc_num

    def __call__(self, cur):
        return self.dfs(cur)


def solution(n, adj_list):
    dfs = DFS(adj_list)
    for i in range(n):
        if not dfs.visited_chk(i):
            dfs(i)
            dfs.network_cnt_up()
    return dfs.how_many_network()


if __name__ == "__main__":
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
