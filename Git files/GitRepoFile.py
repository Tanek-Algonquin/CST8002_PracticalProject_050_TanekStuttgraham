from git import Repo

# Define the URL of the repository and the local path where it should be cloned
repo_url = "https://github.com/Tanek-Algonquin/CST8002_PracticalProject_050_TanekStuttgraham"
repo_path = "C:\AAFINAL-SEMESTER\Programming Language Research Project\Practical_Project"  # Set the local directory path for the clone

# Clone the repository
try:
    print(f"Cloning repository {repo_url}...")
    repo = Repo.clone_from(repo_url, repo_path)
    print(f"Repository cloned successfully to {repo_path}")
except Exception as e:
    print(f"Error cloning repository: {e}")
