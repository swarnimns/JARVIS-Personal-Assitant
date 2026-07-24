from app.models.application import Application

APPLICATIONS = {

    "calculator": Application(
        name="calculator",
        path="calc.exe",
        process="CalculatorApp.exe",
        window_process="ApplicationFrameHost.exe",
        aliases=[
            "calc"
        ]
    ),

    "chrome": Application(
        name="chrome",
        path=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        process="chrome.exe",
        aliases=[
            "browser",
            "google chrome"
        ]
    ),

    "explorer": Application(
        name="file explorer",
        path="explorer.exe",
        process="explorer.exe",
        aliases=[
            "explorer",
            "files",
            "file manager"
        ]
    ),

    "notepad": Application(
        name="notepad",
        path="notepad.exe",
        process="notepad.exe",
        aliases=[
            "text editor"
        ]
    ),

    "notion": Application(
        name="notion",
        path=r"C:\Users\Legion\AppData\Local\Programs\Notion\Notion.exe",
        process="Notion.exe",
        aliases=[
            "notes",
            "notion app"
        ]
    ),

    "steam": Application(
        name="steam",
        path=r"C:\Program Files (x86)\Steam\Steam.exe",
        process="steam.exe",
        window_process="steamwebhelper.exe",
        aliases=[
            "games",
            "game launcher"
        ]
    ),

    "visual studio": Application(
        name="visual studio",
        path=r"C:\Program Files\Microsoft Visual Studio\18\Community\Common7\IDE\devenv.exe",
        process="devenv.exe",
        aliases=[
            "vs",
            "visual studio 2022"
        ]
    ),

    "vscode": Application(
        name="vscode",
        path=r"C:\Users\Legion\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        process="Code.exe",
        aliases=[
            "code",
            "vs code",
            "visual studio code",
            "editor"
        ]
    ),

    "word": Application(
        name="word",
        path=r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        process="WINWORD.EXE",
        aliases=[
            "microsoft word",
            "ms word",
            "document"
        ]
    ),

    #"whatsapp": Application(
    #name="whatsapp",
     #   path=r"explorer.exe shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App",
     #   process="WhatsApp.exe",
      #  window_process="ApplicationFrameHost.exe",
      #  aliases=[
       #     "wa",
      #      "whatsapp",
       #     "whats app"
      #  ]
    #),

}


def find_application(name: str):

    name = name.lower().strip()

    # Check application key first
    app = APPLICATIONS.get(name)

    if app is not None:
        return app

    # Check aliases
    for app in APPLICATIONS.values():

        if name in app.aliases:
            return app

    return None