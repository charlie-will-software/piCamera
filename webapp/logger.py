"""Logging configuration methods."""

import logging


SUPPORTED_LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR")


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


def set_log_level(level: str) -> None:
    level = level.upper()
    if level not in SUPPORTED_LOG_LEVELS:
        raise ValueError(f"Loge level {level} not supported")

    log.setLevel(level)
