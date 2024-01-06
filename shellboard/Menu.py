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
                 _tag: str = "mLayer"):
        """
        :param title: Instance name.
        """
        super().__init__(_name, _class, _tag)
        Core.InputManager.__init__(self)

        @self.looping.combine
        def __looping(func):
            func()
            while self.loop:
                self.clearBuffer()
                self.bufferCondition()
                self.shellClear()
                print(f"\t{self.title}")
                print(self.join())
                while self.updateCursor():
                    pass

        self.title = title

        self.cursor = 0
        self.cursorKey = ""
        self.old = datetime.datetime.now()

        self.looping = __looping()
        self.isEnter = Core.EventManager(self.__isEnter())
        self.isKeyUp = Core.EventManager(self.__isKeyUp())
        self.isKeyDown = Core.EventManager(self.__isKeyDown())

    def bufferCondition(self):
        for uid, i in enumerate(self.widget_list):
            self.addToBuffer((i.on_selected if uid == self.cursor else i.on_unselected)())

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

    def setTitle(self, title):
        self.title = title

    def __isEnter(self):
        self.widget_list[self.cursor].on_clicked()

    def __isKeyUp(self):
        self.cursor = len(self.widget_list) - 1 if self.cursor == 0 else self.cursor - 1

    def __isKeyDown(self):
        self.cursor = 0 if self.cursor == len(self.widget_list) - 1 else self.cursor + 1

    def updateCursor(self):
        self.updateKey()
        if self.lastKey == b'H':
            self.isKeyUp()
        elif self.lastKey == b'P':
            self.isKeyDown()
        elif self.lastKey == b'\r':
            self.isEnter()
        else:
            try:
                if self.lastKey.decode().isdigit():
                    new = datetime.datetime.now()
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

        self.on_selected = Core.EventManager(self.__on_selected)
        self.on_unselected = Core.EventManager(self.__on_unselected)
        self.on_clicked = Core.EventManager()

        super().__init__(_name, _class, _tag)

    def __on_selected(self):
        return f"{self.color}> {self.text} {colorama.Fore.LIGHTBLACK_EX}{self.desc} {colorama.Style.RESET_ALL}"

    def __on_unselected(self):
        return f"{self.text}"


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
        super().__init__(text, desc, color if color else colorama.Fore.CYAN, _name, _class, _tag)

        self.link = link if link else function
        self.args = args or []

        self.on_clicked = Core.EventManager(self.__on_clicked)

    def __on_clicked(self):
        return self.link(*self.args)


class mOption(mLink):
    def __init__(self,
                 text: str,
                 obj: mLayer,
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
        super().__init__(text, desc, obj.looping, None, color, _name, _class, _tag)
