import logging
import sys

from config import DebugConfig, InfoConfig, WarningConfig, ErrorConfig, MINIMUM_ACCEPTED_LOG_LEVEL
from targets import perform_target


class Logger:

    def __init__(self):
        self.level_severity = MINIMUM_ACCEPTED_LOG_LEVEL
        self.logger = logging.getLogger()
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        self.logger.setLevel(MINIMUM_ACCEPTED_LOG_LEVEL)

    def debug(self, message: str = "") -> None:
        if self.logger.level >= DebugConfig.LEVEL_SEVERITY:
            perform_target(logger=self.logger, message=message, targets_allowed=DebugConfig.TARGETS_ALLOWED, type_logging="debug")

    def info(self, message: str = "") -> None:
        if self.logger.level >= InfoConfig.LEVEL_SEVERITY:
            perform_target(logger=self.logger, message=message, targets_allowed=InfoConfig.TARGETS_ALLOWED, type_logging="info")

    def warning(self, message: str = "") -> None:
        if self.logger.level >= WarningConfig.LEVEL_SEVERITY:
            perform_target(logger=self.logger, message=message, targets_allowed=WarningConfig.TARGETS_ALLOWED, type_logging="warning")

    def error(self, message: str = "") -> None:
        if self.logger.level >= ErrorConfig.LEVEL_SEVERITY:
            perform_target(logger=self.logger, message=message, targets_allowed=ErrorConfig.TARGETS_ALLOWED, type_logging="error")


py_logger: Logger = Logger()
