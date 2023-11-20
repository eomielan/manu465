import os
import time

# Constants
YELLOW_CODE = "\033[93m"
RED_CODE = "\033[91m"
GREEN_CODE = "\033[92m"
RESET_CODE = "\033[0m"
STRING_LENGTH = 8
SLEEP_TIME = 2  # seconds


def generate(length: int) -> str:
    """Generate new random alphanumeric string of given length.

    Args:
        length (int): The length of the string to generate.

    Returns:
        str: The randomly generated string.
    """
    # TODO: Implement this function
    return ""


def print_diff(expected: str, actual: str) -> None:
    """Print the difference between the expected and actual strings.

    Args:
        expected (str): The expected string.
        actual (str): The actual string.
    """
    print("Expected: " + YELLOW_CODE + expected + RESET_CODE)
    print("Actual:   ", end="")

    for i in range(min(len(expected), len(actual))):
        if expected[i] == actual[i]:
            print(GREEN_CODE + actual[i] + RESET_CODE, end="")
        else:
            print(RED_CODE + actual[i] + RESET_CODE, end="")

    # Print any remaining characters in the input string, if any are present
    if len(actual) > len(expected):
        print(RED_CODE + actual[len(expected):] + RESET_CODE, end="")


def main():
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen

    while True:
        input("Press enter to generate a new string")
        os.system("cls" if os.name == "nt" else "clear")

        expected = generate(STRING_LENGTH)
        print(YELLOW_CODE + expected + RESET_CODE)

        time.sleep(SLEEP_TIME)
        os.system("cls" if os.name == "nt" else "clear")

        actual = input("Enter the string: ")
        print("")
        print_diff(expected, actual)

        print("\n")


if __name__ == "__main__":
    main()
