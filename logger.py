from constants import MINIMUM_ACCEPTED_LOG_LEVEL


class Logger:

    def __init__(self, level_severity: int = MINIMUM_ACCEPTED_LOG_LEVEL):
        self.level_severity = level_severity

    def set_level(self, level: int):
        if level <= MINIMUM_ACCEPTED_LOG_LEVEL:
            self.level_severity = level

    def debug(self, message: str = ""):
        breakpoint()
        print(f"[DEBUG] {message}")

    def info(self, message: str = ""):
        if self.level_severity >= 1:
            print(f"[INFO] {message}")

    def warning(self, message: str = ""):
        if self.level_severity >= 2:
            print(f"[WARNING] {message}")

    def error(self, message: str = ""):
        if self.level_severity >= 3:
            print(f"[ERROR] {message}")


py_logger: Logger = Logger()
