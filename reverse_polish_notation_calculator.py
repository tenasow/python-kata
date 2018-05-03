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
    # check each character in array if it's a mathematical notation and grab
    # the 2 values in array before it, if both of them can be converted to
    # floats calculate it, remove old notation and replace old numbers with
    # the new one. Repeat untill all are gone.... not at all optimized... :(
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
    if output == 0:
        return output
    # if any of symbols in output do it again!
    while any(x in ['+', '/', '-', '*'] for x in output):
        output = rpnc(output)
    # if greater amount of numbers than symbols parse last number.
    if len(output) > 1:
        return float(output[-1])
    # return result from calculation
    return float(output[-1])
    