class TxtInfo():
    def __init__(self, num, txt_len):
        self.num = num
        self.txt_len = txt_len


txt2TxtInfo = {
    "ze": TxtInfo(num=0, txt_len=4),
    "on": TxtInfo(num=1, txt_len=3),
    "tw": TxtInfo(num=2, txt_len=3),
    "th": TxtInfo(num=3, txt_len=5),
    "fo": TxtInfo(num=4, txt_len=4),
    "fi": TxtInfo(num=5, txt_len=4),
    "si": TxtInfo(num=6, txt_len=3),
    "se": TxtInfo(num=7, txt_len=5),
    "ei": TxtInfo(num=8, txt_len=5),
    "ni": TxtInfo(num=9, txt_len=4),
}


def solution(s):
    ans = ""

    i = 0
    while i < len(s):
        tar_str = s[i]
        if i + 1 < len(s):
            tar_str += s[i + 1]

        if tar_str in txt2TxtInfo:
            ans += str(txt2TxtInfo[tar_str].num)
            i = i + txt2TxtInfo[tar_str].txt_len
            continue

        ans += s[i]
        i += 1

    return ans


if __name__ == "__main__":
    print(solution("23four5six7"))
