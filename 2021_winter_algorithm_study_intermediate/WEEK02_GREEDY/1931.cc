#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;
vector<pii> V;

int main(){
	int N;
	scanf("%d", &N);
	for(int i = 0; i < N; i++){
		int u, v;
		scanf("%d %d", &u, &v);
		V.push_back({v, u});
	}
	sort(V.begin(), V.end());
	int cnt = 0;
	int cur = 0;
	for(auto elem : V){
		if(elem.second >= cur){
			cnt++;
			cur = elem.first;
		}
	}
	printf("%d\n", cnt);
}