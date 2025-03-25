import pytest

@pytest.mark.supported
def test_1(tmp_path):
    py_file = tmp_path / "test_file1.py"
    py_file.write_text("""
from time import time
""")
    with open(str(tmp_path)+"/test_file1.py") as f:
        code = f.read()

    assert "time" in code

@pytest.mark.supported
def test_2(tmp_path):
    py_file = tmp_path / "test_file2.py"
    py_file.write_text("""
from random import random
""")
    
    with open(str(tmp_path)+"/test_file2.py") as f:
        code = f.read()

    assert "time" in code