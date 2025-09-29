import unittest
from unittest.mock import patch
from github_api import get_user_repos_and_commits

# Simple mock response class
class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code
    def json(self):
        return self._json

class TestGitHubAPI(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_normal_case(self, mock_get):
        # Simulate two repos and commits
        mock_get.side_effect = [
            MockResponse([{"name": "repo1"}, {"name": "repo2"}], 200),  # repos
            MockResponse([{}, {}, {}], 200),  # repo1 commits
            MockResponse([{}, {}], 200)       # repo2 commits
        ]

        result = get_user_repos_and_commits("fakeuser")
        self.assertEqual(result, [("repo1", 3), ("repo2", 2)])

    @patch("github_api.requests.get")
    def test_user_not_found(self, mock_get):
        mock_get.return_value = MockResponse(None, 404)
        with self.assertRaises(Exception):
            get_user_repos_and_commits("unknownuser")

if __name__ == "__main__":
    unittest.main()
