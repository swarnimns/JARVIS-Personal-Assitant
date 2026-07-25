from app.core.command import Command
from app.config.parser_config import ACTION_ALIASES, FILLER_WORDS
from app.config.web_registry import find_website


class CommandParser:

    def parse(self, text: str) -> Command | None:

        # Normalize user input
        text = text.strip().lower()

        # Split into individual words
        words = text.split()

        # Remove filler words
        filtered_words = []

        for word in words:
            if word not in FILLER_WORDS:
                filtered_words.append(word)

        words = filtered_words

        # Need at least an action and one argument
        if len(words) < 2:
            return None

        # Convert aliases (launch -> open, start -> open, etc.)
        action = ACTION_ALIASES.get(words[0])

        if action is None:
            return None

        # ==========================================================
        # SEARCH COMMANDS
        #
        # Examples:
        #
        # search python decorators
        # search google python decorators
        # search youtube lofi music
        # search github psutil
        # search youtube
        # ==========================================================

        if action == "search":

            website = find_website(words[1])

            # User specified a registered website
            if website is not None:

                target = website.name

                # Example:
                # search youtube
                if len(words) == 2:
                    query = None

                # Example:
                # search youtube lofi music
                else:
                    query = " ".join(words[2:])

            # No website specified -> default to Google
            else:

                target = "google"
                query = " ".join(words[1:])

            return Command(
                action="search",
                target=target,
                query=query,
                source="keyboard",
            )

        # ==========================================================
        # OPEN / CLOSE COMMANDS
        #
        # Examples:
        #
        # open chrome
        # close vscode
        # open visual studio
        # ==========================================================

        target = " ".join(words[1:])

        return Command(
            action=action,
            target=target,
            source="keyboard",
        )