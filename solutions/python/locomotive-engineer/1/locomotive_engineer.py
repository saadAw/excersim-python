"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """

    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    w1, w2, w3, *allother = each_wagons_id

    *combined_list, = w3, *missing_wagons, *allother,  w1, w2

    return combined_list


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    return {**route, "stops": list(kwargs.values())}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """

    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    different_colors = []

    for row in wagons_rows:
        for color in row:
            if color[1] not in different_colors:
                different_colors.append(color[1])

    color_counter = {color: 0 for color in different_colors}
    column_counter = {color: idx for idx, color in enumerate(different_colors)}
    

    new_list = [[None, None, None] for _ in range(3)]

    for row in wagons_rows:
        for color in row:
            new_list[color_counter[color[1]]][column_counter[color[1]]] = color
            color_counter[color[1]] += 1
            
    
    return new_list
                
    
