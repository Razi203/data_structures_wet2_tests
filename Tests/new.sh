rm -rf files/outputs
rm -rf files/inputs
rm -rf files/diffs
rm -rf files/my_out

# Prompt the user for input
read -p "Enter the number of tests: " test_count
read -p "Enter the number of lines per test file: " line_count

# Run the Python script with the provided inputs
python3 generate_tests.py "$test_count" "$line_count"
# ./run.sh