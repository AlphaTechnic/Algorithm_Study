#include <stdio.h>
#include <algorithm>
#include <vector>


struct task{
	int t, s, i;
};

std::vector<task> V;
int N;

bool cmp(task x, task y){
	if(x.t*y.s == x.s*y.t) return x.i < y.i;
	return x.t*y.s < x.s*y.t;
}

int main(){
	scanf("%d", &N);
	for(int i = 0, x, y; i < N; i++){
		scanf("%d%d", &x, &y);
		V.push_back({x,y,i+1});
	}
	std::sort(V.begin(), V.end(), cmp);

	for(auto e:V){
		printf("%d ", e.i);
	}
}