#!/bin/bash
# check_file.sh
# Usage: ./check_file.sh filename.txt

if [ $# -ne 1 ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

file="$1"
if [ -e "$file" ]; then
  echo "File exists: $file"
  echo "------ contents ------"
  cat -- "$file"
else
  echo "File '$file' does not exist."
  read -p "Create it now? (y/N): " ans
  case "$ans" in
    [Yy]*) touch "$file"; echo "Created $file"; echo "You can edit it using your favorite editor." ;;
    *) echo "Not creating file." ;;
  esac
fi
