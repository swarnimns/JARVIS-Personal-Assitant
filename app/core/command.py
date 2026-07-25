from dataclasses import dataclass
from typing import Optional


@dataclass
class Command:
    action: str

    target: str

    source: str = "keyboard"

    query: Optional[str] = None 