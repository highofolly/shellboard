from threading import Thread
from .Menu import mLayer


class aLayer(mLayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__thread = True

    def mainLoop(self):
        def updating(func):
            while self.__thread:
                func()

        self.__thread = True
        th = Thread(target=updating, args=[self.updateCursor])
        th.start()
        while self.loop:
            self.update()
            for i in self.widget_list:
                i.update()
            self.updateBuffer()
            self.shellClear()
            print(self.join())
        self.__thread = False
        th.join()

    def isEnter(self):
        self.__thread = False
        super().isEnter()
