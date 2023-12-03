import sys
import numpy as np
from optparse import OptionParser


def hello_world_with_numpy(argument: str) -> None:
    """
    Prints a greeting and demonstrates a simple NumPy array.

    This function prints "Hello, World!" followed by the received argument.
    It then creates and displays a simple NumPy array.

    Parameters:
    argument (str): The argument to be printed alongside the greeting.
    """

    print("Hello, World!")
    print("Received argument:", argument)

    # Demonstrating a simple NumPy array
    example_array = np.array([1, 2, 3, 4, 5])
    print("Here's a simple NumPy array:", example_array)


def get_args_parser(main_args: bool=True):
    parser = OptionParser()
    parser.add_option("-a", "--argument", dest="argument", 
                      type=str, default="DefaultArgument",
                      help="Provide an argument for the script")
    
    if main_args:
        (options, args) = parser.parse_args()
        return options
    else:
        return parser


if __name__ == "__main__":
    options = get_args_parser()
    hello_world_with_numpy(options.argument)
    print("Done!")
