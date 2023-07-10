# Dont make changes in this file
import unittest
import sys
from io import StringIO

from test import *

class TestOutput(unittest.TestCase):
    def test_output(self):
        expected_output ="hello, Human:)"

        # Redirect sys.stdout to capture the output
        sys.stdout = captured_output = StringIO()

        # Call the student's code
        print_name()

        # Restore sys.stdout
        sys.stdout = sys._stdout_

        # Compare the expected output with the captured output
        self.assertEqual(captured_output.getvalue(), expected_output)

if _name_ == '_main_':
    unittest.main()
