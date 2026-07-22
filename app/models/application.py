from dataclasses import dataclass
from typing import List


@dataclass
class Application:

    name: str

    path: str

    process: str

    aliases: List[str]