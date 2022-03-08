from itertools import permutations
import copy


def operate(operator, a, b):
    if operator == '-':
        return a - b
    if operator == '+':
        return a + b
    if operator == '*':
        return a * b


def calc(priority, expr):
    for operator in priority:
        i = 0
        while i < len(expr):
            if expr[i] == operator:
                expr.insert(i - 1, operate(operator, expr.pop(i - 1), expr.pop(i)))
                expr.pop(i)
                i = i - 1
            i += 1
    return expr[0]


def refine_expr(expr):
    operator_set = set()
    ret_expr = []

    pos = 0
    i = 0
    while i != len(expr):
        if expr[i] == '-' or expr[i] == '*' or expr[i] == '+':
            operator_set.add(expr[i])
            ret_expr.append(int(expr[pos: i]))
            ret_expr.append(expr[i])
            pos = i + 1
            i = pos
        i += 1
    ret_expr.append(int(expr[pos: i]))
    return operator_set, ret_expr


def solution(expression):
    operator_set, expression = refine_expr(expression)

    expression_save = copy.deepcopy(expression)
    max_value = -1
    for priority in permutations(operator_set, len(operator_set)):
        max_value = max(max_value, abs(calc(priority, expression)))
        expression = copy.deepcopy(expression_save)
    return max_value


if __name__ == "__main__":
    print(solution("50*6-3*2"))