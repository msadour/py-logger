import logging


class CustomFormatter(logging.Formatter):

    grey: str = "\x1b[38;22m"
    yellow: str = "\x1b[33;20m"
    red: str = "\x1b[31;20m"
    bold_red: str = "\x1b[31;1m"
    reset: str = "\x1b[0m"
    format: str = "%(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS: dict = {
        logging.DEBUG: grey + format + grey,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt: str = self.FORMATS.get(record.levelno)
        formatter: logging.Formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
