import english_uk
import symbols
from exit_code import ExitCode

ALL_CHARACTERS = set(english_uk.ENGLISH_UK_REMOVED_DUPES + symbols.SYMBOLS_REMOVED_DUPES)
ALL_CHARACTERS_VALID_FOR_NAME = set(english_uk.ENGLISH_UK_VALID_FOR_NAME_ONLY + symbols.SYMBOLS_VALID_FOR_NAME_ONLY)


def verify(input_str: str, verbose: bool = True) -> ExitCode:
    if not input_str:
        if verbose:
            print('Invalid: Name must be at least one character.')
        return ExitCode.INVALID_LENGTH

    exit_code = ExitCode.SUCCESS
    if len(input_str) > 10:
        if verbose:
            print('Invalid: Name cannot be more than 10 characters.')
        exit_code |= ExitCode.INVALID_LENGTH

    if all(char in ALL_CHARACTERS_VALID_FOR_NAME for char in input_str):
        if verbose:
            print('Characters valid!')
    else:
        if verbose:
            print('Invalid: The following characters were not found/allowed: ')
            print(''.join([char for char in input_str if char not in ALL_CHARACTERS_VALID_FOR_NAME]))

        exit_code |= ExitCode.INVALID_CHARS

    return exit_code
