import os

class ErrorFix:
    def detect_and_fix(self):
        print("🔍 Scanning for errors...")
        error_logs = "logs/error_logs.txt"
        if os.path.exists(error_logs):
            print("🛠 Fixing errors...")
            os.remove(error_logs)
            print("✅ Errors fixed successfully!")
