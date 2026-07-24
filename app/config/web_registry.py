from app.models.website import Website

WEBSITES = {

    "youtube": Website(
        name="YouTube",
        url="https://www.youtube.com",
        aliases=[
            "yt"
        ]
    ),

    "github": Website(
        name="GitHub",
        url="https://github.com",
        aliases=[
            "git"
        ]
    ),

    "chatgpt": Website(
        name="ChatGPT",
        url="https://chat.openai.com",
        aliases=[
            "gpt"
        ]
    ),

    "gmail": Website(
        name="Gmail",
        url="https://mail.google.com",
        aliases=[
            "mail"
        ]
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