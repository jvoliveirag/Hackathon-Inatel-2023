"""
Module containing the "main()" function.
"""

from dependencies.dependencies import ui_factory, network_traffic_provider_factory


def main() -> None:
    """
    Main Function. This is where the application starts.
    """
    ui = ui_factory()
    ui.execute()

    network_traffic_provider = network_traffic_provider_factory()
    network_traffic_provider.start()


if __name__ == "__main__":
    main()
