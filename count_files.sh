#!/bin/bash

# Function to count files in a directory
count_files() {
    local dir="$1"
    local file_count=$(find "$dir" -type f | wc -l)
    echo "$file_count"
}

# Function to traverse directories recursively and count files
traverse_directories() {
    local parent_dir="$1"
    local total_files=0

    # Loop through each directory in the parent directory
    for dir in "$parent_dir"/*; do
        if [ -d "$dir" ]; then
            echo "Directory: $dir"
            files_in_dir=$(count_files "$dir")
            echo "Number of files: $files_in_dir"
            total_files=$((total_files + files_in_dir))

            # Recursively call the function for subdirectories
            total_files=$((total_files + $(traverse_directories "$dir")))
        fi
    done

    echo "$total_files"
}

# Main script
if [ $# -ne 1 ]; then
    echo "Usage: $0 <parent_directory>"
    exit 1
fi

parent_directory="$1"

if [ ! -d "$parent_directory" ]; then
    echo "Error: $parent_directory is not a directory."
    exit 1
fi

echo "Parent Directory: $parent_directory"
total_files=$(traverse_directories "$parent_directory")
echo "Total Number of Files: $total_files"
