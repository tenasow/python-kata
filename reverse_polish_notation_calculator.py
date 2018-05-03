# please lord have mercy upon my soul for this abomination.
# to briefly explain, loops through for each mathematical symbol * / - +
# calculates that part and substitutes it with the result and keeps going
# untill nothing is left.

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def rpnc(expr):
    if not expr or expr[0] == '':
        return 0
    newStr = expr
    while set(['+', '/', '-', '*']).issubset(newStr):
        for i, item in enumerate(newStr):
            if item == '+' and isfloat(newStr[i-2]) and isfloat(newStr[i-1]):
                newStr[i-1] = float(newStr[i-2]) + float(newStr[i-1])
                del newStr[i]
                del newStr[i-2]
        for i, item in enumerate(newStr):
            if item == '*' and isfloat(newStr[i-2]) and isfloat(newStr[i-1]):
                newStr[i-1] = float(newStr[i-2]) * float(newStr[i-1])
                del newStr[i]
                del newStr[i-2]
        for i, item in enumerate(newStr):
            if item == '-' and isfloat(newStr[i-2]) and isfloat(newStr[i-1]):
                newStr[i-1] = float(newStr[i-2]) - float(newStr[i-1])
                del newStr[i]
                del newStr[i-2]
        for i, item in enumerate(newStr):
            if item == '/' and isfloat(newStr[i-2]) and isfloat(newStr[i-1]):
                newStr[i-1] = float(newStr[i-2]) / float(newStr[i-1])
                del newStr[i]
                del newStr[i-2]
    return newStr

def calc(expr):
    expr = expr.split(' ')
    output = rpnc(expr)
    print(output)
    return output