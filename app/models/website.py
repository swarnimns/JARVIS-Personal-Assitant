from dataclasses import dataclass


@dataclass
class Website:

    name: str

    url: str

    search_url: str

    aliases: list[str]