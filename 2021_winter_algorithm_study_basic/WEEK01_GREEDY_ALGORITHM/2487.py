import sys

#sys.stdin = open("input.txt", "r")

scores = []
cnt = 0

N = int(input())
for _ in range(N):
    tmp = int(input())
    scores.append(tmp)

if N == 1:
    print(cnt)
    sys.exit()

scores.reverse()
#print(scores)

Max = scores[0]
for ind, score in enumerate(scores[1:]):
    if score >= Max:
        difference = score - Max + 1
        cnt += difference
        scores[ind + 1] = scores[ind + 1] - difference
        Max = scores[ind + 1]
    else:
        Max = scores[ind + 1]

print(cnt)