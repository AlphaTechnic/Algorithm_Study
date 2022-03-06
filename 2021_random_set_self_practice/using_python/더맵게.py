import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)
    cnt = 0
    while True:
        smallest = hq.heappop(scoville)
        if smallest >= K:
            return cnt
        if len(scoville) == 0:
            return -1

        second_smallest = hq.heappop(scoville)
        new_val = smallest + 2 * second_smallest
        hq.heappush(scoville, new_val)
        cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution([0, 1], 10000))
