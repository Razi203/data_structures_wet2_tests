#!/bin/bash

# Check if a zip file is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <zipfile>"
  exit 1
fi

ZIPFILE="$1"

# Create the unzipped directory if it doesn't exist
mkdir -p unzipped

# Remove all files from the unzipped directory except "wet2util.h" and "main24b2.cpp"
find unzipped -type f ! -name "wet2util.h" ! -name "main24b2.cpp" -exec rm -f {} +

# Unzip the provided zip file into the unzipped directory
unzip -q "$ZIPFILE" -d unzipped

# Change to the unzipped directory
cd unzipped || exit

# Compile the cpp files
g++ -std=c++11 -DNDEBUG -Wall *.cpp

# Move the resulting a.out file out of the unzipped directory
mv a.out ..

# Change back to the original directory
cd ..

# Optional: Remove the unzipped directory if you no longer need it
# rm -rf unzipped

echo "Compilation successful. The a.out file has been moved to $(pwd)."
