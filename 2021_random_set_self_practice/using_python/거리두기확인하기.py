from itertools import combinations


def valid(board, pos1, pos2):
    y1, x1 = pos1
    y2, x2 = pos2
    if abs(y1 - y2) + abs(x1 - x2) > 2:
        return True
    if abs(y1 - y2) + abs(x1 - x2) == 1:
        return False

    # 대각선
    if abs(y1 - y2) == 1 and abs(x1 - x2) == 1:
        if not board[y1][x2] == board[y2][x1] == 'X':
            return False
    # row 같음
    if y1 == y2:
        if not board[y1][(x1 + x2) // 2] == 'X':
            return False
    # col 같음
    if x1 == x2:
        if not board[(y1 + y2) // 2][x1] == 'X':
            return False
    return True


def solution(places):
    ans = []
    for place in places:
        poses = []
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    poses.append((r, c))
        for pos1, pos2 in combinations(poses, 2):
            if not valid(place, pos1, pos2):
                ans.append(0)
                break
        else:
            ans.append(1)
    return ans


if __name__ == "__main__":
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
