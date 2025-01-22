from git import Repo

# Define the path to local repository
repo_path = r"C:\AAFINAL-SEMESTER\Programming Language Research Project\Practical_Project"  # Use raw string to avoid \ new line issue

# Initialize the repository
repo = Repo(repo_path)

# Check if there are any uncommitted changes (including untracked files)
if repo.is_dirty() or repo.untracked_files:
    # Stage all changes (including untracked files)
    repo.git.add(A=True)  # Add all changes (modified and untracked files)
    
    # Commit the changes
    commit_message = "Second automated commit from Thonny for my Practical Project. Including a DTO for Facilities and an incomplete CSV reader class"
    repo.index.commit(commit_message)
    
    # Print commit message
    print(f"Committed changes with message: {commit_message}")
    
    # Check if there is more than one commit to compare with
    if len(list(repo.iter_commits())) > 1:
        # Print files that were modified or added in the commit
        print("Files that were committed:")
        for diff in repo.head.commit.diff("HEAD~1"):  # Compare with the previous commit
            print(f"- {diff.a_path} (change type: {diff.change_type})")
    else:
        print("This is the first commit, no previous commit to compare with.")
    
    # Push the changes
    try:
        print("Attempting to push to remote repository...")
        repo.remotes.origin.push()
        print("Push Successful! :)")
    except Exception as e:
        print(f"Error pushing changes: {e}")
else:
    print("No changes to commit.")
