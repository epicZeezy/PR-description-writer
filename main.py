import os
import argparse
from utility import *
from github_client import GithubClient
from llm_clients import *
from prompt_formatting import GeneratePRDescriptionPromptTemplate
from dotenv import load_dotenv
load_dotenv()
def main():
    # Initialize GitHub API with token
    github_client = GithubClient()
    parser = argparse.ArgumentParser(description='Process repository path and pull request number.')
    parser.add_argument('--repo_path', type=str, help='The path to the repository.')
    parser.add_argument('--pr_number', type=int, help='The pull request number.')
    # Get the repo path and PR number
    args = parser.parse_args()
    repo_path = args.repo_path
    pull_request_number = args.pr_number

    # Get diff for pull request

    # Format data for prompt

    # Ollama local LLM call

    # Update the PR description

if __name__ == '__main__':
    main()
