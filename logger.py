"""Logging configuration methods."""

import logging


log = logging.getLogger()


def configure_initial_logger() -> None:
    """Configures initial settings for logger.

    Default settings are configured before app settings are loaded. Log level defaults to INFO.
    """

    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("{asctime}s [{levelname}] {message}", style="{")
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)

    log.setLevel("INFO")
