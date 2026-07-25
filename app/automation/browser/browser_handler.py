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

#------------------------------------------------------------------------------

    def search(self, website_name: str, query: str):

        website = find_website(website_name)

        #website not found
        if website is None:
            return Response(
                success=False,
                message=f"{website_name} is not registered."
            )

        #no search query -> just open  the website
        if not query or not query.strip():

            webbrowser.open(website.url)

            return Response(
                success=True,
                message=f"Searching {website.name} for '{query}'..."
            )

        #Remove extra spaces
        query= query.strip()

        #Build the search URL
        search_url= website.search_url.format(query)

        #Open search results
        webbrowser.open(search_url)

        return Response(
            success=True,
            message=f"Searching {website.name} for '{query}'..."
        )