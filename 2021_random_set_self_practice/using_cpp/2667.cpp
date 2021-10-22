#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
using pii = pair<int, int>;
#define SZ (26)

int N;
int bd[SZ][SZ];
vector<int> ans;
int cnt;
bool vis[SZ][SZ];
pii dir[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

void dfs(int cy, int cx, int N){
    cnt++;
    vis[cy][cx] = true;
    for (auto [dy, dx]: dir){
        int ny, nx;
        ny = cy + dy; nx = cx + dx;
        if (!(0 <= ny && ny < N)) continue;
        if (!(0 <= nx && nx < N)) continue;
        if (vis[ny][nx]) continue;
        if (bd[ny][nx] == 0) continue;

        dfs(ny, nx, N);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    string ln;
    for (int r = 0; r < N; r++){
        cin >> ln;
        for (int c = 0; c < N; c++){
            bd[r][c] = ln[c] - '0';
        }
    }

    for (int r = 0; r < N; r++){
        for (int c = 0; c < N; c++){
            if (bd[r][c] == 0) continue;
            if (vis[r][c]) continue;

            cnt = 0;
            dfs(r, c, N);
            ans.push_back(cnt);
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << '\n';
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << '\n';
    }
}