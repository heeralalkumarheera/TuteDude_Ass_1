# Assignment 4 – Git and GitHub (Step-by-Step Explanation)

## Task 1: Create Assignment-4 Folder and Push to GitHub

First, I created a new folder named Assignment-4 inside my existing project repository. Then I created a new branch to work on this assignment separately.

### Commands Used:

git checkout -b assignment4
→ This command creates a new branch named "assignment4" and switches to it.

git add .
→ This command adds all new and modified files to the staging area.

git commit -m "Added Assignment-4"
→ This saves the changes with a message.

git push origin assignment4
→ This uploads the new branch and changes to GitHub.

git checkout main
→ Switches back to the main branch.

git merge assignment4
→ Merges the assignment4 branch into the main branch.

git push origin main
→ Updates the main branch on GitHub.

---

## Task 2: Create New Branch and Update JSON File

I created another branch to update the JSON file used in the API and then merged it into the main branch.

### Commands Used:

git checkout -b heeralal_new
→ Creates and switches to a new branch.

git add .
→ Adds updated JSON file to staging.

git commit -m "Updated JSON file"
→ Saves the changes.

git push origin heeralal_new
→ Pushes the branch to GitHub.

git checkout main
→ Switches to main branch.

git merge heeralal_new
→ Merges the changes into main.

git push origin main
→ Pushes updated main branch.

If there was a conflict:
git add .
git commit -m "Resolved conflict"
→ This saves the conflict resolution changes.

---

## Task 3: Frontend and Backend Development Using Branches

I created two branches: one for frontend and one for backend.

### Branch Creation:

git checkout -b master_1
→ Creates branch for frontend work.

git checkout main
git checkout -b master_2
→ Creates branch for backend work.

---

### Frontend (master_1):

I created a To-Do form with fields like Item Name and Item Description.

Commands:
git add .
git commit -m "Added frontend To-Do form"
git push origin master_1

---

### Backend (master_2):

I created an API route to accept data and store it.

Commands:
git add .
git commit -m "Added backend API"
git push origin master_2

---

### Merge Both Branches:

git checkout main
→ Switch to main branch.

git merge master_1
→ Merge frontend changes.

git merge master_2
→ Merge backend changes.

git push origin main
→ Push final merged code.

---

## Task 4: Multiple Commits, Reset and Rebase

In this task, I added fields step-by-step and committed each change separately.

### Step-by-step commits:

git checkout master_1

git add .
git commit -m "Added Item ID"
→ First commit

git add .
git commit -m "Added Item UUID"
→ Second commit

git add .
git commit -m "Added Item Hash"
→ Third commit

git push origin master_1

---

### Merge into Main:

git checkout main
git merge master_1

---

### Git Reset:

git log --oneline
→ Shows commit history.

git reset --soft <commit_id>
→ Moves back to a previous commit but keeps changes staged.

git commit -m "Reset to Item ID state"
→ Saves the reset state.

git push origin main

---

### Git Rebase:

git checkout master_1
git rebase main
→ Applies main branch changes onto master_1 without losing commit history.

git push origin master_1

---

## Conclusion

In this assignment, I learned how to create and manage branches, merge changes, resolve conflicts, and use advanced Git commands like reset and rebase. This helped me understand version control and project management in a better way.
