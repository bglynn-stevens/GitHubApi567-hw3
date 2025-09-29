import unittest
from github_api import get_user_repos_and_commits

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        """
        Optional: set a default username that you can easily change for testing.
        """
        self.user_to_test = "richkempinski"  # Change this to test a different GitHub user

    def test_user_repos_structure(self):
        """Test that the returned data is in the correct format for any user."""
        repos = get_user_repos_and_commits(self.user_to_test)
        self.assertIsInstance(repos, list)
        for item in repos:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)
            self.assertIsInstance(item[0], str)  # repo name
            self.assertIsInstance(item[1], int)  # commit count

    def test_invalid_user(self):
        """Test behavior for a user that does not exist."""
        with self.assertRaises(Exception):
            get_user_repos_and_commits("thisuserdoesnotexist12345")

if __name__ == "__main__":
    unittest.main()
