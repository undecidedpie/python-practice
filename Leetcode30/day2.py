import math

def digit_sum(n):
    """
    helper method to compute sum of power of digits and return it
    
    note: upper bound of value returned by this is 9^2 * 10 = 810, since there can only be 10 unique digits
    """
    sum = 0 

    #remember that python doesn't default on floor division! (Got stuck on)
    while n != 0:
        digit = n % 10
        sum +=  (digit * digit)
        n //= 10
    return sum

def solution(input):
    """
    first checks if number is one, otherwise
    then checks if number has been visited, if so then terminates program since loop
    if the number has not been seen before, then adds to set() and continues
    """

    visited_number = set()

    #check: are sets ordered in python?
    while(True):
        if input == 1:
            return True
        
        if input in visited_number:
            return False

        visited_number.add(input)
        input = digit_sum(input)

        print(visited_number)

#test with provided number 19, should work
print(solution(19))