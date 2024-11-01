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


with patch.dict(sys.modules, {
    'js': MagicMock(currentCAE='CAE-1'), 
    'pyodide.http': PyodideHttpMock()
    }):
    import end2end


class TestEndToEnd(unittest.TestCase):

    def test_corpusCleanup_word_removal(self):
        input_corpus = 'This is an assigned task.'
        expected_output = 'This is an  task.'
        result = end2end.corpusCleanup(input_corpus)
        self.assertEqual(result, expected_output)

    def test_corpusCleanup_no_word(self):
        input_corpus = 'This is a test sentence'
        expected_output = 'This is a test sentence'
        result = end2end.corpusCleanup(input_corpus)
        self.assertEqual(result, expected_output)

    def test_corpusCleanup_multiple_exodus_words(self):
        input_corpus = "This job is for a junior developer."
        expected_output = "This  is for a  developer."
        result = end2end.corpusCleanup(input_corpus)
        self.assertEqual(result, expected_output)

    def test_list2string_empty_list(self):        
        self.assertEqual(end2end.list2string([], ', '), '')

    def test_list2string_single_element(self):
        self.assertEqual(end2end.list2string(['apple'], ', '), 'apple')

    def test_getAssessmentOutcomes(self):
        mock_js = sys.modules['js']
        result = end2end.getAssessmentOutcomes(mock_js.currentCAE)
        assert len(result) > 0

    @patch('end2end.display_to_div', MagicMock())
    def test_buttonExecution(self):
        end2end.buttonExecution()
