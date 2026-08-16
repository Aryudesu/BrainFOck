from collections.abc import Callable

from error import NoBracketsError, PointerError
from importFile import file_check


def get_char(value: int) -> str:
    """Return the character for value, or an empty string if it is invalid."""
    try:
        return chr(value)
    except (ValueError, OverflowError):
        return ""


def build_bracket_map(source: str) -> dict[int, int]:
    """Build a bidirectional map between matching brackets."""
    bracket_map: dict[int, int] = {}
    stack: list[int] = []

    for index, command in enumerate(source):
        if command == "[":
            stack.append(index)
        elif command == "]":
            if not stack:
                raise NoBracketsError()
            opening_index = stack.pop()
            bracket_map[opening_index] = index
            bracket_map[index] = opening_index

    if stack:
        raise NoBracketsError()

    return bracket_map


def bf(
    source: str,
    read_char: Callable[[], str] | None = None,
    write: Callable[[str], None] | None = None,
) -> None:
    """Execute a Brainfuck program."""
    if read_char is None:
        read_char = _read_char
    if write is None:
        write = lambda value: print(value, end="")

    bracket_map = build_bracket_map(source)
    memory = [0]
    pointer = 0
    instruction_pointer = 0

    while instruction_pointer < len(source):
        command = source[instruction_pointer]

        if command == "+":
            memory[pointer] += 1
        elif command == "-":
            memory[pointer] -= 1
        elif command == ">":
            pointer += 1
            if pointer == len(memory):
                memory.append(0)
        elif command == "<":
            pointer -= 1
            if pointer < 0:
                raise PointerError()
        elif command == ".":
            write(get_char(memory[pointer]))
        elif command == ",":
            memory[pointer] = ord(read_char())
        elif command == "[" and memory[pointer] == 0:
            instruction_pointer = bracket_map[instruction_pointer]
        elif command == "]" and memory[pointer] != 0:
            instruction_pointer = bracket_map[instruction_pointer]

        instruction_pointer += 1


def _read_char() -> str:
    value = input("\n Input Char > ")
    return value[0]


def main() -> None:
    file_name = input("FileName > ")
    file_check(file_name)

    with open(file_name, encoding="utf-8") as source_file:
        source = source_file.read()

    bf(source)
    print()


if __name__ == "__main__":
    main()
