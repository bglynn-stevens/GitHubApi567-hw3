[![CircleCI](https://dl.circleci.com/status-badge/img/gh/bglynn-stevens/GitHubApi567-hw3/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/bglynn-stevens/GitHubApi567-hw3/tree/HW03b_mocking)

# GitHubApi567 - HW03b Mocking

## Description
This branch uses the same GitHub API function from HW03a, but all unit tests mock the API calls.  
No real network calls are made, so the tests run consistently and do not depend on GitHub data.

## Files
- `github_api.py` - contains the main function `get_user_repos_and_commits`.
- `test_github_api_mocked.py` - contains unit tests using `unittest.mock` to simulate GitHub responses.

## How to run
1. Make sure Python 3.8 is installed.
2. Run the mocked tests:
