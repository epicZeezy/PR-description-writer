import os
from github import Github, Auth
from dotenv import load_dotenv
load_dotenv()

class GithubClient:
    def __init__(self):
        self.domain = "github.snooguts.net"
        auth = Auth.Token(os.getenv('GITHUB_TOKEN'))
        self.client = Github(base_url=f"https://{self.domain}/api/v3", auth=auth)

    def get_pr_diff(self, repo_path: str, pull_request_number: int):
        pass

    def update_pr_description(self, repo_path, pr_description, pr_number):
        pass
