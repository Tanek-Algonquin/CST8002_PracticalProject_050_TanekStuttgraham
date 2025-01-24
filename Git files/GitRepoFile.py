from git import Repo
"""This file (GitRepoFile) was written by Tanek Stuttgraham Student No 041012512, Course Code: CST8002_050, Prof. Todd Keuleman"""
# Define the URL of the repository and the local path where it should be cloned
repo_url = "https://github.com/Tanek-Algonquin/CST8002_PracticalProject_050_TanekStuttgraham"
repo_path = "C:\AAFINAL-SEMESTER\Programming Language Research Project\Practical_Project"  # Set the local directory path for the clone

"""
Clones a Git repo  from repository url to a file location defined by repo_path
Args :
    repo_url (str) : Url for github.com repository.
    repo_path(str) : Location for clone of repository on local machine.
"""
try:
    print(f"Cloning repository {repo_url}...")
    repo = Repo.clone_from(repo_url, repo_path)
    print(f"Repository cloned successfully to {repo_path}")
except Exception as e:
    print(f"Error cloning repository: {e}")
