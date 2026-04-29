def value(colors):
    my_dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    number_list = [my_dict[color] for color in colors[:2]]

    strr=""

    for number in number_list:
        strr += str (number)

    return int (strr)
        

