import math

def score(x, y):

    distance = (x ** 2 + y ** 2) ** 0.5
    
    rules = [
        (1, 10),
        (5, 5),
        (10, 1)
    ]

    for radius, points in rules:
        if radius >= distance:
            return points
        
    return 0