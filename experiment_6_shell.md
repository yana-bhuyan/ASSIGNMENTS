# 🐚 Shell Scripting Tutorial!!
Shell scripting allows you to automate tasks in Linux/Unix by writing commands inside a file that the shell executes line by line.

## 1. 🔹 What is a Shell Script?
   * A shell is a command-line interpreter (e.g., `bash`, `zsh`, `sh`).
   * A shell script is a text file with a series of commands.
   * File usually has `.sh` extension, though not mandatory.

Example: `hello.sh`
>#!/bin/bash\
echo "Hello, World!"

![alt text](<Screenshot from 2025-08-28 23-31-39-2.png>)

![alt text](<Screenshot from 2025-08-28 23-33-59-1.png>)
Run it:
>chmod +x hello.sh  # make it executable
./hello.sh

Output:
>Hello, World!

![alt text](<Screenshot from 2025-08-28 23-33-59.png>)

## 2. 🔹 Variables
Variables store data (text, numbers, paths, etc.).
### Defining variables
>name="Yana"\
age=18

⚠️ No spaces around `=`.

### Accessing variables
>echo "My name is $name and I am $age years old."

Output:
>My name is Yana and I am 18 years old.

![alt text](<Screenshot from 2025-08-28 23-36-28.png>)

![alt text](<Screenshot from 2025-08-28 23-37-14.png>)
### Environment variables
>echo $HOME   # home directory\
echo $USER   # current user\
echo $PWD    # present working directory

![alt text](<Screenshot from 2025-08-28 23-39-07.png>)

![alt text](<Screenshot from 2025-08-28 23-39-43.png>)
## 3. 🔹 User Input
Read input from user with `read`.
>#!/bin/bash\
echo "Enter your favorite language:"\
read lang\
echo "You chose $lang"

![alt text](<Screenshot from 2025-08-28 23-42-29.png>)

![alt text](<Screenshot from 2025-08-28 23-43-11.png>)
## 4. 🔹 Conditional Statements (if-else)
>#!/bin/bash\
num=10\
if [ $num -gt 5 ]; then\
    echo "Number is greater than 5"\
else\
    echo "Number is less than or equal to 5"\
fi

![alt text](<Screenshot from 2025-08-28 23-50-30.png>)

![alt text](<Screenshot from 2025-08-28 23-51-15.png>)
Operators:
   
   *`-eq `(equal)
   * `-ne` (not equal)-ne (not equal)
   * `-gt` (greater than)
   * `-lt` (less than)
   * `-ge` (greater or equal)
   * `-le` (less or equal)

   ## 5. 🔹 Loops
   ### For loop
   >for i in 1 2 3 4 5\
do\
    echo "Number: $i"\
done

![alt text](<Screenshot from 2025-08-29 00-07-33.png>)

![alt text](<Screenshot from 2025-08-29 00-08-14.png>)

Or use a range:
>for i in {1..5}\
do\
    echo "Iteration $i"\
done\

![alt text](<Screenshot from 2025-08-29 00-10-24.png>)

![alt text](<Screenshot from 2025-08-29 00-10-53.png>)
### While loop
>count=1\
while [ $count -le 5 ]\
do\
    echo "Count: $count"\
    ((count++))   # increment\
done

![alt text](<Screenshot from 2025-08-29 00-32-06.png>)

![alt text](<Screenshot from 2025-08-29 00-32-36.png>)
### Until loop
Runs until condition becomes true.
>x=1\
until [ $x -gt 5 ]\
do\
    echo "Value: $x"\
    ((x++))\
done

![alt text](<Screenshot from 2025-08-29 00-35-34.png>)

![alt text](<Screenshot from 2025-08-29 00-35-59.png>)

## 6. 🔹 Functions
Encapsulate reusable code.
>greet() {\
    echo "Hello, $1"\
}\
greet Yana\
greet World

Output:
>Hello, Yana\
Hello, World

![alt text](<Screenshot from 2025-08-29 00-38-48.png>)

![alt text](<Screenshot from 2025-08-29 00-40-11.png>)
## 7. 🔹 Command Line Arguments
Access arguments passed to script:
>#!/bin/bash\
echo "Script name: $0"\
echo "First argument: $1"\
echo "Second argument: $2"\
echo "All arguments: $@"\
echo "Number of arguments: $#"

Run:
>./script.sh apple banana

Output:
>Script name: ./script.sh\
First argument: apple\
Second argument: banana\
All arguments: apple banana\
Number of arguments: 2

![alt text](<Screenshot from 2025-08-29 00-54-04.png>)

![alt text](<Screenshot from 2025-08-29 00-54-57.png>)
## 8. 🔹 Arrays
>fruits=("apple" "banana" "cherry")\
echo "First fruit: ${fruits[0]}"\
for fruit in "${fruits[@]}"; do\
    echo "Fruit: $fruit"\
done

![alt text](<Screenshot from 2025-08-29 01-37-36.png>)

![alt text](<Screenshot from 2025-08-29 01-38-19.png>)
## 9. 🔹 Useful Commands in Scripts
   * `date` → show current date/time
   * `whoami` → show current user
   * `ls` → list files
   * `pwd` → print working directory
   * `cat` → read file contents

   ![alt text](<Screenshot from 2025-08-29 01-35-50.png>)

   ![alt text](<Screenshot from 2025-08-29 01-36-15.png>)
## 10. 🔹 A Practical Example
Backup script (`backup.sh`):
>#!/bin/bash
#Backup home directory to /tmp\
backup_file="/tmp/home_backup_$(date +%Y%m%d%H%M%S).tar.gz"\
tar -czf $backup_file $HOME\
echo "Backup saved to $backup_file"

Run:

>./backup.sh


