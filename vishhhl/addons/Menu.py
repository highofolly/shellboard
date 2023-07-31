from ..Widgets import LayerType, WidgetType
from .. import function
import colorama
import os

colorama.init()


class mLayer(LayerType):
    def __init__(self,
                 title: str = None,
                 desc: str = None,
                 _name: str = None,
                 _class: str = "main",
                 _tag: str = "mLayer"):
        """
        :param title: Instance name.
        :param desc: Description of the instance.
        """
        from datetime import datetime
        self.datetime = datetime
        super().__init__(_name, _class, _tag)
        self.func_list = []

        self.title = title
        self.desc = desc

        self.cursor = 0
        self.loop = False
        self.cursorKey = ""
        self.tmpOld = self.datetime.now()

    def enable(self):
        """Opens the loop."""
        self.loop = True
        self.mainLoop()

    def disable(self):
        """Closes the menu loop."""
        self.loop = False

    def updateLayer(self):
        self.clear()
        self.update()

        self.add(f"\t{self.title}")

        for i in range(len(self.func_list)):
            self.func_list[i].update()
            if self.cursor == i:
                # i.func_list[self.cursor].__add_event__(0x100)
                self.add(self.func_list[i].on_selected())
            else:
                # self.buffer.add(i.func_list[self.cursor].__add_event__(0x101))
                self.add(self.func_list[i].on_unselected())

        os.system("cls")

    def mainLoop(self):
        while self.loop:
            self.update()
            self.updateLayer()
            self.printLayer()
            while self.updateCursor():
                pass

    def addOption(self, *functions):
        for i in functions:
            self.func_list.append(i)

    def addOptionByIndex(self, *options, index):
        for i in options:
            self.func_list.insert(index, i)

    def delOption(self, *functions):
        for i in functions:
            for uid in range(len(self.func_list)):
                if i == self.func_list[uid]:
                    del self.func_list[uid]

    def delOptionByIndex(self, index):
        try:
            del self.func_list[index]
        except IndexError:
            return 1

    def changeTitle(self, title):
        self.title = title

    def changeDesc(self, desc):
        self.desc = desc

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
                self.cursor = len(self.func_list) - 1
            else:
                self.cursor -= 1
        elif self.isKeyDown():
            if self.cursor == len(self.func_list) - 1:
                self.cursor = 0
            else:
                self.cursor += 1
        elif self.isEnter():
            self.func_list[self.cursor].on_clicked()
        else:
            try:
                if self.lastKey.decode().isdigit():
                    tmpNow = self.datetime.now()
                    if (tmpNow - self.tmpOld).total_seconds() > 0.75 and len(self.cursorKey) < 4:
                        self.cursorKey = ""
                    self.cursorKey += self.lastKey.decode()
                    self.cursor = int(self.cursorKey) - 1
                    if self.cursor >= len(self.func_list):
                        self.cursor = len(self.func_list) - 1
                    elif self.cursor < 0:
                        self.cursor = 0
                    self.tmpOld = tmpNow
                    return 0
                else:
                    return 1
            except UnicodeDecodeError:
                return 1


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


class mLabel(mWidget):
    def __init__(self,
                 text: str,
                 comment: str = None,
                 color: colorama = colorama.Fore.WHITE,
                 _name: str = None,
                 _class: str = "menu",
                 _tag: str = "mLabel"):
        """
        :param text: Instance name.
        :param comment: Description of the instance.
        :param color: Color of the cursor in the menu.
        """
        self.text = text
        self._name = _name if _name else text
        self.comment = comment or ""
        self.color = color
        super().__init__(_name, _class, _tag)

    def changeText(self, text):
        self.text = text

    def changeComment(self, comment):
        self.comment = comment

    def on_selected(self):
        return f"{self.color}> {self.text} {colorama.Fore.LIGHTBLACK_EX}{self.comment} {colorama.Style.RESET_ALL}"

    def on_unselected(self):
        return f"{self.text}"


class mLink(mLabel):
    def __init__(self,
                 text: str,
                 link: function,
                 args: list = None,
                 comment: str = None,
                 color: colorama = colorama.Fore.CYAN,
                 _name: str = None,
                 _class: str = "menu",
                 _tag: str = "mLink"):
        """
        :param text: Instance name.
        :param link: Link to function object to call.
        :param args: Arguments to pass to function.
        :param comment: Description of the instance.
        :param color: Color of the cursor in the menu.
        """
        self.link = link
        self.args = args or []
        super().__init__(text, comment, color, _name, _class, _tag)

    def on_clicked(self):
        return self.link(*self.args)


class mOption(mLink, mLayer):
    def __init__(self,
                 text: str,
                 obj_menu: mLayer,
                 comment: str = None,
                 color: colorama = colorama.Fore.CYAN,
                 title: str = None,
                 desc: str = None,
                 _name: str = None,
                 _class: str = "menu",
                 _tag: str = "mOption"):
        """
        :param text: Instance name.
        :param obj_menu: Menu object to call.
        :param comment: Description of the instance.
        :param color: Color of the cursor in the menu.
        :param title: Instance name.
        :param desc: Description of the instance.
        """
        mLayer.__init__(self, title, desc)
        super().__init__(text, obj_menu.enable, None, comment, color, _name, _class, _tag)
