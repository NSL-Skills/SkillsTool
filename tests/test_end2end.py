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


@patch.dict(sys.modules, {'js': MagicMock(currentCAE='CAE-1'), 'pyodide.http': PyodideHttpMock()})
class TestEndToEnd(unittest.TestCase):
    
    @unittest.skip
    def test_getAssessmentOutcomes(self):
        import end2end

        mock_js = sys.modules['js']
        result = end2end.getAssessmentOutcomes(mock_js.currentCAE)

        assert len(result) > 0

    @patch('end2end.display_to_div', MagicMock())
    def test_buttonExecution(self):
        import end2end

        end2end.buttonExecution()


