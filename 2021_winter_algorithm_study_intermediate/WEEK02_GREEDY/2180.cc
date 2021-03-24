#include <stdio.h>
#include <algorithm>
#include <vector>

#define MOD 40000

struct task{
	int a,b;
};

std::vector<task> V;
int N;

bool cmp(task x, task y){
	return y.a*x.b < x.a*y.b;
}

int main(){
	scanf("%d", &N);
	for(int i = 0, x, y; i < N; i++){
		scanf("%d%d", &x, &y);
		if(x == 0 && y == 0) continue;
		V.push_back({x,y});
	}
	std::sort(V.begin(), V.end(), cmp);

	int ans = 0;
	for(auto e:V){
		ans = (e.a+1)*ans+e.b;
		ans %= MOD;
	}

	printf("%d\n", ans);
}