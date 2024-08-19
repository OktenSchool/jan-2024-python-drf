import math
from math import sqrt


def calc(a: int, b: int, operator: str) -> int | float:
    match operator:
        case '+':
            res = math.cos(a)
            return a + b +res
        case '*':
            return a * b + sqrt(a)
        case '/':
            return a / b
