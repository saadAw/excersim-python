"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPERATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preperation time depending on the number of layers.

    :param number_of_layers: int - how many layers the lasagna.
    :return: int - total preperation time (in minutes).

    Function that takes the number of layers and multiplies it by the preperation time for each layer and returns the total prep      time in minutes.
    """
    return number_of_layers*PREPERATION_TIME

#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time (in minutes).

    :param number_of_layers: int - how many layers the lasagna.
    :param elapsed_bake_time: int - the number how much time the lasagna has passed (in minutes) baking in the oven
    :return: int - total time in the kitchen (in minutes)

    Function that takes the number of layers and the elapsed bake time returns the total time spent in the kitchen in minutes.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
