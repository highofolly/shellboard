"""
This is a code example showing the main features of the library. 
"""

from vishhhl.addons.Menu import *
import colorama

clrm = colorama.Fore


class Menu(mOption):
    login = None

    def __init__(self,
                 title: str = None,
                 desc: str = None,
                 text: str = None,
                 comment: str = None):
        self.org_title = title
        desc = desc if desc else f"This is the {colorama.Fore.MAGENTA}vishhhl{colorama.Style.RESET_ALL}!"
        text = text if text else title
        comment = comment if comment else desc

        super().__init__(text, self, comment, title=title, desc=desc)
        self.symbol = "\n"

    def update(self):
        if self.login:
            self.changeTitle(f"{self.org_title} | Authorized: {self.login}")
        else:
            self.changeTitle(self.org_title)


class clsSetting(Menu):
    def __init__(self):
        super().__init__("Settings",
                         comment="Customize button color")
        self.addOption(mLink("Red", link=self.changeColor, args=[0]),
                       mLink("Green", link=self.changeColor, args=[1]),
                       mLink("Cyan", link=self.changeColor, args=[2]),
                       mLink("Back", link=self.disable))

    def changeColor(self, index):
        for i in menMain.func_list + self.func_list:
            i.color = (clrm.RED, clrm.GREEN, clrm.CYAN)[index]

    def on_selected(self):
        ret = super().on_selected()
        # input(ret)
        return ret


class clsMain(Menu):
    def __init__(self):
        super().__init__("Menu")
        self.optLogIn = mLink(text="Log in", link=self.fLogIn, comment="Log in to continue")
        self.optLogOut = mLink(text="Log out", link=self.fLogOut, comment="Log out from system")

        menSetting = clsSetting()
        eveInfo = mLink(text="Information", link=input,
                        args=["\nEmail - sw3atyspace@gmail.com "
                              "\nYouTube - https://www.youtube.com/@sw3aty702 "
                              "\nDiscord Server - https://discord.gg/jchJKYqNmK"])
        eveExit = mLink(text="Exit", link=self.fQuit)

        self.addOption(self.optLogIn, menSetting, eveInfo, eveExit)

    def fLogIn(self):
        Menu.login = input("\nEnter your name: ")
        self.delOptionByIndex(index=0)
        self.addOptionByIndex(self.optLogOut, index=0)

    def fLogOut(self):
        Menu.login = None
        self.delOptionByIndex(index=0)
        self.addOptionByIndex(self.optLogIn, index=0)

    def fQuit(self):
        ans = input("\nDo you really want to go out (Y/n) ").upper()
        if ans == "Y":
            exit()


menMain = clsMain()
menMain.enable()
