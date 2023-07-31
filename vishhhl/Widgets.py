from . import Core, function


class WidgetType(Core.eventManager, Core.bufferManager, Core.inputManager):
    def __init__(self,
                 _name: str,
                 _class: str,
                 _tag: str):
        self._name = _name
        self._class = _class
        self._tag = _tag

        self.func_events = {}
        super().__init__()
        Core.bufferManager.__init__(self)
        Core.inputManager.__init__(self)

        self.func_events[0x001] = self.enable
        self.func_events[0x002] = self.disable

    def enable(self):
        pass

    def disable(self):
        pass

    def update(self):
        pass

    def updateEvents(self):
        for i in self.get():
            self.func_events[i]()
            self.events.remove(i)


class LayerType(WidgetType):
    def __init__(self,
                 _name: str = "unnamed",
                 _class: str = "main",
                 _tag: str = "mwLayer"):
        import os
        super().__init__(_name, _class, _tag)
        self.symbol = "\n"

        self.cmd_clear = lambda: os.system("cls")
        self.printLayer = lambda: print(self.join())
        self.addLine = lambda string: self.add(string)
        self.delLine = lambda index: self.buffer.pop(index)
