"""
input :
4 2 3 10

output :
18
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    x, y, hor_cost, diag_cost = map(int, input().rstrip().split())

    case1 = case2 = case3 = 10 ** 20
    mnv = min(x, y)
    mxv = max(x, y)

    case1 = (x + y) * hor_cost
    if (x + y) % 2 == 0:
        case2 = mxv * diag_cost
    else:
        case3 = (mxv - 1) * diag_cost + hor_cost
    case4 = mnv * diag_cost + (mxv - mnv) * hor_cost

    print(min(case1, case2, case3, case4))
