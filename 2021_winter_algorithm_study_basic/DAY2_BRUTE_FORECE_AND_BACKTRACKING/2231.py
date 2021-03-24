import sys

sys.stdin = open("input.txt", "r")

N = int(input())

for gen in range(N+1):
    # 자리수의 합
    nums = []
    nums.append(gen)
    while gen != 0:
        extract = gen % 10
        nums.append(extract)
        gen = (gen - extract) / 10
    if sum(nums) == N:
        break

if nums[0] == N:
    print(0)
else:
    print(nums[0])

