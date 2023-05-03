import logging

from config import (
    MINIMUM_ACCEPTED_LOG_LEVEL,
    DebugConfig,
    ErrorConfig,
    InfoConfig,
    WarningConfig,
)
from formater import CustomFormatter
from targets import perform_target


class Logger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(MINIMUM_ACCEPTED_LOG_LEVEL)

        ch = logging.StreamHandler()
        ch.setFormatter(CustomFormatter())

        self.logger.addHandler(ch)

    def debug(self, message: str = "") -> None:
        if self.logger.level >= DebugConfig.LEVEL_SEVERITY:
            perform_target(
                logger=self.logger,
                message=message,
                targets_allowed=DebugConfig.TARGETS_ALLOWED,
                type_logging="debug",
            )

    def info(self, message: str = "") -> None:
        if self.logger.level >= InfoConfig.LEVEL_SEVERITY:
            perform_target(
                logger=self.logger,
                message=message,
                targets_allowed=InfoConfig.TARGETS_ALLOWED,
                type_logging="info",
            )

    def warning(self, message: str = "") -> None:
        if self.logger.level >= WarningConfig.LEVEL_SEVERITY:
            perform_target(
                logger=self.logger,
                message=message,
                targets_allowed=WarningConfig.TARGETS_ALLOWED,
                type_logging="warning",
            )

    def error(self, message: str = "") -> None:
        if self.logger.level >= ErrorConfig.LEVEL_SEVERITY:
            perform_target(
                logger=self.logger,
                message=message,
                targets_allowed=ErrorConfig.TARGETS_ALLOWED,
                type_logging="error",
            )


py_logger: Logger = Logger()
