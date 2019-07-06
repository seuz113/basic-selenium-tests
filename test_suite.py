import unittest
import google_search
import google_search_suggestions
 
class TestSuite(unittest.TestCase):
    def test_suite_to_execute(self):
        suite = unittest.TestSuite()
        suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(google_search.GoogleSearch),
            unittest.defaultTestLoader.loadTestsFromTestCase(google_search_suggestions.GoogleSearchSuggestions),
        ])
        suite.run(unittest.TestResult())

if __name__ == '__main__':
    unittest.main()