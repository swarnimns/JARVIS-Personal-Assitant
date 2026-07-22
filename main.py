from app.core.command_engine import CommandEngine
from app.parser.command_parser import CommandParser


def main():

    print("=================================")
    print("      JARVIS TERMINAL")
    print("=================================")

    parser = CommandParser()
    engine = CommandEngine()

    while True:

        user_input = input("\n> ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        command = parser.parse(user_input)

        if command is None:
            print("I couldn't understand that command.")
            continue

        engine.process(command)


if __name__ == "__main__":
    main()