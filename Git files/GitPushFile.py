from git import Repo

# Define the path to local repository
repo_path = r"C:\AAFINAL-SEMESTER\Programming Language Research Project\Practical_Project"

# Initialize the repository
repo = Repo(repo_path)

# Check if there are any uncommitted changes (including untracked files)
if repo.is_dirty() or repo.untracked_files:
    """
    If there are uncommitted changes or new files in the local repository;
    We stage (add) changes to repo. Commit changes with commit message.
    Compare this commit with the last commit and list files that had changes.
    Push changes to remote repository.
    """
    # Stage all changes (including untracked files)
    repo.git.add(A=True)  # Add all changes (modified and untracked files)
    
    # Commit the changes
    commit_message = "First Push of second practical project. Added MVC Folder structure. Modified CSVReader class to be FacilityModel class."
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
    
    # Push the changes to the remote repository
    try:
        print("Attempting to push to remote repository...")
        
        # Ensure the repository has a remote named 'origin'
        if repo.remotes:
            # Push the changes
            repo.remotes.origin.push()
            print("Push Successful! Nice job Tanek! Thanks Tanek 041012512 :)")
        else:
            print("No remote repository set up. Please add a remote and try again.")
    
    except Exception as e:
        print(f"Error pushing changes: {e}")
else:
    print("No changes to commit.")
