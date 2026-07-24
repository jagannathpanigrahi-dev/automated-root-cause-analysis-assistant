from collections import Counter
from src.parser import LogParser


class LogAnalyzer:

    def __init__(self, logs):
        self.logs = logs

    def analyze(self):

        # Count log levels
        level_counter = Counter()

        # Count error messages
        error_counter = Counter()

        for log in self.logs:

            level_counter[log["level"]] += 1

            if log["level"] in ["ERROR", "CRITICAL"]:
                error_counter[log["message"]] += 1

        print("\n========== LOG ANALYSIS REPORT ==========\n")

        print(f"Total Logs      : {len(self.logs)}")
        print(f"INFO            : {level_counter['INFO']}")
        print(f"WARNING         : {level_counter['WARNING']}")
        print(f"ERROR           : {level_counter['ERROR']}")
        print(f"CRITICAL        : {level_counter['CRITICAL']}")

        print("\n-------- Top Errors --------")

        for error, count in error_counter.most_common():
            print(f"{error} --> {count} time(s)")


if __name__ == "__main__":

    parser = LogParser("logs/sample.log")

    logs = parser.parse_logs()

    analyzer = LogAnalyzer(logs)

    analyzer.analyze()