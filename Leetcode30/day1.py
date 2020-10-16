test = [1,2,2,3,3]

def solver(input):
    """ 
    Returns entry in array which appears only once while all other entries appear twice

    arg: single array containing int entries

    returns: single int value
    
    """
    x = 0 
    for entry in input:
        x ^= entry
    return x

y = solver(test)
print(y)