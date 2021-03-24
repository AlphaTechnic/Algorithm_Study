import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
num_list = [i for i in range(1, N+1)]

delta = K - 1
ind = 0
print("<", end='')
ind += delta
ind = ind % len(num_list)
print("%s" % num_list[ind], end='')
del(num_list[ind])

while len(num_list) != 0:
    ind += delta
    ind = ind % len(num_list)
    print(", %s" % num_list[ind], end='')
    del(num_list[ind])
print(">")