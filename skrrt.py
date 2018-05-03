def persistence(n):
    # your code
    counter = 0
    number = n
    while number < 0 or number > 9 :
        counter += 1
        number = reduce(lambda x, y: x*y, [int(d) for d in str(number)])
    return counter