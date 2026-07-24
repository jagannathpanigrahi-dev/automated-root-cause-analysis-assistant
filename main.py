from src.parser import LogParser
from src.analyzer import LogAnalyzer
from src.root_cause import RootCauseAnalyzer
import subprocess
import os


LOG_FILE = os.path.join("logs", "sample.log")


def parse_logs():
    parser = LogParser(LOG_FILE)
    return parser.parse_logs()


while True:

    print("\n" + "=" * 55)
    print(" AUTOMATED ROOT CAUSE ANALYSIS ASSISTANT ")
    print("=" * 55)
    print("1. Parse Log File")
    print("2. Analyze Logs")
    print("3. Root Cause Analysis")
    print("4. Train AI Model")
    print("5. Predict Root Cause (AI)")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        logs = parse_logs()

        print("\nTotal Logs :", len(logs))

        for log in logs:
            print(log)

    elif choice == "2":

        logs = parse_logs()

        analyzer = LogAnalyzer(logs)

        analyzer.analyze()

    elif choice == "3":

        logs = parse_logs()

        root = RootCauseAnalyzer(logs)

        root.analyze()

    elif choice == "4":

        subprocess.run(["python", "src/train_model.py"])

    elif choice == "5":

        subprocess.run(["python", "src/predict.py"])

    elif choice == "6":

        print("\nThank You!")
        break

    else:

        print("\nInvalid Choice")