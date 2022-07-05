from test_framework import generic_test


def evaluate(expression: str) -> int:
    # loop for str 
    # if found + - / y, pop two item then do arithmetics op
    # else push into stack
    result = []
    OPERATION={
        '+':lambda y,x:x+y,
        '-':lambda y,x:x-y,
        '*':lambda y,x:x*y,
        '/':lambda y,x:int(x/y)
    }
    for item in expression.split(','):
        if item in OPERATION:
            result.append(OPERATION[item](result.pop(),result.pop()))
        else:
            result.append(int(item))
    return result[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
