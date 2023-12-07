from . import Core


class By:
    NAME = "_name"
    CLASS = "_class"
    TAG = "_tag"


class WidgetType(Core.EventManager, Core.BufferManager, Core.InputManager):
    def __init__(self,
                 _name: str = None,
                 _class: str = "main",
                 _tag: str = "WidgetType"):
        self._name = _name
        self._class = _class
        self._tag = _tag

        self.func_events = {}
        super().__init__()
        Core.BufferManager.__init__(self)
        Core.InputManager.__init__(self)

        self.func_events[0x001] = self.enable
        self.func_events[0x002] = self.disable

    def enable(self):
        pass

    def disable(self):
        pass

    def update(self):
        pass

    def updateEvents(self):
        for i in self.get_events():
            self.func_events[i]()
            self.events.remove(i)


class LayerType(WidgetType):
    def __init__(self,
                 _name: str = None,
                 _class: str = "main",
                 _tag: str = "LayerType"):
        super().__init__(_name, _class, _tag)
        self.widget_list = []
        self.symbol = "\n"

    def enable(self):
        self.updateBuffer()
        return self.join()

    def updateBuffer(self):
        self.clearBuffer()
        self.update()

        for i in self.widget_list:
            self.addToBuffer(str(i.update()))

    def addWidget(self, *functions):
        for i in functions:
            self.widget_list.append(i)

    def delWidget(self, *functions):
        self.widget_list.remove(*functions)

    def findBy(self, key: By.NAME, val):
        ret = []
        for widget in self.widget_list:
            if eval(f"widget.{key} == val"):
                ret.append(widget)
        return ret
