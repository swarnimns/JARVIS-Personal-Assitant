from app.core.command import Command
from app.config.parser_config import ACTION_ALIASES, FILLER_WORDS



class CommandParser:

    def parse(self, text: str) -> Command | None:

        text = text.strip().lower()

        words = text.split()

        filtered_words = []   

        for word in words:
            if word not in FILLER_WORDS:
                filtered_words.append(word)

        words = filtered_words

        if len(words) < 2:
            return None

        action = ACTION_ALIASES.get(words[0])

        if action is None:
            return None
        
        target = " ".join(words[1:])

        return Command(
            action=action,
            target=target,
            source="keyboard"
        )