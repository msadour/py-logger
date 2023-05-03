from constants import ERROR, WARNING, INFO, DEBUG


class DebugConfig:

    LEVEL_SEVERITY = DEBUG
    TARGETS_ALLOWED = []


class InfoConfig:

    LEVEL_SEVERITY = INFO
    TARGETS_ALLOWED = [
        "email",
        "file",
        "server_api",
        "splunk",
    ]


class WarningConfig:

    LEVEL_SEVERITY = WARNING
    TARGETS_ALLOWED = [
        "file",
    ]


class ErrorConfig:

    LEVEL_SEVERITY = ERROR
    TARGETS_ALLOWED = [
        "file",
        "splunk",
    ]


MINIMUM_ACCEPTED_LOG_LEVEL: int = DebugConfig.LEVEL_SEVERITY
