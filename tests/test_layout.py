import ast
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LayoutTests(unittest.TestCase):
    def test_recovered_top_three_from_another_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.check_output(
                [sys.executable, "-B", str(ROOT / "src/question2a.py")]
                + [str(ROOT / "data" / f"data{i}.csv") for i in range(1, 4)],
                cwd=directory, text=True,
            )
        self.assertEqual(ast.literal_eval(result), [("C", 99.0), ("D", 99.0), ("A", 90.0)])
