import webbrowser

from app.config.web_registry import find_website
from app.responses.response import Response


class BrowserHandler:

    def open_website(self, website_name: str):

        website = find_website(website_name)

        if website is None:

            return Response(
                success=False,
                message=f"{website_name} is not registered."
            )

        webbrowser.open(website.url)

        return Response(
            success=True,
            message=f"Opening {website.name}..."
        )