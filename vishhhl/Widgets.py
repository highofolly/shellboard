"""
This is a code example showing the main features of the library. 
"""
from vishhhl_v5.addons.Menu import *


class palette:
    pass


for i in colorama.Fore.__dict__.keys():
    if i not in ["RESET", "BLACK"]:
        if i[:5] == "LIGHT":
            setattr(palette, f"{i[:5]}_{i[5:-3]}", getattr(colorama.Fore, i))
        else:
            setattr(palette, i, getattr(colorama.Fore, i))


def findByIndex(index):
    return list({i for i in palette.__dict__ if palette.__dict__[i] == index})[0]


class Menu(mOption, mLayer):
    def __init__(self,
                 text: str,
                 title: str,
                 desc: str = None,
                 second: str = None):
        super().__init__(text, self, desc)
        mLayer.__init__(self, title, second)
        self.symbol = "\n"


class clsSetting(Menu):
    class lColor(mLink):
        def __init__(self, color: palette.WHITE):
            super().__init__(link=self.changeColor, color=color, text=findByIndex(color).title())

        def changeColor(self):
            for i in menMain.widget_list:
                i.color = self.color

    def __init__(self):
        super().__init__("Settings", title="Settings", second="Customize button color")
        self.algn_len = 15

        for i in palette.__dict__.keys():
            if i[0] != "_":
                eval(f"self.addWidget(self.lColor(color=palette.{i}))")
        self.addWidget(mLink("Back", link=self.disable))
        self.colm_len = len(self.widget_list) // 3


class clsMain(Menu):
    def __init__(self):
        super().__init__(str(), title="Menu")
        self.optLogIn = mLink(text="Log in", desc="Log in to continue", link=self.fLogIn)
        self.optLogOut = mLink(text="Log out", desc="Log out from system", link=self.fLogOut)

        menSetting = clsSetting()
        eveInfo = mLink(text="Information", link=input,
                        args=["\nEmail - sw3atyspace@gmail.com "
                              "\nYouTube - https://www.youtube.com/@sw3aty702 "
                              "\nDiscord Server - https://discord.gg/jchJKYqNmK"])
        eveExit = mLink(text="Exit", link=self.fQuit)

        self.addWidget(self.optLogIn, menSetting, eveInfo, eveExit)

    def fLogIn(self):
        self.changeSecond(input("\nEnter your name: "))
        self.delWidgetByIndex(0)
        self.addOptionByIndex(self.optLogOut, index=0)

    def fLogOut(self):
        self.changeSecond(None)
        self.delWidgetByIndex(0)
        self.addOptionByIndex(self.optLogIn, index=0)

    def fQuit(self):
        ans = input("\nDo you really want to go out (Y/n) ").upper()
        if ans == "Y":
            exit()


menMain = clsMain()
menMain.enable()
