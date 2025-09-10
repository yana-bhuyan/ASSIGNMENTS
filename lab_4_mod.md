# Starter kit
## Script: starter_kit.sh
![alt text](<Screenshot from 2025-09-10 18-59-02-1.png>)

   * "#!/bin/bash --- Shebang line. It tells the system to use bash to execute this script.
   * Comments (# ...) --- Explain what the script does (not executed)"
   * "mkdir" = "make directory"
   * -p = creates parent directories only if they don't exist, preventing error.
   * project/(scripts,docs,data) uses brace expansion to create:
   project/docs/

   project/data/ (All inside the project/folder).
      * "echo "text" prints text.
      * .> redirects the output into a file. If the file doesn't exist, it creates it; if it exists, it overwrites.
      * Example: echo "#Project Root" > project/README.md creates a file called README.md in the project/folder with heading "# Project Root".
## Output
![alt text](<Screenshot from 2025-09-10 19-17-44.png>)
