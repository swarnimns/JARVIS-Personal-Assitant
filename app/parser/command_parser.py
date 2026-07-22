from app.core.command import Command


class CommandParser:

    def parse(self, text: str) -> Command | None:

        text = text.strip().lower()

        words = text.split()

        if len(words) < 2:
            return None

        action = words[0]
        target = " ".join(words[1:])

        return Command(
            action=action,
            target=target,
            source="keyboard"
        )