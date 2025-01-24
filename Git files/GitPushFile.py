from git import Repo
"""This file (GitPushFile) was written by Tanek Stuttgraham Student No 041012512, Course Code: CST8002_050, Prof. Todd Keuleman"""
# Define the path to local repository
repo_path = r"C:\AAFINAL-SEMESTER\Programming Language Research Project\Practical_Project"  

# Initialize the repository
repo = Repo(repo_path)

# Check if there are any uncommitted changes (including untracked (New) files)
if repo.is_dirty() or repo.untracked_files:
    """
If there are uncommited changes or new files in the local repository;
We stage (add) changes to repo. Commit changes with commit message.
Compare this commit with the last commit and list files that had changes.
Push changes to remote repository.
"""
    # Stage all changes (including untracked files)
    repo.git.add(A=True)  # Add all changes (modified and untracked files)
    # Commit the changes
    commit_message = "Sixth and actual final commit. Added course code and proffessor name source code comments."
    repo.index.commit(commit_message)
    # Print commit message
    print(f"Committed changes with message: {commit_message}")
    # Check if there is more than one commit to compare with
    if len(list(repo.iter_commits())) > 1:
        # Print files that were modified or added in the commit
        print("TanekSg committed these files:")
        for diff in repo.head.commit.diff("HEAD~1"):  # Compare with the previous commit
            print(f"- {diff.a_path} (change type: {diff.change_type})")
    else:
        print("This is the first commit, no previous commit to compare with.")
    
    # Push the changes
    try:
        print("Attempting to push to remote repository...")
        repo.remotes.origin.push()
        print("Push Successful! Nice job Tanek! Thanks Tanek 041012512:)")
    except Exception as e:
        print(f"Error pushing changes: {e}")
else:
    print("No changes to commit.")
