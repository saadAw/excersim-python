def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    divider_sum = 0

    if number < 1: 
        raise ValueError("Classification is only possible for positive integers.")
    
    if number == 1:
        return "deficient"

    for x in range(1, (number//2) + 1):
        
        if number % x != 0: 
            continue
        divider_sum += x
    
    if divider_sum > number:
        return "abundant"
    
    if divider_sum < number:
        return "deficient"
    
    return "perfect"
