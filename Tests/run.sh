#!/bin/bash

# Define directories
input_dir="./files/inputs"
output_dir="./files/outputs"
my_out_dir="./files/my_out"
diffs_dir="./files/diffs"
temp_dir="./files/temp"

# Create directories if they don't exist
mkdir -p "$my_out_dir"
mkdir -p "$diffs_dir"
mkdir -p "$temp_dir"

# File to save failed tests
failed_tests_file="failed_tests"

# ANSI color codes
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# ASCII Art Title
echo -e "${BLUE}"
echo '          _______ _________       _______       _________ _______  _______ _________ _______ '
echo '|\     /|(  ____ \\__   __/      / ___   )      \__   __/(  ____ \(  ____ \\__   __/(  ____ \'
echo '| )   ( || (    \/   ) (         \/   )  |         ) (   | (    \/| (    \/   ) (   | (    \/'
echo '| | _ | || (__       | |             /   )         | |   | (__    | (_____    | |   | (_____ '
echo '| |( )| ||  __)      | |           _/   /          | |   |  __)   (_____  )   | |   (_____  )'
echo '| || || || (         | |          /   _/           | |   | (            ) |   | |         ) |'
echo '| () () || (____/\   | |         (   (__/\         | |   | (____/\/\____) |   | |   /\____) |'
echo '(_______)(_______/   )_(         \_______/         )_(   (_______/\_______)   )_(   \_______)'
echo -e "${NC}\n"

# Initialize counters
total_tests=0
failed_tests=0
failed_tests_list=""

# Iterate over all input files
for input_file in "$input_dir"/input*.txt; do
  # Increment the total test counter
  ((total_tests++))

  # Extract the number from the input file name
  base_name=$(basename "$input_file")
  num="${base_name//[^0-9]/}"

  # Define the corresponding output and my output files
  output_file="$output_dir/output${num}.txt"
  my_output_file="$my_out_dir/my${num}.txt"
  diff_file="$diffs_dir/diff${num}.txt"
  valgrind_log="$temp_dir/valgrind${num}.log"

  # Print test running information
  echo -e "${BLUE}Running test ${num} >>>${NC}"

  # Run the a.out program with the input file and measure execution time
  start_time=$(date +%s%3N)
  ./a.out < "$input_file" > "$my_output_file"
  end_time=$(date +%s%3N)
  execution_time=$((end_time - start_time))

  # Print execution time
  echo -e "Test ${num} execution time: ${YELLOW}${execution_time}ms${NC}"

  # Check if execution time is within 15 seconds
  if [ "$execution_time" -le 15000 ]; then
    time_complexity="pass"
    echo -e "Time Complexity (<= 15 sec): ${GREEN}pass${NC}"
  else
    time_complexity="fail"
    echo -e "Time Complexity (<= 15 sec): ${RED}fail${NC}"
  fi

  # Compare my output file with the expected output file
  if diff -q "$my_output_file" "$output_file" > /dev/null; then
    output_match=true
    echo -e "Test Output: ${GREEN}Passed${NC}"
    # Remove diff file if it exists
    [ -f "$diff_file" ] && rm "$diff_file"
  else
    output_match=false
    diff "$my_output_file" "$output_file" > "$diff_file"
    echo -e "Test Output: ${RED}Failed${NC}"
  fi

  # Run Valgrind memory check
  valgrind --leak-check=full --log-file="$valgrind_log" ./a.out < "$input_file" > /dev/null

  # Check for memory errors
  if grep -q "ERROR SUMMARY: 0 errors" "$valgrind_log"; then
    valgrind_success=true
    echo -e "Memory Leak: ${GREEN}Passed${NC}"
  else
    valgrind_success=false
    echo -e "Memory Leak: ${RED}Failed${NC}"
  fi

  # Track failed tests
  if [ "$output_match" = false ] || [ "$valgrind_success" = false ] || [ "$time_complexity" = "fail" ]; then
    ((failed_tests++))
    failed_tests_list+="${num} "
  fi

  # Add a blank line between tests
  echo ""
done

# Print summary of failed tests
echo -e "\nTotal tests failed: ${RED}${failed_tests}${NC}"

# Save failed tests to a file
echo "$failed_tests_list" > "$failed_tests_file"

# Print final result message in ASCII art
if [ "$failed_tests" -gt 0 ]; then
    echo -e "${RED} _______    _______   _________   _          _______    ______  "
    echo -e "(  ____ \\  (  ___  )  \\__   __/  ( \\        (  ____ \\  (  __  \\ "
    echo -e "| (    \\/  | (   ) |     ) (     | (        | (    \\/  | (  \\  )"
    echo -e "| (__      | (___) |     | |     | |        | (__      | |   ) |"
    echo -e "|  __)     |  ___  |     | |     | |        |  __)     | |   | |"
    echo -e "| (        | (   ) |     | |     | |        | (        | |   ) |"
    echo -e "| )        | )   ( |  ___) (___  | (____/\\  | (____/\\  | (__/  )"
    echo -e "|/         |/     \\|  \\_______/  (_______/  (_______/  (______/ "
    echo -e "                                                                ${NC}"
else
    echo -e "${GREEN} _______    _______    _______    _______    _______    ______  "
    echo -e "(  ____ )  (  ___  )  (  ____ \\  (  ____ \\  (  ____ \\  (  __  \\ "
    echo -e "| (    )|  | (   ) |  | (    \\/  | (    \\/  | (    \\/  | (  \\  )"
    echo -e "| (____)|  | (___) |  | (_____   | (_____   | (__      | |   ) |"
    echo -e "|  _____)  |  ___  |  (_____  )  (_____  )  |  __)     | |   | |"
    echo -e "| (        | (   ) |        ) |        ) |  | (        | |   ) |"
    echo -e "| )        | )   ( |  /\\____) |  /\\____) |  | (____/\\  | (__/  )"
    echo -e "|/         |/     \\|  \\_______)  \\_______)  (_______/  (______/ "
    echo -e "                                                                ${NC}"
fi

# Clean up temporary directory
rm -rf "$temp_dir"
