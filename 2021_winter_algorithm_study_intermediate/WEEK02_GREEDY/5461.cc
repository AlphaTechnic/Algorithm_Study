#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#define MAXN 500050

using namespace std;

int N;
long long int W;
int S[MAXN], Q[MAXN];
vector<pair<double, int>> V;
vector<pair<int,int>> ANS;
priority_queue<int> PQ;

int main(){
	scanf("%d%lld", &N, &W);
	for(int i = 0; i < N; i++){
		scanf("%d%d", S+i, Q+i);
		V.push_back({(double)S[i]/Q[i], i});
	}
	sort(V.begin(), V.end());

	int ans_cardinality = 0;
	int ans_ratio_a = 0;
	int ans_ratio_b = 0;
	int ans_index = 0;
	long long int ans_sum_of_Q = 0;
	
	long long int sum_of_Q = 0;
	for(int i = 0; i < N; i++){
		int cur_idx = V[i].second;
		int cur_ratio_a = S[cur_idx];
		int cur_ratio_b = Q[cur_idx];

		sum_of_Q += Q[cur_idx];
		PQ.push(Q[cur_idx]);
		while(sum_of_Q*cur_ratio_a > W*cur_ratio_b){
			sum_of_Q -= PQ.top();
			PQ.pop();
		}

		if(PQ.size() > ans_cardinality || (PQ.size() == ans_cardinality && sum_of_Q*cur_ratio_a*ans_ratio_b < ans_sum_of_Q*ans_ratio_a*cur_ratio_b)){
			ans_cardinality = PQ.size();
			ans_sum_of_Q = sum_of_Q;
			ans_ratio_a = cur_ratio_a;
			ans_ratio_b = cur_ratio_b;
			ans_index = i;
		}
	}

	for(int i = 0; i <= ans_index; i++){
		ANS.push_back({Q[V[i].second], V[i].second});
	}
	sort(ANS.begin(), ANS.end());

	printf("%d\n", ans_cardinality);
	for(int i = 0; i < ans_cardinality; i++){
		printf("%d\n", ANS[i].second+1);
	}

}