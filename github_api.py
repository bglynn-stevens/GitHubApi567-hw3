import requests

def get_user_repos_and_commits(user_id):
    """
    Retrieves repositories for a GitHub user and counts commits for each.
    Returns a list of tuples: (repo_name, commit_count)
    """
    repo_url = f"https://api.github.com/users/{user_id}/repos"
    resp = requests.get(repo_url)

    # Check if user exists
    if resp.status_code != 200:
        raise Exception(f"GitHub user '{user_id}' not found or API limit exceeded.")

    repos = resp.json()
    result = []

    for repo in repos:
        name = repo.get("name")
        commits_url = f"https://api.github.com/repos/{user_id}/{name}/commits"
        commits_resp = requests.get(commits_url)

        if commits_resp.status_code != 200:
            commits_count = 0
        else:
            commits_count = len(commits_resp.json())

        result.append((name, commits_count))

    return result


if __name__ == "__main__":
    user_id = input("Enter a GitHub username to check: ")
    try:
        repos_and_commits = get_user_repos_and_commits(user_id)
        for repo_name, count in repos_and_commits:
            print(f"Repo: {repo_name}  Number of commits: {count}")
    except Exception as e:
        print(e)
