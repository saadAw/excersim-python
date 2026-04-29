def label(colors):
    
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

    
    number = my_dict[colors[0]] * 10 + my_dict[colors[1]]

    exp = my_dict[colors[2]]

    number = number * 10 ** exp
    
    einheiten = ["ohms", "kiloohms", "megaohms", "gigaohms"]

    if number == 0:
        return "0 ohms"
    
    einheiten_index = 0

    while(number%1000==0 and number > 0):
        number = number // 1000
        einheiten_index += 1


    return str(number) + " " +einheiten[einheiten_index]

