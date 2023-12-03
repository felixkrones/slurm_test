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


def get_args_parser(main_args=True):
    parser = OptionParser()
    parser.add_option("-a", "--argument", dest="argument", 
                      type="string", default="DefaultArgument",
                      help="Provide an argument for the script")
    
    (options, args) = parser.parse_args(args=main_args and sys.argv[1:] or [])
    return options


if __name__ == "__main__":
    import sys
    options = get_args_parser()
    hello_world_with_numpy(options.argument)
