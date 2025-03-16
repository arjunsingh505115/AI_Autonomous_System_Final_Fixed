import os

class CommandCenter:
    INBOX_FILE = "inbox/commands.txt"

    def process_commands(self):
        if os.path.exists(self.INBOX_FILE):
            with open(self.INBOX_FILE, "r") as f:
                commands = f.readlines()

            if commands:
                for command in commands:
                    print(f"📥 Executing: {command.strip()}")
                os.remove(self.INBOX_FILE)
