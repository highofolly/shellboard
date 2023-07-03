"""
vishhhl version 0.3
This library makes it easy to create a beautiful visual menu in the console. Based on the VisualMenu library.
Email - sw3atyspace@gmail.com
Discord Server - https://discord.com/invite/jchJKYqNmK
Youtube - https://www.youtube.com/@sw3aty702
"""
from datetime import datetime
from msvcrt import getch
from os import system
import colorama

colorama.init()
cmd_clear = "cls"

class Event:
    def __init__(self,
                 text: str,
                 func,
                 args: list = None,
                 desc: str = None,
                 color: colorama = colorama.Fore.CYAN):
        """
        :param text: Instance name.
        :param func: The function to call.
        :param args: Arguments to pass to the function.
        :param desc: Description of the instance.
        """
        self.text = text
        self.func = func
        self.args = args or []
        self.desc = desc or ""
        self.color = color

    def enable(self):
        """Activates the event."""
        self.func(*self.args)


class Menu(Event):
    def __init__(self,
                 title: str,
                 desc: str = None,
                 opt_list: list = None):
        """
        :param title: Instance name. Displayed on top of all elements.
        :param desc: Description of the instance. Shown above the title.
        """
        super().__init__(title, None, desc)
        self.desc = desc
        self.opt_list = opt_list or []

        self.loop = False

    def changeTitle(self, title):
        """
        :param title: Instance name. Displayed on top of all elements.
        """
        self.text = title

    def changeDesc(self, desc):
        """
        :param desc: Description of the instance. Shown above the title.
        """
        self.desc = desc

    def update(self):
        """A function that runs in a loop."""
        pass

    def enable(self):
        """Activates the menu and creates a loop."""
        self.cursor = 0
        self.loop = True
        cursorKey = ""
        tmpOld = datetime.now()
        while self.loop:
            self.update()
            self._print()
            while True:
                pressedKey = getch()
                try:
                    if pressedKey.decode().isdigit():
                        tmpNow = datetime.now()
                        if (tmpNow - tmpOld).total_seconds() > 0.75 and len(cursorKey) < 4:
                            cursorKey = ""
                        cursorKey += pressedKey.decode()
                        self.cursor = int(cursorKey) - 1
                        if self.cursor >= len(self.opt_list):
                            self.cursor = len(self.opt_list)-1
                        elif self.cursor < 0:
                            self.cursor = 0
                        tmpOld = tmpNow
                        break
                except UnicodeDecodeError:
                    pass

                if pressedKey == b'H':
                    if self.cursor == 0:
                        self.cursor = len(self.opt_list)-1
                    else:
                        self.cursor -= 1
                    break
                elif pressedKey == b'P':
                    if self.cursor == len(self.opt_list)-1:
                        self.cursor = 0
                    else:
                        self.cursor += 1
                    break
                elif pressedKey == b'\r':
                    self.opt_list[self.cursor].enable()
                    break

    def disable(self):
        """Closes the menu loop."""
        self.loop = False

    def _print(self):
        tmp_list = []
        for i in range(len(self.opt_list)):
            if self.cursor == i:
                tmp_list.append(
                    f"{self.opt_list[i].color}> {self.opt_list[i].text}" +
                    (f" {colorama.Fore.LIGHTBLACK_EX}{self.opt_list[i].desc}{colorama.Style.RESET_ALL}"))
            else:
                tmp_list.append(self.opt_list[i].text)

        system(cmd_clear)
        print((f"{self.desc}\n" if self.desc else "") + f"\t{self.text}\n" + "\n".join(tmp_list))

    def addOption(self, *options, index=None):
        """Adds instances to the menu."""
        if index is None:
            if len(self.opt_list):
                index = len(self.opt_list)
            else:
                for i in options:
                    self.opt_list.append(i)
                return
        for i in options:
            self.opt_list.insert(index, i)

    def delOption(self, *options):
        """Removes instances from the menu."""
        try:
            for i in options:
                for uid in range(len(self.opt_list)):
                    if i == self.opt_list[uid]:
                        del self.opt_list[uid]
        except IndexError:
            return 1

class Option(Event):
    def __init__(self,
                 text: str,
                 obj_menu: Menu = None,
                 desc: str = None,
                 color: colorama = colorama.Fore.CYAN):
        """
        :param text: Instance name.
        :param obj_menu: Function to call.
        :param desc: Description of the instance. Displayed to the right of the option.
        :param color: Color of the cursor in the menu.
        """
        color = color if obj_menu else colorama.Fore.LIGHTRED_EX
        super().__init__(text, obj_menu.enable if obj_menu else None, desc=desc, color=color)
