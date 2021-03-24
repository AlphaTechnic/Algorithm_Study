import sys
sys.stdin = open("input.txt", "r")

while True:
    s = input()
    if s == ".":
        break
    fail = [0]*len(s)

    j = 0
    for i in range(1, len(s)):
        if j > 0 and (s[i] != s[j]):
            j = fail[j-1]
        if s[i] == s[j]:
            j += 1
            fail[i] = j

    p = fail[-1]
    q = len(s) - p

    if q == 0 or (p % q != 0):
        print(1)
    else:
        print(p // q + 1)
