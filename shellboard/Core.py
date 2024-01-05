from . import function, ctypes, os


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
    def __init__(self, *args, **kwargs):
        self.__func = kwargs.pop("func", None) or args[0]

    def set(self, func: function):
        self.__func = func

    def on(self, *args, **kwargs):
        self.hook()
        return self.__func(*args, **kwargs)

    def hook(self):
        pass


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
                 symbol: str = None,
                 colm_len: int = 10,
                 algn_len: int = 10):
        self.buffer = buffer or []
        self.symbol = symbol or "\n"
        self.colm_len = colm_len
        self.algn_len = algn_len

    def __iadd__(self, other: str):
        self.addToBuffer(other)
        return self

    def __isub__(self, other: str):
        self.delFromBuffer(other)
        return self

    def __str__(self):
        return self.join()

    def addToBuffer(self, *args: str):
        for i in args:
            self.buffer.append(i)

    def delFromBuffer(self, *args: str):
        self.buffer.remove(*args)

    def clearBuffer(self):
        self.buffer.clear()

    def join(self) -> str:
        ret = list(range(self.colm_len if len(self.buffer) > self.colm_len else len(self.buffer)))
        index = 0
        for i in self.buffer:
            i = i.ljust(self.algn_len)
            ret[index] = i if type(ret[index]) == int else ret[index] + i
            if index < self.colm_len-1:
                index += 1
            else:
                index = 0
        return self.symbol.join(ret)


class CacheManager:
    def __init__(self, *args, **kwargs):
        self.cache = BufferManager(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.addsToState(*args, **kwargs)

    def addsToState(self, func: function, yield_func: iter, args: list = None):
        args = args or []
        for i in yield_func(*args):
            self.cache.addToBuffer(func(*i))
