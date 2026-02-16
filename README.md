# TuteDude_Ass_1
# Linux Commands Assignment

Name: Heeralal Kumar Sahni  
Course: B.Tech CSE  
Environment Used: Git Bash on Windows  

---

## 1. Creating and Renaming Files

### Create a directory
Command:
mkdir test_dir

Explanation:
This command creates a new directory named test_dir.

---

### Go inside the directory
Command:
cd test_dir

Explanation:
This command changes the current directory to test_dir.

---

### Create an empty file
Command:
touch example.txt

Explanation:
This command creates a blank file named example.txt.

---

### Rename the file
Command:
mv example.txt renamed_example.txt

Explanation:
This command renames example.txt to renamed_example.txt.

---

## 2. Viewing File Contents

(Note: Since I am using Windows, I used the hosts file instead of /etc/passwd.)

### Display file content
Command:
cat /c/Windows/System32/drivers/etc/hosts

Explanation:
This command displays the content of the file.

---

### Display first 5 lines
Command:
head -5 /c/Windows/System32/drivers/etc/hosts

Explanation:
This command shows the first 5 lines of the file.

---

### Display last 5 lines
Command:
tail -5 /c/Windows/System32/drivers/etc/hosts

Explanation:
This command shows the last 5 lines of the file.

---

## 3. Searching for a Pattern

Command:
grep "localhost" /c/Windows/System32/drivers/etc/hosts

Explanation:
This command searches for the word "localhost" in the file.

---

## 4. Zipping and Unzipping

(Note: zip was not available in Git Bash, so PowerShell was used.)

### Compress folder
Command:
powershell Compress-Archive test_dir test_dir.zip

Explanation:
This command creates a zip file of the test_dir folder.

---

### Extract zip file
Command:
powershell Expand-Archive test_dir.zip unzipped_dir

Explanation:
This command extracts the zip file into a new folder.

---

## 5. Downloading a File

Command:
curl -O https://example.com/sample.txt

Explanation:
This command downloads a file from the internet.

---

## 6. Changing Permissions

### Create file
Command:
touch secure.txt

### Make file read-only
Command:
chmod 444 secure.txt

Explanation:
This command makes the file read-only for all users.

---

## 7. Environment Variable

### Set variable
Command:
export MY_VAR="Hello, Linux!"

### Check variable
Command:
echo $MY_VAR

Explanation:
The export command sets an environment variable and echo displays its value.

---

## Conclusion

All commands were successfully executed using Git Bash on Windows. Screenshots of all outputs are attached in the document.