import sys
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 각 index 정수가 그 정수를 나누는 가장 작은 소수를 값으로 갖도록 만든다.
MAX = 5000000
end = int(math.sqrt(MAX))
min_factors = [i for i in range(MAX + 1)]

for i in range(2, end + 1):
    if min_factors[i] == i:
        for j in range(i + i, MAX + 1, i):
            if min_factors[j] % i == 0:
                min_factors[j] = i

int(input())
num_list = list(map(int, input().split()))
for target_num in num_list:
    while target_num != 1:
        min_factor = min_factors[target_num]
        print(min_factor, end=' ')
        target_num = target_num // min_factor
    print()
