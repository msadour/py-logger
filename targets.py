def send_email(message: str) -> None:
    print(f"Send by email the following message : {message}")


def write_in_file(message: str) -> None:
    print(f"Write in file the following message : {message}")


def send_to_server_api(message: str) -> None:
    print(f"Send to server the following message : {message}")


def send_to_splunk(message: str) -> None:
    print(f"Send to splunk the following message : {message}")


def perform_target(targets_allowed: list, message: str) -> None:
    target: str
    for target in targets_allowed:
        if target == "email":
            send_email(message=message)

        if target == "file":
            write_in_file(message=message)

        if target == "server_api":
            send_to_server_api(message=message)

        if target == "splunk":
            send_to_splunk(message=message)
