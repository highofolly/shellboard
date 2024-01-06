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
    def __init__(self,
                 _name: str = None,
                 _class: str = "main",
                 _tag: str = "LayerType"):

        class Looping(Core.EventManager):
            def func(cls, *args, **kwargs):
                """Open layer loop"""
                self.loop = True

        class Closing(Core.EventManager):
            def func(cls, *args, **kwargs):
                """Close layer loop"""
                self.loop = False

        self.widget_list = []
        self.symbol = "\n"
        self.loop = False

        self.shellClear = lambda: os.system("cls")

        self.looping = Looping()
        self.closing = Closing()

        super().__init__(_name, _class, _tag)

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
