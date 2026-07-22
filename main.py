from app.core.command_engine import CommandEngine
from app.parser.command_parser import CommandParser
from app.responses.response_manager import ResponseManager
from app.responses.response import Response


def main():

    print("=================================")
    print("      JARVIS TERMINAL")
    print("=================================")

    parser = CommandParser()
    engine = CommandEngine()
    response_manager = ResponseManager()

    while True:

        user_input = input("\n> ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        command = parser.parse(user_input)

        if command is None:
            response_manager.show(
                Response(
                    success=False,
                    message="I couldn't understand that command."
                )
            )
            continue

        response = engine.process(command)

        response_manager.show(response)


if __name__ == "__main__":
    main()