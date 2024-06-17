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
    pull_request_diff = github_client.get_pr_diff(repo_path, pull_request_number)

    # Format data for Gemini prompt
    pr_description_generator = GeneratePRDescriptionPromptTemplate()
    pr_description_prompt = pr_description_generator.generate_pr_description_prompt(pull_request_diff)

    # Ollama local LLM call
    llm = new_ollama_client()
    llm_response = llm.invoke(pr_description_prompt)
    print(llm_response.content)

    # Do some structured output for LLM response
    # github_client.update_pr_description(repo_path, llm_response.content, pull_request_number)

if __name__ == '__main__':
    main()
