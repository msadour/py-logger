from config import DebugConfig, InfoConfig, WarningConfig, ErrorConfig, MINIMUM_ACCEPTED_LOG_LEVEL
from targets import perform_target


class Logger:

    def __init__(self):
        self.level_severity = MINIMUM_ACCEPTED_LOG_LEVEL

    def debug(self, message: str = "") -> None:
        if self.level_severity >= DebugConfig.LEVEL_SEVERITY:
            print(f"[DEBUG] {message}")
            perform_target(message=message, targets_allowed=DebugConfig.TARGETS_ALLOWED)

    def info(self, message: str = "") -> None:
        if self.level_severity >= InfoConfig.LEVEL_SEVERITY:
            print(f"[INFO] {message}")
            perform_target(message=message, targets_allowed=InfoConfig.TARGETS_ALLOWED)

    def warning(self, message: str = "") -> None:
        if self.level_severity >= WarningConfig.LEVEL_SEVERITY:
            print(f"[WARNING] {message}")
            perform_target(message=message, targets_allowed=WarningConfig.TARGETS_ALLOWED)

    def error(self, message: str = "") -> None:
        if self.level_severity >= ErrorConfig.LEVEL_SEVERITY:
            print(f"[ERROR] {message}")
            perform_target(message=message, targets_allowed=ErrorConfig.TARGETS_ALLOWED)


py_logger: Logger = Logger()
