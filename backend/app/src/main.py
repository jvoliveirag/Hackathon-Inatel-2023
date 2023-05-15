"""
Module containing the "main()" function.
"""

from dependencies import UI_INJECTION


def main() -> None:
    """
    Main Function. This is where the application starts.
    """
    UI_INJECTION.execute()


if __name__ == "__main__":
    main()
