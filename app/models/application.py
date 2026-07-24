from dataclasses import dataclass
from typing import List


@dataclass
class Application:

    name: str

    path: str

    # Process used to detect whether the app is running
    process: str

    # Process that owns the visible window
    # If not specified, we'll use `process`
    window_process: str | None = None

    aliases: List[str] = None

    def __post_init__(self):

        if self.window_process is None:
            self.window_process = self.process

        if self.aliases is None:
            self.aliases = []