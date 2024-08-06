# Data Structures Wet2 Tests
Tests for Data Structures Wet Homework 2 - Spring 2024

The test suite is designed to help you verify the correctness of your zip file before submission. This way you ensure that your file works as expected and that no files are missing or mixed up at submission!

**###### FOR TESTS TO VERIFY YOUR PIRATE RANK, VISIT: [Eilon's Tests (including custom rank testing)](https://github.com/eilon-code/data_structures_wet2_tests) ######**

These tests were created with ❤️ - Just kidding! You’re on your own unless there’s an error in the tests themselves!

## Your Not-So-Friendly Guide for Testing

All tests were randomly generated! If you notice any mistakes, feel free to message me, open an issue on GitHub, or make a pull request.

Good Luck!

## Steps

0. Ensure you are in the Tests directory in your terminal.

1. Move or copy your *zip file* into the Tests folder. Your file should be in the same directory as all the supplied files and folders.

**Note:** The \<zip file\> refers to the one you want to submit (containing your dry and all). You do not need to attach "wet2util.h" or "main24b2.cpp". A copy of wet-verify.py is included if you want to test your zip file too!

    ```
    Tests/
    ├── Files/
    ├── Unzipped/
    ├── compile.sh
    ├── new.sh
    ├── run.sh
    └── <your zip file>
    ```

2. Use `chmod` to gain access to the .sh files: `chmod +x compile.sh new.sh run.sh`

    **Common bugs**:
- If you encounter "You don't have access to a.out", fix it by running `chmod +x a.out`
- If you encounter "unzip/zip errors", fix it by running `sudo apt install zip unzip`

4. Run [compile.sh](compile.sh) each time you change your zip folder. You only need to do this once if no changes are made. Use `./compile.sh <your zip file>`

5. Run the tests using `./run.sh`

## Results

The tests check for:
- Time
- Output matching
- Memory Leaks

Each result will be displayed as passed or failed, and the total number of failed tests will be printed at the end.

For details on failed tests, check the file *tests_failed.txt*.

For differences in the output, check *Files/diff/\<test number\>*.

## Generating More Tests

All the Python code used for test generation is included. You can create new tests using `./new.sh`. However, note that this process can be time-consuming, so you may want to adjust the values in the generation scripts beforehand.

- The file *generate_tests.py* holds two variables: test count and the number of lines used.
- The file *input_generate.py* determines the range of values for IDs and money.
