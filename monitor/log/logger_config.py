import logging
import sys

class CustomFormatter(logging.Formatter):

    yellow = "\x1b[33;20m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.WARNING: yellow + "%(levelname)s %(asctime)s %(message)s" + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logger():
    try:
        # Create a custom logger
        logger = logging.getLogger("monit_logger")
        logger.setLevel(logging.DEBUG)  # This needs to be DEBUG to capture all levels of logs

        # Create handlers
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('./var/log/monit_log')
        c_handler.setLevel(logging.DEBUG)  # Set to DEBUG to ensure all levels are logged to console
        f_handler.setLevel(logging.DEBUG)  # Set to DEBUG to ensure all levels are logged to file

        # Create formatters and add it to handlers
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        c_handler.setFormatter(CustomFormatter())
        f_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        sys.exit(1)
    return logger