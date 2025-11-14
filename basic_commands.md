# LINUX BASIC COMMANDS
## 1. Navigation Commands
### `pwd` – Print Working Directory
Shows the current location in the filesystem.
>pwd

Output example:
>/Users/Yana/projects

![alt text](IMG-20251114-WA0021-1.jpg)

### ls – List Directory Contents
Lists files and folders in the current directory.
>ls

   * ls -l → Detailed list (permissions, size, date)
   * ls -a → Shows hidden files (those starting with .)
   * ls -la → Combined

Output :
![alt text](IMG-20251114-WA0017-1.jpg) ![alt text](IMG-20251114-WA0018-1.jpg) ![alt text](IMG-20251114-WA0019-1.jpg) ![alt text](IMG-20251114-WA0020-1.jpg)

### `cd` – Change Directory
Moves into a directory.
>cd folder_name

Examples:
>cd Documents        # Go to Documents\
cd ..               # Go up one level\
cd /                # Go to root\
cd ~                # Go to home directory

Output:
![alt text](IMG-20251114-WA0015-1.jpg)

## 2. File and Directory Management
### `mkdir` – Make Directory
Creates a new folder.
>mkdir new_folder

Output:
![alt text](THISONE-1.jpg)

### `touch` – Create File
Creates an empty file.
>touch file.txt

![alt text](THISONE-2.jpg)

### `cp` – Copy Files or Directories

```bash
cp source.txt destination.txt
```

* Copy folder:


```bash
cp -r folder1 folder2
```
![alt text](IMG-20251114-WA0010-1.jpg)
---

### `mv` – Move or Rename Files

```bash
mv oldname.txt newname.txt
```

```bash
mv file.txt ~/Documents/     # Move file
```
![alt text](IMG-20251114-WA0010-2.jpg)
---

### `rm` – Remove Files

```bash
rm file.txt          # Delete file
rm -r folder_name    # Delete folder (recursively)
```
![alt text](IMG-20251114-WA0010-3.jpg)
⚠️ **Be careful!** There is no undo.

---

## ✅ 3. File Viewing & Editing

### `cat` – View File Contents

Displays content in terminal.

```bash
cat file.txt
```
![alt text](IMG-20251114-WA0010-4.jpg)
---

### `nano` – Edit Files in Terminal

A basic terminal-based text editor.

```bash
nano file.txt
```
![alt text](IMG-20251114-WA0009-1.jpg)
* Use arrows to move
* `CTRL + O` to save
* `CTRL + X` to exit

---

### `clear` – Clears the Terminal

```bash
clear
```

Shortcut: `CTRL + L`

---

## ✅ 4. System Commands

### `echo` – Print Text

Useful for debugging or scripting.

```bash
echo "Hello, World!"
```
![alt text](IMG-20251114-WA0007-1.jpg)
---

### `whoami` – Show Current User

```bash
whoami
```
![alt text](IMG-20251114-WA0008-1.jpg)
---

### `man` – Manual for Any Command

```bash
man ls
```
![alt text](IMG-20251114-WA0005-1.jpg)
Use `q` to quit the manual.

---

## ✅ 5. Searching and Finding

### `find` – Locate Files

```bash
find . -name "*.txt"
```

🔍 Finds all `.txt` files in current folder and subfolders.

---
![alt text](IMG-20251114-WA0008-4.jpg)
### `grep` – Search Inside Files

```bash
grep "hello" file.txt
```

🔍 Searches for the word `hello` inside `file.txt`.
![alt text](IMG-20251114-WA0006-1.jpg)
---

## ✅ 6. Helpful Shortcuts

| Shortcut   | Action                      |
| ---------- | --------------------------- |
| `Tab`      | Auto-complete files/folders |
| `↑ / ↓`    | Browse command history      |
| `CTRL + C` | Stop a running command      |
| `CTRL + L` | Clear screen                |

---

## ✅ 7. Bonus: Chaining Commands

* **Run multiple commands**:

```bash
mkdir test && cd test && touch hello.txt
```

* **Run only if previous command succeeds**: `&&`
* **Run regardless of success**: `;`

---


