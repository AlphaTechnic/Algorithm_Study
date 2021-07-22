"""
input :
(()[[]])([])

output :
28
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


paren_dic = {'(': ')', '[': ']'}


def is_valid():
    st = list()
    for ch in text:
        if ch in paren_dic:
            st.append(ch)
        else:  # ch가 닫는 괄호라면,
            if len(st) == 0: return False
            if ch != paren_dic[st.pop()]: return False

    if len(st) != 0: return False
    return True


def get_val():
    st = list()
    for ch in text:
        if ch in paren_dic:
            st.append(ch)
        else:  # ch가 닫는 괄호라면,
            if ch == ')':
                tot = 0
                while True:
                    ele = st.pop()
                    if ele == '(':
                        break
                    tot += ele
                score = max(tot, 1) * 2
                st.append(score)
            else:  # ch == ']'
                tot = 0
                while True:
                    ele = st.pop()
                    if ele == '[':
                        break
                    tot += ele
                score = max(tot, 1) * 3
                st.append(score)

    return sum(st)


if __name__ == "__main__":
    text = input().rstrip()
    if not is_valid():
        print(0)
        exit()

    print(get_val())
