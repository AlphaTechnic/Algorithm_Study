"""
input :
10 24
5
7
5
4
2
7
8
5
3
4
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

price_trend = []
N, AMOUNT = map(int, input().split())
for _ in range(N):
    price_trend.append(int(input()))

if N == 1:
    print(AMOUNT)
    exit()

buy_flag = False
for i in range(N-1):
    if not buy_flag and price_trend[i] < price_trend[i+1]:  # 사 놓은 게 없는데 저점을 만남 -> 매수
        buy_num = AMOUNT // price_trend[i]
        AMOUNT -= buy_num * price_trend[i]
        buy_flag = True
    elif buy_flag and price_trend[i] > price_trend[i+1]:  # 사놓은 게 있는데 고점을 만남 -> 매도
        AMOUNT += buy_num * price_trend[i]
        buy_flag = False

if buy_flag: # 마지막 날에 들고 있는 코인이 있다면 -> 전량 매도
    AMOUNT += buy_num * price_trend[-1]

print(AMOUNT)