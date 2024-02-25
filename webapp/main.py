import logging

# Local imports
import logger


log = logging.getLogger(__name__)


def main() -> None:
    logger.configure_initial_logger()
    log.info("---Pi Camera webapp---")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl-C pressed! Exiting...")
        sys.exit(0)
