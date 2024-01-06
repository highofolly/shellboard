from . import Core, os


class By:
    NAME = "_name"
    CLASS = "_class"
    TAG = "_tag"


class WidgetType(Core.BufferManager):
    def __init__(self,
                 _name: str = None,
                 _class: str = "main",
                 _tag: str = "WidgetType"):
        self._name = _name
        self._class = _class
        self._tag = _tag

        super().__init__()


class LayerType(WidgetType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widget_list = []
        self.symbol = "\n"
        self.loop = False

        self.shellClear = lambda: os.system("cls")

        self.looping = Core.EventManager(self.__looping())
        self.closing = Core.EventManager(self.__closing())

    def __looping(self):
        """Open layer loop"""
        self.loop = True

    def __closing(self):
        """Close layer loop"""
        self.loop = False

    def find(self, key: By.NAME, val):
        """
        Finding a child element in a layer widget list
        :return: class exemplar
        """
        ret = []
        for widget in self.widget_list:
            if eval(f"widget.{key} == val"):
                ret.append(widget)
        return ret
