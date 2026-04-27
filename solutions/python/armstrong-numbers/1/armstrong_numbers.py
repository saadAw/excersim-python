def is_armstrong_number(number):
    
    return sum(digit ** len(str(number)) for digit in map(int, str(number))) == number
