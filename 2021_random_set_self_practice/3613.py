"""
input :
long_and_mnemonic_identifier

output :
longAndMnemonicIdentifier
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def validate(text, t):
    if t == 'cpp':
        if '__' in text:
            return False
        if text[0] == '_' or text[-1] == '_':
            return False
        for i in range(len(text)):
            if not (text[i].islower() or text[i] == '_'):
                return False
    elif t == 'java':
        if text[0][0].isupper():
            return False
        for i in range(len(text)):
            if not text[i].isalpha():
                return False
    return True


def cpp_to_java(text):
    new_texts = text.split('_')
    res = [new_texts[0]]
    for i in range(1, len(new_texts)):
        if new_texts[i] == '': continue
        new = new_texts[i][0].upper()
        new += new_texts[i][1:]
        res.append(new)
    return ''.join(res)


def java_to_cpp(text):
    res = []
    for i in range(len(text)):
        if text[i].isupper():
            res.append('_' + text[i].lower())
            continue
        res.append(text[i])
    return ''.join(res)


def change(text, t):
    if t == 'cpp':
        return cpp_to_java(text)
    else:
        return java_to_cpp(text)


if __name__ == "__main__":
    text = input().rstrip()
    t = ""
    if '_' in text:
        t = 'cpp'
    else:
        t = 'java'

    if not validate(text, t):
        print("Error!")
        exit(0)

    print(change(text, t))
