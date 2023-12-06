import ctypes
from . import function
import os


class ConsoleManagerBeta:
    @staticmethod
    def getTitle() -> str:
        """Get the title of current console"""
        strbuffer = ctypes.create_string_buffer(1024)
        size = ctypes.c_short(1024)
        ctypes.windll.kernel32.GetConsoleTitleA(strbuffer, size)
        return strbuffer.value.replace(b" - pc", b"").decode()

    @staticmethod
    def setTitle(title):
        """Set the title of the current console"""
        ctypes.windll.kernel32.SetConsoleTitleA(bytes(title))

    @staticmethod
    def getSize() -> list:
        """Get size of current console"""
        return list(os.get_terminal_size())

    @staticmethod
    def setSize(x, y):
        """Set size of current console"""
        os.system(f"mode {x},{y}")


class EventManager:
    def __init__(self):
        self.events = []

    def __add_event__(self, uid):
        self.events.append(uid)

    def get_events(self) -> iter:
        return iter(self.events)


class InputManager:
    def __init__(self):
        from msvcrt import getch
        self.getch = getch
        self.lastKey = None

    def updateKey(self) -> int:
        while True:
            self.lastKey = self.getch()
            if self.lastKey == b'\xe0':
                self.lastKey = self.getch()
                return 0x2
            else:
                return 0x1


class BufferManager:
    def __init__(self,
                 buffer: list = None,
                 symbol: str = None):
        self.buffer = buffer or []
        self.symbol = symbol or "\n"

    def addToBuffer(self, *args: str):
        for i in args:
            self.buffer.append(i)

    def delFromBuffer(self, *args: str):
        self.buffer.remove(*args)

    def clearBuffer(self):
        self.buffer.clear()

    def join(self) -> str:
        return self.symbol.join(self.buffer)

    def __iadd__(self, other: str):
        self.addToBuffer(other)
        return self

    def __isub__(self, other: str):
        self.delFromBuffer(other)
        return self

    def __str__(self):
        return self.join()
