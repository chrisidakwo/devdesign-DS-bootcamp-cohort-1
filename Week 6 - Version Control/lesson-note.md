# Version Control with Git

## What is Version Control?

Version control is a system that records changes to files over time so that you can:
- Recall specific versions later
- Track changes and their authors
- Revert to previous states of your project
- Compare changes over time

## Why Git Matters for Data Science

- **Experiment Tracking**: Track different approaches to your data analysis
- **Reproducibility**: Ensure others can reproduce your results exactly
- **Collaboration**: Work with team members without conflicts
- **Portfolio Building**: Showcase your projects on GitHub
- **Industry Standard**: Essential skill in professional data science roles

## Git Basics: The Core Workflow

Git works by taking snapshots of your project files when you commit:

1. **Working Directory**: Your local folder with project files
2. **Staging Area**: Files marked for the next commit
3. **Repository**: Where Git stores the committed history

The basic workflow:
```
Edit files → Stage changes → Commit → Push to remote
```

## Essential Git Commands

- `git init`: Create a new Git repository
- `git status`: Check the status of your working directory
- `git add <file>`: Add files to the staging area
- `git commit -m "message"`: Create a snapshot with a message
- `git log`: View commit history
- `git push`: Upload local changes to remote repository
- `git pull`: Download changes from remote repository

## Hands-on Practice

Let's create our first Git repository!

### 1. Initial Setup

```bash
# Configure Git with your identity (only needed once)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Create a project folder
mkdir student_grading_system
cd student_grading_system
```

### 2. Initialize Repository

```bash
# Create a new Git repository
git init

# Check status
git status
```

### 3. Add Files & Make First Commit

```bash
# Create a simple Python script
echo '# Student Grading System' > README.md
echo 'def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the function
print(calculate_grade(85))  # Should print "B"
' > grading.py

# Check status
git status

# Stage files
git add README.md grading.py

# Check status again
git status

# Commit
git commit -m "Initial commit with README and grading function"

# View history
git log
```

### 4. Making Changes & Tracking Them

```bash
# Edit the file to add another function
echo '
def calculate_average(scores):
    return sum(scores) / len(scores)

# Test the new function
test_scores = [85, 90, 78, 92]
print(f"Average score: {calculate_average(test_scores)}")
' >> grading.py

# Check what changed
git diff

# Stage and commit
git add grading.py
git commit -m "Added function to calculate average scores"
```

## GitHub: Taking Git to the Cloud (5 minutes)

GitHub is a web platform for hosting Git repositories:

### Creating a Remote Repository
1. Go to github.com and sign in
2. Click "New repository"
3. Name it "student_grading_system"
4. Keep it public for your portfolio (or private if preferred)
5. Skip adding README, .gitignore, license for now
6. Click "Create repository"

### Linking & Pushing to GitHub
```bash
# Connect your local repo to GitHub (replace with your username)
git remote add origin https://github.com/your-username/student_grading_system.git

# Push your commits to GitHub
git push -u origin main  # or git push -u origin master for older Git versions
```

## Take-Home Exercise

Apply version control to your Student Grading System project:

1. Create a GitHub repository
2. Add your existing code files
3. Make at least 3 different commits with meaningful changes
4. Write a proper README.md that describes:
   - What your project does
   - How to run it
   - Features implemented
5. Push all changes to GitHub

## Resources for Further Learning

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Interactive Tutorial: Learn Git Branching](https://learngitbranching.js.org/)
- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials)
- [Pro Git Book (free)](https://git-scm.com/book/en/v2)

## Git Cheat Sheet

```
# Getting Started
git init                   # Initialize a repository
git clone [url]            # Clone existing repository

# Basic Workflow
git status                 # Check status
git add [file]             # Add file to staging area
git add .                  # Add all changed files
git commit -m "[message]"  # Commit with message
git push                   # Upload to remote

# History
git log                    # View commit history
git diff                   # View changes

# Branches (Advanced)
git branch                 # List branches
git branch [name]          # Create branch
git checkout [name]        # Switch to branch
git merge [branch]         # Merge branch into current

# Undo (Advanced)
git restore [file]         # Discard changes
git reset HEAD [file]      # Unstage file
```