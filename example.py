"""
This is a code example showing the main features of the library. 
"""

from vishhhl import Menu, Option, Event, colorama, version
clrm = colorama.Fore

login = None

class clsSetting(Menu):
    def __init__(self):
        super().__init__(f"Settings", desc=f"This is the {colorama.Fore.MAGENTA}vishhhl{colorama.Style.RESET_ALL} of version {version}!")
        self.option = Option("Settings", obj_menu=self, desc="Customize button color")
        self.addOption(Event("Red", func=self.changeColor, args=[0]),
                       Event("Green", func=self.changeColor, args=[1]),
                       Event("Cyan", func=self.changeColor, args=[2]),
                       Event("Back", func=self.disable))
        self.option_type = [r"\optText", r"\optColor > \optText < \optDesc \clrm.RESET"]

    def changeColor(self, index):
        for i in menMain.opt_list + self.opt_list:
            i.color = (clrm.RED, clrm.GREEN, clrm.CYAN)[index]

    def update(self):
        if login:
            self.changeTitle(f"Settings | Authorized: {login}")
        else:
            self.changeTitle(f"Settings")

class clsMain(Menu):
    def __init__(self):
        super().__init__("Menu", desc=f"This is the {colorama.Fore.MAGENTA}vishhhl{colorama.Style.RESET_ALL} of version {version}!")
        self.optLogIn = Event(text="Log in", func=self.fLogIn, desc="Log in to continue")
        self.optLogOut = Event(text="Log out", func=self.fLogOut, desc="Log out from system")

        menSetting = clsSetting()

        eveInfo = Event(text="Information", func=input,
                        args=["\nEmail - sw3atyspace@gmail.com "
                              "\nYouTube - https://www.youtube.com/@sw3aty702 "
                              "\nDiscord Server - https://discord.gg/jchJKYqNmK"])
        eveExit = Event(text="Exit", func=self.f_quit)

        self.addOption(self.optLogIn, menSetting.option, eveInfo, eveExit)

    def update(self):
        if login:
            self.changeTitle(f"Menu | Authorized: {login}")
        else:
            self.changeTitle(f"Menu")

    def fLogIn(self):
        global login
        login = input("\nEnter your name: ")
        self.delOption(self.optLogIn)
        self.addOption(self.optLogOut, index=0)

    def fLogOut(self):
        global login
        login = None
        self.delOption(self.optLogOut)
        self.addOption(self.optLogIn, index=0)

    def f_quit(self):
        ans = input("\nDo you really want to go out (Y/n) ").upper()
        if ans == "Y":
            exit()


menMain = clsMain()
menMain.enable()
