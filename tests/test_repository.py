import ast
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NotebookTests(unittest.TestCase):
    def test_notebooks_are_clean_and_python_cells_parse(self):
        for path in ROOT.glob("*.ipynb"):
            notebook = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(notebook["nbformat"], 4)
            for index, cell in enumerate(notebook["cells"]):
                if cell["cell_type"] == "code":
                    with self.subTest(notebook=path.name, cell=index):
                        self.assertFalse(cell.get("outputs"))
                        self.assertIsNone(cell.get("execution_count"))
                        source = "".join(line for line in cell["source"] if not line.lstrip().startswith("%"))
                        ast.parse(source)

    def test_no_common_key_literals_in_application_or_notebooks(self):
        pattern = re.compile(r"sk-[A-Za-z0-9_-]{20,}")
        for path in [*ROOT.glob("*.py"), *ROOT.glob("*.ipynb"), ROOT / ".env.example"]:
            self.assertIsNone(pattern.search(path.read_text(encoding="utf-8")), path.name)

    def test_retrieval_chunk_boundaries(self):
        notebook = json.loads((ROOT / "MIT COCOMELON.ipynb").read_text(encoding="utf-8"))
        source = next("".join(c["source"]) for c in notebook["cells"] if "def chunk_text(" in "".join(c["source"]))
        namespace = {"re": re, "List": list}
        exec(compile(source, "retrieval_chunk_cell", "exec"), namespace)
        chunk = namespace["chunk_text"]
        self.assertEqual(chunk("one two three four", 4, 1), ["one two three four"])
        self.assertEqual(chunk("one two three four five", 4, 1), ["one two three four", "four five"])
        for size, overlap in ((0, 0), (4, -1), (4, 4), (4, 5)):
            with self.assertRaises(ValueError):
                chunk("some words", size, overlap)
        with self.assertRaises(ValueError):
            namespace["clean_transcript"](" \n\t")


if __name__ == "__main__":
    unittest.main()
