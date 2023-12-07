"""
Addon for todo: desc
"""
from . import *
import colorama

colorama.init()


class By(By):
    TITLE = "title"
    DESC = "desc"
    TEXT = "text"
    COMMENT = "comment"
    COLOR = "color"
    LINK = "link"


class mWidget(WidgetType):
    def __init__(self,
                 _name: str,
                 _class: str = "menu",
                 _tag: str = "mWidget"):
        super().__init__(_name, _class, _tag)

        self.func_events[0x100] = self.on_selected
        self.func_events[0x101] = self.on_unselected
        self.func_events[0x102] = self.on_clicked

    def on_selected(self):
        pass

    def on_unselected(self):
        pass

    def on_clicked(self):
        pass


class mLayer(LayerType):
    def __init__(self,
                 title: str or mWidget,
                 second: str = None,
                 _name: str = None,
                 _class: str = "main",
                 _tag: str = "mLayer"):
        """
        :param title: Instance name.
        :param second: Description of the instance.
        """
        from datetime import datetime
        import os
        self.datetime = datetime
        super().__init__(_name, _class, _tag)

        self.title = title
        self.second = second

        self.cursor = 0
        self.loop = False
        self.cursorKey = ""
        self.old = self.datetime.now()

        self.shellClear = lambda: os.system("cls")

    def enable(self):
        """Opens the loop."""
        self.loop = True
        self.mainLoop()

    def disable(self):
        """Closes the menu loop."""
        self.loop = False

    def updateBuffer(self):
        self.clearBuffer()
        self.update()

        for uid, i in enumerate(self.widget_list):
            if self.cursor == uid:
                # i.func_list[self.cursor].__add_event__(0x100)
                self.addToBuffer(i.on_selected())
            else:
                # self.buffer.add(i.func_list[self.cursor].__add_event__(0x101))
                self.addToBuffer(i.on_unselected())

    def mainLoop(self):
        while self.loop:
            self.update()
            for i in self.widget_list:
                i.update()
            self.updateBuffer()
            self.shellClear()
            print(f"\t{self.title}" + (f" | {self.second}" if self.second else ""))
            print(self.join())
            while self.updateCursor():
                pass

    def addOptionByIndex(self, *options, index):
        for i in options:
            self.widget_list.insert(index, i)

    def delWidgetByIndex(self, *indexes):
        for i in indexes:
            del self.widget_list[i]

    def changeTitle(self, title):
        self.title = title

    def changeSecond(self, second):
        self.second = second

    def isEnter(self):
        return True if self.lastKey == b'\r' else False

    def isKeyUp(self):
        return True if self.lastKey == b'H' else False

    def isKeyDown(self):
        return True if self.lastKey == b'P' else False

    def updateCursor(self):
        self.updateKey()
        if self.isKeyUp():
            if self.cursor == 0:
                self.cursor = len(self.widget_list) - 1
            else:
                self.cursor -= 1
        elif self.isKeyDown():
            if self.cursor == len(self.widget_list) - 1:
                self.cursor = 0
            else:
                self.cursor += 1
        elif self.isEnter():
            self.widget_list[self.cursor].on_clicked()
        else:
            try:
                if self.lastKey.decode().isdigit():
                    new = self.datetime.now()
                    if (new - self.old).total_seconds() > 0.75 and len(self.cursorKey) < 4:
                        self.cursorKey = ""
                    self.cursorKey += self.lastKey.decode()
                    self.cursor = int(self.cursorKey) - 1
                    if self.cursor >= len(self.widget_list):
                        self.cursor = len(self.widget_list) - 1
                    elif self.cursor < 0:
                        self.cursor = 0
                    self.old = new
                    return 0
                else:
                    return 1
            except UnicodeDecodeError:
                return 1


class mLabel(mWidget):
    def __init__(self,
                 text: str,
                 desc: str = None,
                 color: colorama = None,
                 _name: str = None,
                 _class: str = "menu",
                 _tag: str = "mLabel"):
        """
        :param text: Instance name.
        :param desc: Description of the instance.
        :param color: Color of the cursor in the menu.
        """
        self.text = text
        self.desc = desc or ""
        self.color = color if color else colorama.Fore.WHITE
        super().__init__(_name, _class, _tag)

    def changeText(self, text):
        self.text = text

    def changeDescription(self, desc: str):
        self.desc = desc

    def on_selected(self):
        return f"{self.color}> {self.text} {colorama.Fore.LIGHTBLACK_EX}{self.desc} {colorama.Style.RESET_ALL}"

    def on_unselected(self):
        return f"{self.text}"

    def on_clicked(self):
        self.color = colorama.Fore.RED


class mLink(mLabel):
    def __init__(self,
                 text: str,
                 desc: str = None,
                 link: function = None,
                 args: list = None,
                 color: colorama = None,
                 _name: str = None,
                 _class: str = "menu",
                 _tag: str = "mLink"):
        """
        :param text: Instance name.
        :param link: Link to function object to call.
        :param args: Arguments to pass to function.
        :param desc: Description of the instance.
        :param color: Color of the cursor in the menu.
        """
        self.link = link if link else function
        self.args = args or []
        color = color if color else colorama.Fore.CYAN
        super().__init__(text, desc, color, _name, _class, _tag)

    def on_clicked(self):
        return self.link(*self.args)


class mOption(mLink):
    def __init__(self,
                 text: str,
                 obj_menu: mLayer,
                 desc: str = None,
                 color: colorama = colorama.Fore.CYAN,
                 _name: str = None,
                 _class: str = "menu",
                 _tag: str = "mOption"):
        """
        :param text: Instance name.
        :param obj_menu: Menu object to call.
        :param color: Color of the cursor in the menu.
        :param desc: Description of the instance.
        """
        super().__init__(text, desc, obj_menu.enable, None, color, _name, _class, _tag)
