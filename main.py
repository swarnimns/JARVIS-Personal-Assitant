from app.core.command import Command
from app.core.command_engine import CommandEngine


def main():

    print("Starting Jarvis...\n")

    engine = CommandEngine()

    command = Command(
        action="open",
        target="Chrome"
    )

    engine.process(command)


if __name__ == "__main__":
    main()