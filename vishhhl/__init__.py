"""
vishhhl version 0.3.1
This library makes it easy to create a beautiful visual menu in the console. Based on the VisualMenu library.
Email - sw3atyspace@gmail.com
Discord Server - https://discord.com/invite/jchJKYqNmK
Youtube - https://www.youtube.com/@sw3aty702
"""

version = "0.3.1"

import numpy as np
from datetime import datetime
from msvcrt import getch
from os import system
import colorama

colorama.init()
cmd_clear = "cls"


class Layer:
    def __init__(self,
                 title: str,
                 desc: str = None,
                 opt_list: list = None):
        """
        :param title: Instance name. Displayed on top of all elements.
        :param desc: Description of the instance. Shown above the title.
        """
        self.title = title
        self.desc = desc or ""
        self.opt_list = opt_list or []

        self.title_type = r"\desc\n\t\title"
        self.option_type = [r"\optText", r"\optColor > \optText \clrm.LIGHTBLACK_EX \optDesc \clrm.RESET"]
        self.max_items_column = 0
        self.key_hook = True

        self.loop = False
        self.tmpOld = datetime.now()
        self.cursor = 0
        self.cursorKey = ""

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

    def delOptionByIndex(self, index):
        """Removes instances from a menu by index."""
        try:
            del self.opt_list[index]
        except IndexError:
            return 1

    def update(self):
        """A function that runs in a loop."""
        pass

    def enable(self):
        """Opens the loop."""
        self.loop = True
        self.mainLoop()

    def disable(self):
        """Closes the menu loop."""
        self.loop = False

    def mainLoop(self):
        while self.loop:
            self.update()
            self.printManager()
            while self.hookManager():
                pass

    def decodeManager(self, string, obj_option=None):
        string = string.replace(r"\desc", self.desc)
        string = string.replace(r"\title", self.title)
        if obj_option:
            string = string.replace(r"\optColor", obj_option.color)
            string = string.replace(r"\optText", obj_option.text)
            string = string.replace(r"\optDesc", obj_option.desc)
            string = string.replace(r"\clrm.LIGHTBLACK_EX", colorama.Fore.LIGHTBLACK_EX)
            string = string.replace(r"\clrm.RESET", colorama.Style.RESET_ALL)
        string = string.replace(r"\n", "\n")
        string = string.replace(r"\t", "\t")
        return string

    def printManager(self):
        # todo: list division
        # try:
        #     split_list = np.array_split(self.opt_list, len(self.opt_list) // (len(self.opt_list) // self.max_items_column))
        # except ZeroDivisionError:
        #     split_list = [self.opt_list]
        split_list = [self.opt_list]
        print_list = []
        for x in range(len(split_list)):
            for i in range(len(split_list[x])):
                if self.cursor == i:
                    if len(print_list) < x:
                        print_list[i] += "\t" + self.decodeManager(self.option_type[1], self.opt_list[i])
                    else:
                        print_list.append(self.decodeManager(self.option_type[1], self.opt_list[i]))
                else:
                    if len(print_list) < x:
                        print_list[i] += "\t" + self.decodeManager(self.option_type[0], self.opt_list[i])
                    else:
                        print_list.append(self.decodeManager(self.option_type[0], self.opt_list[i]))

        system(cmd_clear)
        print(self.decodeManager(self.title_type) + "\n" + "\n".join(print_list))

    def fastInputManager(self, pressedKey):
        try:
            if pressedKey.decode().isdigit():
                tmpNow = datetime.now()
                if (tmpNow - self.tmpOld).total_seconds() > 0.75 and len(self.cursorKey) < 4:
                    self.cursorKey = ""
                self.cursorKey += pressedKey.decode()
                self.cursor = int(self.cursorKey) - 1
                if self.cursor >= len(self.opt_list):
                    self.cursor = len(self.opt_list) - 1
                elif self.cursor < 0:
                    self.cursor = 0
                self.tmpOld = tmpNow
                return 0
            else:
                return 1
        except UnicodeDecodeError:
            return 1

    def basicInputManager(self, pressedKey):
        if pressedKey == b'H':
            if self.cursor == 0:
                self.cursor = len(self.opt_list) - 1
            else:
                self.cursor -= 1
            return 0
        elif pressedKey == b'P':
            if self.cursor == len(self.opt_list) - 1:
                self.cursor = 0
            else:
                self.cursor += 1
            return 0
        elif pressedKey == b'\r':
            self.opt_list[self.cursor].enable()
            return 0
        else:
            return 1

    def hookManager(self):
        pressedKey = getch()
        if self.key_hook:
            if not self.fastInputManager(pressedKey):
                return 0
        return self.basicInputManager(pressedKey)


class Event:
    def __init__(self,
                 text: str,
                 func: object,
                 args: list = None,
                 desc: str = None,
                 color: colorama = colorama.Fore.CYAN):
        """
        :param text: Instance name.
        :param func: The function to call.
        :param args: Arguments to pass to the function.
        :param desc: Description of the instance.
        :param color: Color of the cursor in the menu.
        """
        self.text = text
        self.func = func
        self.args = args or []
        self.desc = desc or ""
        self.color = color

    def enable(self):
        """Activates the event."""
        self.func(*self.args)


class Menu(Layer):
    def __init__(self,
                 title: str,
                 desc: str = None,
                 opt_list: list = None):
        """
        :param title: Instance name. Displayed on top of all elements.
        :param desc: Description of the instance. Shown above the title.
        """
        super().__init__(title, desc, opt_list)


class Option(Event):
    def __init__(self,
                 text: str,
                 obj_menu: Menu = None,
                 desc: str = None,
                 color: colorama = colorama.Fore.CYAN):
        """
        :param text: Instance name.
        :param obj_menu: Menu object to call.
        :param desc: Description of the instance. Displayed to the right of the option.
        :param color: Color of the cursor in the menu.
        """
        color = color if obj_menu else colorama.Fore.LIGHTRED_EX
        super().__init__(text, obj_menu.enable if obj_menu else None, desc=desc, color=color)
