"""
Module containing the "main()" function.
"""

from dependencies.dependencies import ui_factory


def main() -> None:
    """
    Main Function. This is where the application starts.
    """
    ui = ui_factory()
    ui.execute()


if __name__ == "__main__":
    main()
