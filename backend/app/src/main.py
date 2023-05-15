"""
Module containing the "main()" function.

DOING: MAKING USE CASE AVAILABLE TO THE UI
"""

# TODO: REMOVE LINE BELOW
import test_functions
from dependencies import UI_INJECTION


def main() -> None:
    """
    Main Function. This is where the application starts.
    """
    print("Hello, World!")
    # test_functions.test_use_case()
    UI_INJECTION.execute()


if __name__ == "__main__":
    main()
