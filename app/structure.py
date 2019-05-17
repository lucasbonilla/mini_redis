import threading


class ThreadSafeDict(dict):
    def __init__(self, * p_arg, ** n_arg):
        dict.__init__(self, * p_arg, ** n_arg)
        self._lock = threading.Lock()

    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, type, value, traceback):
        self._lock.release()


class ReturnValue(str):

    OK_ = "ok"
    NIL_ = "nil"
    ERROR_NUMBER_OF_ARGUMENTS = "Invalid number of arguments"
    ERROR_TYPE_DATA = "Invalid type of data"
    ZERO = 0
