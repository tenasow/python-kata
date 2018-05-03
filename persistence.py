# Write a function, persistence, that takes in a positive parameter 
# num and returns its multiplicative persistence, which is the
# number of times you must multiply the digits in num until you 
# reach a single digit.

def persistence(n):
    # your code
    counter = 0
    number = n
    while number < 0 or number > 9 :
        counter += 1
        number = reduce(lambda x, y: x*y, [int(d) for d in str(number)])
    return counter