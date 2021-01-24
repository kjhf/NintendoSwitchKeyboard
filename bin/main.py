import sys

from keyboard import verify

if __name__ == '__main__':
    exit_code = verify(input('Name to verify?'))
    sys.exit(exit_code.value)
