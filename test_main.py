import subprocess
import sys
import unittest
from pathlib import Path

from error import NoBracketsError, PointerError
from main import bf, build_bracket_map


class BrainfuckTest(unittest.TestCase):
    def execute(self, source: str, inputs: str = "") -> str:
        output: list[str] = []
        iterator = iter(inputs)
        bf(source, read_char=lambda: next(iterator), write=output.append)
        return "".join(output)

    def test_hello_world_sample(self) -> None:
        source = Path("hw.bf").read_text(encoding="utf-8")
        self.assertEqual(self.execute(source), "Hello, world!")

    def test_loop_and_ignored_characters(self) -> None:
        self.assertEqual(self.execute("++ comment [>++<-]>+."), chr(5))

    def test_input(self) -> None:
        self.assertEqual(self.execute(",.", "A"), "A")

    def test_unmatched_brackets(self) -> None:
        for source in ("[", "]"):
            with self.subTest(source=source):
                with self.assertRaises(NoBracketsError):
                    build_bracket_map(source)

    def test_pointer_cannot_move_left_of_memory(self) -> None:
        with self.assertRaises(PointerError):
            self.execute("<")

    def test_import_has_no_side_effects(self) -> None:
        result = subprocess.run(
            [sys.executable, "-c", "import main"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
