import ctypes
from . import function
import os


class consoleManagerBeta:
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


class eventManager:
    def __init__(self):
        self.events = []

    def __add_event__(self, uid):
        self.events.append(uid)

    def get(self):
        return iter(self.events)


class inputManager:
    def __init__(self):
        from msvcrt import getch
        self.getch = getch
        self.lastKey = None

    def updateKey(self):
        while True:
            self.lastKey = self.getch()
            if self.lastKey == b'\xe0':
                self.lastKey = self.getch()
                return 0x2
            else:
                return 0x1

    def lastInputKey(self):
        return self.lastKey


class bufferManager:
    def __init__(self,
                 buffer: list = None,
                 symbol: str = None):
        self.buffer = buffer or []
        self.symbol = symbol or ""
        self.buffers = [self]

    def connect(self, buffer: function):
        self.buffers.append(buffer)

    def add(self, string: str):
        self.buffer.append(string)

    def join(self):
        ret = ""
        for i in self.buffers:
            if len(i.buffers) > 1 and i != self:
                ret += i.join()
            else:
                ret += i.symbol.join(i.buffer)
        return ret

    def clear(self):
        self.buffer = []

    def __iadd__(self, other: str):
        self.add(other)

    def __str__(self):
        self.join()


class bufferManagerBeta:  # todo: +mgc methods, dict
    def __init__(self,
                 file_name: str = "buffer"):
        self.file_name = file_name
        self.buffer = {}

    # def updateFile(self):
    #     open(self.file_name)

    def delFrom(self, uname):
        del self.buffer[uname]

    def addTo(self, uname, string):
        self.buffer[uname] = string

    def getData(self, uname):
        return self.buffer[uname]
