import sys
sys.stdin = open("input.txt", "r")

flag = 0
while True:
    string = input()
    if string == '.':
        break
    parenthesis = []
    for char in string:
        if char == '(' or char == '[':
            parenthesis.append(char)
        elif char == ')' or char == ']':
            if len(parenthesis) != 0:
                open = parenthesis.pop()
            else:
                print("no")
                flag = 1
                break

            if ((open == '(' and char == ')') or (open == '[' and char == ']')) is False:
                print('no')
                flag = 1
                break
    if flag == 0:
        if len(parenthesis) != 0:
            print('no')
        else:
            print('yes')
    flag = 0
