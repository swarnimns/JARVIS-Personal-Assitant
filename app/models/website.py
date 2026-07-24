from dataclasses import dataclass


@dataclass
class Website:

    name: str

    url: str

    aliases: list[str]