import re


class LogParser:
    def __init__(self, log_file):
        self.log_file = log_file

    def parse_logs(self):
        """
        Reads the log file and returns a list of dictionaries.
        """

        logs = []

        pattern = re.compile(
            r"^(?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+"
            r"(?P<level>INFO|WARNING|ERROR|CRITICAL)\s+"
            r"(?P<message>.+)$"
        )

        with open(self.log_file, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                match = pattern.match(line)

                if match:

                    logs.append(
                        {
                            "timestamp": match.group("timestamp"),
                            "level": match.group("level"),
                            "message": match.group("message")
                        }
                    )

        return logs


if __name__ == "__main__":

    parser = LogParser("logs/sample.log")

    log_data = parser.parse_logs()

    print("Total Logs :", len(log_data))
    print()

    for log in log_data:
        print(log)