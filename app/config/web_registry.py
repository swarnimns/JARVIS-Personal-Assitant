from app.models.website import Website

WEBSITES = {

    "google": Website(
        name="google",
        url="https://www.google.com",
        search_url="https://www.google.com/search?q={}",
        aliases=["google", "g"]
    ),

    "youtube": Website(
        name="youtube",
        url="https://www.youtube.com",
        search_url="https://www.youtube.com/results?search_query={}",
        aliases=["youtube", "yt"]
    ),

    "github": Website(
        name="github",
        url="https://github.com",
        search_url="https://github.com/search?q={}",
        aliases=["github", "gh"]
    ),

    #later wwe will use playwright or selenium for browser automation
    "chatgpt": Website(
        name="chatgpt",
        url="https://chat.openai.com",
        search_url="https://chat.openai.com",
        aliases=["chatgpt", "gpt"]
    ),

    "gmail": Website(
        name="gmail",
        url="https://mail.google.com",
        search_url="https://mail.google.com",
        aliases=["gmail", "mail"]
    ),

    

}


def find_website(name: str):

    name = name.lower().strip()

    website = WEBSITES.get(name)

    if website is not None:
        return website

    for website in WEBSITES.values():

        if name in website.aliases:
            return website

    return None