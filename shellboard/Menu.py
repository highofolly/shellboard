from . import colorama, Core, function, datetime
from .Widgets import By as BY, LayerType, WidgetType


class By(BY):
    TITLE = "title"
    DESC = "desc"
    TEXT = "text"
    COMMENT = "comment"
    COLOR = "color"
    LINK = "link"


class mLayer(LayerType, Core.InputManager):
    def __init__(self,
                 title: str or WidgetType,
                 _name: str = None,
                 _class: str = "main",
                 _tag: str = "bmLayer"):
        """
        :param title: Instance name.
        """
        self.datetime = datetime.datetime

        self.title = title

        self.cursor = 0
        self.cursorKey = ""
        self.old = self.datetime.now()

        super().__init__(_name, _class, _tag)
        Core.InputManager.__init__(self)

    def looping(self):
        super().looping()
        while self.loop:
            self.clearBuffer()
            for i in enumerate(self.widget_list):
                self.addToBuffer(self.bufferCondition(i))
            self.shellClear()
            print(f"\t{self.title}")
            print(self.join())
            while self.updateCursor():
                pass

    def bufferCondition(self, i):
        return (i[1].Selected.on if i[0] == self.cursor else i[1].Unselected.on)()

    def addWidget(self, *functions):
        for i in functions:
            self.widget_list.append(i)

    def delWidget(self, *functions):
        self.widget_list.remove(*functions)

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


class mLabel(WidgetType):
    def __init__(self,
                 text: str,
                 desc: str = None,
                 color: colorama = None,
                 _name: str = None,
                 _class: str = "menu",
                 _tag: str = "bmLabel"):
        """
        :param text: Instance name.
        :param desc: Description of the instance.
        :param color: Color of the cursor in the menu.
        """
        self.text = text
        self.desc = desc or ""
        self.color = color if color else colorama.Fore.WHITE

        self.Selected = Core.EventManager(self.on_selected)
        self.Unselected = Core.EventManager(self.on_unselected)
        self.Clicked = Core.EventManager(self.on_clicked)

        super().__init__(_name, _class, _tag)

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
                 _tag: str = "bmLink"):
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
                 _tag: str = "bmOption"):
        """
        :param text: Instance name.
        :param obj_menu: Menu object to call.
        :param color: Color of the cursor in the menu.
        :param desc: Description of the instance.
        """
        super().__init__(text, desc, obj_menu.looping, None, color, _name, _class, _tag)
