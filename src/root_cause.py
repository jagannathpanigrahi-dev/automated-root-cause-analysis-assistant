from src.parser import LogParser


class RootCauseAnalyzer:

    def __init__(self, logs):
        self.logs = logs

        self.knowledge_base = {

            "Database Connection Failed": {
                "cause": "Database server is unavailable.",
                "solution": "Restart the database service and verify database credentials."
            },

            "Database Service Stopped": {
                "cause": "Database service crashed.",
                "solution": "Restart the database service immediately."
            },

            "Network Timeout": {
                "cause": "Poor network connectivity.",
                "solution": "Check internet connection and firewall settings."
            },

            "Permission Denied": {
                "cause": "User does not have required permissions.",
                "solution": "Verify user permissions or run as administrator."
            },

            "File Not Found": {
                "cause": "Required file is missing.",
                "solution": "Check the file path and restore the missing file."
            },

            "Authentication Failed": {
                "cause": "Invalid username or password.",
                "solution": "Verify login credentials."
            },

            "Invalid API Key": {
                "cause": "API key is incorrect or expired.",
                "solution": "Generate a new API key."
            },

            "SSL Certificate Expired": {
                "cause": "SSL certificate has expired.",
                "solution": "Renew and install a new SSL certificate."
            },

            "Email Service Unreachable": {
                "cause": "Mail server is down.",
                "solution": "Check SMTP server status."
            },

            "Server Shutdown Unexpectedly": {
                "cause": "Unexpected system crash.",
                "solution": "Check power supply and system logs."
            }

        }

    def analyze(self):

        print("\n========== ROOT CAUSE ANALYSIS ==========\n")

        for log in self.logs:

            if log["level"] not in ["ERROR", "CRITICAL"]:
                continue

            message = log["message"]

            found = False

            for keyword in self.knowledge_base:

                if keyword in message:

                    print("-------------------------------------")
                    print("Error      :", message)
                    print("Cause      :", self.knowledge_base[keyword]["cause"])
                    print("Solution   :", self.knowledge_base[keyword]["solution"])
                    print()

                    found = True
                    break

            if not found:

                print("-------------------------------------")
                print("Error      :", message)
                print("Cause      : Unknown")
                print("Solution   : Check the log manually.")
                print()


if __name__ == "__main__":

    parser = LogParser("logs/sample.log")

    logs = parser.parse_logs()

    analyzer = RootCauseAnalyzer(logs)

    analyzer.analyze()