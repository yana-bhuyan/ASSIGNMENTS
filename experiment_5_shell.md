# What is Shell Script
   * A shell script is a text file containing a series of commands written for the shell to execute.
   * It automates tasks that you would normally run in the terminal.
   * Example: Running multiple commands, looping through files, making backups, etc.

## 1. Creating Your First Shell Script
   * Open a terminal and create a file:
   >nano hello.sh
   * Add the following content:
   >#!/bin/bas  
   
   >#This is a simple shell script
    
    >echo "Hello, World!"

   * >#!/bin/bash
    → called a shebang, tells the system which shell to use.
   * >echo 
    → prints text to the screen.
   * >"#"  → marks a comment.

   ![alt text](<Screenshot from 2025-08-25 09-06-11.png>)

   
   * Save and exit (CTRL+O, CTRL+X in nano).
   * Make it executable:
    >chmod +x hello.sh
   * Run it:
    >./hello.sh

✅ Output should be:
    
    > Hello, World!

![alt text](<Screenshot from 2025-08-25 11-16-52-1.png>)
##  2. Variables in Shell
You can store data in variables:
>#!/bin/bash
name="Yana"

>age=37

>echo "My name is $name"

>echo "I am $age years old"

![alt text](<Screenshot from 2025-08-24 08-28-35.png>)

![alt text](<Screenshot from 2025-08-24 08-29-29.png>)

⚠️ Note: No spaces around = when assigning values.

## 3. Taking User Input
>#!/bin/bash

>echo "Enter your name:"
read username

>echo "Hello, $username! Welcome to shell scripting."

   * >read → takes input from the user.
   * >$username → retrieves the value.

![alt text](<Screenshot from 2025-08-24 08-34-50.png>)

![alt text](<Screenshot from 2025-08-24 08-35-46.png>)
## 4. Conditional Statements (if-else)
>#!/bin/bash

>echo "Enter a number:"
read num

>if [ $num -gt 10 ]

>then
    echo "The number is greater than 10"

>else
    echo "The number is 10 or smaller"

>fi
   * >-gt → greater than.

![alt text](<Screenshot from 2025-08-24 08-34-50.png>)

![alt text](<Screenshot from 2025-08-24 08-35-46.png>)
   * Other operations:
    >-lt
    (less than),
    >-eq 
    (equal).
    
