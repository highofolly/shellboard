from msvcrt import getch
from os import system
from time import sleep
import colorama

colorama.init()
clear = "cls"

def init():
    global clear
    import platform
    os = platform.system()
    if os == "Windows":
        clear = "cls"
    elif os == "Linux":
        clear = "clear"
    else:
        class DetectSystemError(LookupError):
            pass

        raise DetectSystemError("Failed to detect system")


class Event:
    def __init__(self, title: str, function, args: list = None, description: str = None, display_descript: bool = True,
                 active: bool = True):
        self.title = title
        self.description = description or ""
        self.display_descript = display_descript
        self.active = active
        self.function = function
        self.args = args or []

    def Enable(self, old=None):
        self.function(*self.args)


class Menu:
    def __init__(self, title: str, description: str = None, display_descript: bool = True, active: bool = True,
                 color: colorama = colorama.Fore.CYAN, events: list = None):
        self.title = title
        self.description = description
        self.display_descript = display_descript
        self.active = active
        self.color = color
        self.events = events or []

        self.enable = False

    def Enable(self, old=None):
        self.cursor = 0
        self.enable = True
        while self.enable:
            self._print(old)
            while True:
                pressedKey = getch()
                if pressedKey == b'H' and self.cursor != 0:
                    self.cursor -= 1
                    break
                elif pressedKey == b'P' and self.cursor != len(self.events):
                    self.cursor += 1
                    break
                elif pressedKey == b'\r':
                    if self.cursor == len(self.events):
                        return
                    elif self.cursor != len(self.events) and self.events[self.cursor].active:
                        self.events[self.cursor].Enable(self.title)
                        break
                sleep(.1)

    def Disable(self):
        self.enable = False

    def _print(self, old):
        tmp = []
        if self.cursor == len(self.events):
            for i in range(len(self.events)):
                tmp.append(self.events[i].title)
            tmp.append(f"{self.color}> Back{colorama.Style.RESET_ALL}")
        else:
            for i in range(len(self.events)):
                if self.cursor == i:
                    tmp.append(
                        f"{self.color if self.events[i].active else colorama.Fore.LIGHTRED_EX}> {self.events[i].title}" + (
                            f" {colorama.Fore.LIGHTBLACK_EX}{self.events[i].description}{colorama.Style.RESET_ALL}" if
                            self.events[i].description and self.events[
                                i].display_descript else colorama.Style.RESET_ALL))
                else:
                    tmp.append(self.events[i].title)
            tmp.append("Back")

        system(clear)
        print((f"{self.description}\n" if self.description else "") + (
            f"\t{old} | {self.title}\n" if old else f"\t{self.title}\n") + "\n".join(tmp))

    def add_event(self, *events):
        for i in events:
            self.events.append(i)

    def del_event(self, *events):
        for i in events:
            for uid in range(len(self.events)):
                if i == self.events[uid]:
                    del self.events[uid]
