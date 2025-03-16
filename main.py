import time
from self_build import SelfBuild
from error_fix import ErrorFix
from command_center import CommandCenter
from ai_modules.advanced_ai import AdvancedAI

class AI_Autonomous_System:
    def __init__(self):
        self.self_build = SelfBuild()
        self.error_fix = ErrorFix()
        self.command_center = CommandCenter()
        self.advanced_ai = AdvancedAI()

    def run(self):
        print("🚀 AI Autonomous System Started...")
        while True:
            self.command_center.process_commands()
            self.self_build.upgrade_ai()
            self.error_fix.detect_and_fix()
            self.advanced_ai.self_evolve()
            time.sleep(10)

if __name__ == "__main__":
    ai_system = AI_Autonomous_System()
    ai_system.run()
