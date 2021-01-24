from enum import Flag, auto


class ExitCode(Flag):
    SUCCESS = 0
    INVALID_CHARS = auto()
    INVALID_LENGTH = auto()
