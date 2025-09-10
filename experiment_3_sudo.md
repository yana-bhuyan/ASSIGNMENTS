# Sudo and Admin managment commands
## ✅ 1. sudo – Run Commands as Administrator
`sudo` (SuperUser DO) allows you to run commands with root privileges.
>sudo command

Examples:
>sudo apt update      # Run package update as admin

>sudo reboot          # Reboot system

## ✅ 2. User Management (Linux/macOS only)
### 👤 `adduser` – Create a New User
>sudo adduser newusername

![alt text](<Screenshot from 2025-08-28 22-35-28.png>)
### 🔑 `passwd` – Change User Password
>sudo passwd newusername


### 👥 `usermod` – Modify User Account
Add a user to a group:
>sudo usermod -aG groupname username

Example:
>sudo usermod -aG sudo alice     # Give 'alice' sudo access

### ❌ `deluser` – Delete a User
>sudo deluser username

To remove the user's home directory
>sudo deluser --remove-home username

## ✅ 3. File Permissions with chmod and chown
### 🔐 `chmod` – Change File Permissions
Basic syntax:
>chmod [permissions] file

Common Usage:
>chmod 755 script.sh     # Owner: read/write/execute; others: read/execute

>chmod +x file.sh        # Add execute permission

>chmod -x file.sh        # Remove execute permission

### 🔢 What Do Numbers Mean?
| Number | Permission             |
| ------ | ---------------------- |
| 7      | read + write + execute |
| 6      | read + write           |
| 5      | read + execute         |
| 4      | read only              |
| 0      | no permission          |

Example:
>chmod 644 file.txt
#Owner: read/write, Group: read, Others: read

### 👑 chown – Change File Owner
>sudo chown user:group file

Example:
>sudo chown alice:alice myfile.txt
## ✅ 4. Disk Usage & System Info
### 💽 df – Disk Space Usage
>df -h

![alt text](<Screenshot from 2025-08-28 22-46-03.png>)
Shows mounted partitions with human-readable sizes.
### 📁 du – Directory Size
>du -sh folder_name

![alt text](<Screenshot from 2025-08-28 22-48-38.png>)

### 🖥️ top – Live System Processes
>top

![
](<Screenshot from 2025-08-28 22-49-44.png>)

![alt text](<Screenshot from 2025-08-28 22-49-58.png>)

![alt text](<Screenshot from 2025-08-28 22-50-07.png>)
Press `q` to quit.

Alternative: `htop` (better UI, needs to be installed)
## ✅ 5. Networking Commands
### 🌐 ping – Check Network Connectivity
>ping google.com

![alt text](<Screenshot from 2025-08-28 22-52-09.png>)

Press `CTRL + C` to stop.
### 📶 ifconfig or ip a – Show IP Address & Network Info
>ip a

>ifconfig   # May require sudo or installation

### 🔍 netstat – Show Active Network Connections
>netstat -tuln

![alt text](<Screenshot from 2025-08-28 22-55-52.png>)

Or use:
>ss -tuln   # Faster alternative

## ✅ 6. Package Management
### For Ubuntu/Debian (APT):
>sudo apt update            # Refresh package list

>sudo apt upgrade           # Upgrade installed packages

>sudo apt install git       # Install a package

>sudo apt remove git        # Uninstall a package

### For macOS (Homebrew):
>brew install git

## ✅ 7. Process Management
### 🔎 ps – Show Running Processes
>ps aux

![alt text](<Screenshot from 2025-08-28 22-57-23.png>)

### 🔫 kill – Kill a Process
>kill <PID>


Example:
>kill 12345

Force kill:
>kill -9 12345
## ✅ 8. Shutdown and Reboot
>sudo shutdown now        # Immediate shutdown

>sudo shutdown -r now     # Immediate reboot