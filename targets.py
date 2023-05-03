from logging import Logger


def logging_target(logger: Logger, message: str, type_logging: str) -> None:
    if type_logging == "debug":
        logger.debug(msg=f"DEBUG:root:{message}")

    if type_logging == "info":
        logger.info(msg=f"INFO:root:{message}")

    if type_logging == "warning":
        logger.warning(msg=f"WARNING:root:{message}")

    if type_logging == "error":
        logger.error(msg=f"ERROR:root:{message}")


def perform_target(logger: Logger, targets_allowed: list, message: str, type_logging: str) -> None:
    target: str
    for target in targets_allowed:
        if target == "console":
            logging_target(logger=logger, message=message, type_logging=type_logging)

        if target == "email":
            logging_target(logger=logger, message=f"Send by email the following message : {message}", type_logging=type_logging)

        if target == "file":
            logging_target(logger=logger, message=f"Write in file the following message : {message}", type_logging=type_logging)

        if target == "server_api":
            logging_target(logger=logger, message=f"Send to server the following message : {message}", type_logging=type_logging)

        if target == "splunk":
            logging_target(logger=logger, message=f"Send to splunk the following message : {message}", type_logging=type_logging)
