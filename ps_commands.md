# Linux Process Management
It covers essential Linux commands for monitering and managing processes. Each section explains what the command does, why it's useful and include examples .

## Table of Contents
* Show all processes
* Process tree (pstree -p)
* Real-Time Monitering (top)
* Adjust Process Priorty (nice, renice)
* CPY Affinity (taskset)
* I/O Scheduling Priority (ionice)
* File Descriptors (Isof)
* Trace System Calls (strace)
* Find Process Using a Port (fuser)
* Per-Process Statistics (pidstat)
* Control Groups (cgroups)

### 1. Show All Processes
> ps aux

   * a → shows processes for all users
   * u → shows the user/owner of the process
   * x → show processes not attached to terminal

### Output:
![alt text](<Screenshot from 2025-09-27 12-00-55.png>)  ![alt text](<Screenshot from 2025-09-27 12-01-42.png>)

   * Useful for system monitering , troubleshooting high CPU/memory usage or finding PIDS
## 2. Process Tree
>pstree -p

   * It shows processes in hiearchical tree structure
   * It helps understand parent-child relationships
### Output:
![alt text](<Screenshot from 2025-09-27 12-08-38.png>) ![alt text](<Screenshot from 2025-09-27 12-08-52.png>) ![alt text](<Screenshot from 2025-09-27 12-09-16.png>)

   * Great for debugging orphan processes( an orphan process is a process whose parent has  terminated[exited]while the child is still running)or seeing how daemons and shells are linked.
## 3. Real-Time Monitering
> top


   * Interactive command to monitor CPU, memory, and tasks in real time.
   * Navigate:
     * press q →  quit
     * press k →  kill a process
     * press h →  help
### Output:
![alt text](<Screenshot from 2025-09-27 12-23-03.png>)

## 4. (1) Adjust Process Priority
   * Start a process with priority
   > nice -n 10 sleep 300 &

   * -n 10 → sets nice value = 10 (lower priority)
   * Background job [1] 57730 created
### Output:
![alt text](<Screenshot from 2025-09-27 14-09-01.png>)

### (2) Changing priority of running process
>renice -n -5 -p 57730

   * Used when you want critical tasks to run faster or background jobs to run slower.
### Output:
![alt text](<Screenshot from 2025-09-27 20-03-17.png>)
## 5. CPU Affinity (Bind process to CPU Core)
> taskset -cp 62745

   * It shows CPU cores a process can use.
### Output:

![alt text](<Screenshot from 2025-09-28 06-07-52.png>)
   * Restrict to core 1:
   > taskset -cp 1 62745

### Output:
![alt text](<Screenshot from 2025-09-28 06-23-13.png>)

   * Useful for performance tuning, ensuring tasks run on specific cores.
## 6. I/O Scheduling Priority
> ionice -c 3 -p 63095

> ionice -p 63095

   * Control disk I/O priority of a process.
   * set pid 3050's IO scheduling class to idle.
### Output:
![alt text](<Screenshot from 2025-09-28 06-29-48.png>)
   * prevents background jobs (like branches) from slowing down disk access.
## 7. File Descriptors used by a Process
>Isof -p 

   * It lists files opened by a process ie checks which files, sockets or devices a process is using.
### Output:
![alt text](<Screenshot from 2025-09-28 06-57-02.png>)
## 8. Trace System Calls of a Process
> strace -p 

   * Attaches to a process and shows system calls.
### Output:
![alt text](<Screenshot from 2025-09-28 16-24-48.png>)
   * Used in debugging programs by checking file, network and interactions.
## 9. Find Process Using a Port
> sudo fuser -n tcp 8080

   * system prompts tp enter password
   * It finds which process is bound to a TCP/UDP port
   * used in debugging web servers, databases, or services.
   * PID 4553 is using port 8080
## 10. Pre-Process Statistics
>pidstat -p 4553 2 3

   * It displays detailed CPU usage for a process over time.
     * 2 = interval (seconds)
     * 3 = number of reports
### Output:
![alt text](<Screenshot from 2025-09-28 17-09-52.png>)
   * It is usually considered better than top when monitoring one specified process
## 11. Control Groups (cgroups) for Resource Limits
### 1. Create a cgroup:
   * Before proceeding to create control groups (cgroups), it is necessary to first install the relevant cgroup tools on your Linux system. These tools, such as cgcreate, cgset, and cgexec, are essential utilities that allow for the easy definition, configuration, and management of resource limits---like CPU time, memory, and disk I/O--- for processes within the kernel's cgroup framework. This prerequisite installation ensures that the commands you will use to set up and manage cgroups are available and functional.
   > sudo cgcreate -g cpu,memory:/testgroup
### Output:
![alt text](<Screenshot from 2025-09-28 17-40-43.png>)
### 2. Limit CPU and Memory
   * First identify if your system is running on cgroup v1 or cgroup v2.
     * If running on cgroup v1, files like cpu.cfs_quota_us and memory.limit_in_bytes exist but if on v2 cpu.max,memory.max exist
     * cgroup v1 or cgroup v2 can be identified using
     > mount | grep cgroup
   ### Examples:
   ![alt text](<Screenshot from 2025-09-28 17-45-24.png>)
   * My system is running on cgroup v2

   > echo "50000 100000" | sudo tee /sys/fs/cgroup/testgroup/cpu.max\
   echo 100M | sudo tee /sys/fs/cgroup/testgroup/testgroup/memory.max

### Output:
![alt text](<Screenshot from 2025-09-28 17-49-39.png>)
   * Add process (PID 3050) to cgroup:
   > echo 3050 | sudo tee /sys/fs/cgroup/cpu/testgroup/cgroup.procs

### Output:
![alt text](<Screenshot from 2025-09-28 17-53-52.png>)
   * These commands enforce resource limits on a specific process by utilizing Linux Control Groups (cgroups). THe result is that the process identified by is placed into the testgroup cgroup, where it is immediately constrained  to use a maximum of 50% of a singlle CPU coree (by setting the cpu.max value to 50000 out of 100000) and is limited to 100 Mgeabytes (MB) of total memory (by setting the memory.max value). This practice is crucial for resource isolation, preventing a potentially runaway or resource-intensive process from consuming all available system resources and ensuring fair sharing among all running applications.