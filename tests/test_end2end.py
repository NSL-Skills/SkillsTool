import os
import io
import sys
import urllib.parse
import unittest
from unittest.mock import MagicMock, patch


class PyodideHttpMock(MagicMock):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_url(self, url):
        parsed_url = urllib.parse.unquote(url)
        path = os.path.basename(parsed_url)
        return io.StringIO(open(path, 'r').read())

class TestEndToEnd(unittest.TestCase):
    
    @patch.dict(sys.modules, {'js': MagicMock(currentCAE='CAE-1'), 'pyodide.http': PyodideHttpMock()})
    def test_getAssessmentOutcomes(self):
        import end2end

        assert 1 == 1

