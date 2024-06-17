## Overview
In this project, we will develop a **PR description writer** to enhance developer productivity. We will leverage Retrieval-Augmented Generation (RAG) to dynamically get the pull request diff and update the PR description. This will help summarize our changes to reviewers.

## Setup Steps

### Python Setup
1. Update Homebrew:
    ```bash
    brew update
    ```
2. Install `pyenv`:
    ```bash
    brew install pyenv
    ```
3. Install Python 3.9.0:
    ```bash
    pyenv install 3.9.0
    ```
4. Set Python 3.9.0 as the global version:
    ```bash
    pyenv global 3.9.0
    ```
5. Verify Python version:
    ```bash
    python --version
    ```

### Virtual Environment Setup
1. Create a virtual environment (you can do this in Visual Studio Code):
    ```bash
    pyenv virtualenv <name of virtualenv>
    ```
2. Activate the virtual environment:
    ```bash
    pyenv activate <name of virtualenv>
    ```

### Install Requirements
1. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
2. If you need to delete current packages:
    ```bash
    pip freeze | xargs pip uninstall -y
    ```

### Ollama Setup
1. Install Ollama based on [this documentation](https://python.langchain.com/v0.2/docs/integrations/llms/ollama/):
    ```bash
    brew install ollama
    ```
2. Pull and run the `llama3` model:
    ```bash
    ollama pull llama3
    ollama run llama3
    ```
3. The model will be hosted on `localhost:11343`. You can test it with:
    ```bash
    curl http://localhost:11434/api/generate -d '{
        "model": "llama3",  
        "prompt":"Why is the sky blue?"  
      }'  
    ```

Now, you can go into your editor and start working.


### Bonus
1. **Github workflow:** Make the script a github workflow for a repository that you fork
---
