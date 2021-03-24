N = int(input())
attackers = list(map(int, input().split()))

cnt = 0
best_kill = 0
best_killer = attackers[0]

for ind, attacker in enumerate(attackers):
    if best_killer > attacker:
        cnt += 1
    if (best_killer < attacker) or (ind == N - 1):
        best_killer = attacker
        if best_kill < cnt:
            best_kill = cnt
        cnt = 0

print(best_kill)

