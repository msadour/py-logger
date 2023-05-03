from constants import MINIMUM_ACCEPTED_LOG_LEVEL
from targets import perform_target


class Logger:

    def __init__(self, level_severity: int = MINIMUM_ACCEPTED_LOG_LEVEL):
        self.level_severity = level_severity

    def set_level(self, level: int) -> None:
        if level <= MINIMUM_ACCEPTED_LOG_LEVEL:
            self.level_severity = level

    def debug(self, message: str = "") -> None:
        print(f"[DEBUG] {message}")
        perform_target(message)

    def info(self, message: str = "") -> None:
        if self.level_severity >= 1:
            print(f"[INFO] {message}")
            perform_target(message)

    def warning(self, message: str = "") -> None:
        if self.level_severity >= 2:
            print(f"[WARNING] {message}")
            perform_target(message)

    def error(self, message: str = "") -> None:
        if self.level_severity >= 3:
            print(f"[ERROR] {message}")
            perform_target(message)


py_logger: Logger = Logger()
