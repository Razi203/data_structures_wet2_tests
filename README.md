# Data Structures Wet2 Tests
## Tests for Data Structures Wet Homework 2 - Spring 2024

These tests were made with <3 - jk you're on your own. I'm not fixing any issues unless some test is wrong!

### Your Not-So-Friendly Guide for Testing

All of the tests were randomly generated!

If you notice any mistakes, send me a message, open an issue on GitHub, or make a pull request.

Good Luck!

---

## Steps

### 0. Preparation

Make sure you are in the `Tests` directory in your terminal!

### 1. Modify Your Code

Add the following line to `pirates24b2.h` under the public section:
```cpp
output_t<int> get_pirate_rank(int pirateId);
```
Implement the function in `pirates24b2.cpp`. Remember to delete the function after you're done testing.

### 2. Set Up Your Environment

Move or copy your **zip file** to the `Tests` folder. Your file should be in the same directory as all the supplied files and folders.

**Note:** The `<zip file>` refers to the one you want to submit (containing your dry and all) meaning that you don't have to attach "wet2util.h" or "main24b2.cpp". A copy of `wet-verify.py` is attached if you want to test your zip file too!

The `Tests` directory structure should look like this:
```
Tests/
|__Files/
|__Unzipped/
.
.
.
|__compile.sh
|__new.sh
|__run.sh
|__<your zip file>
```

### 3. Grant Execute Permissions

Use `chmod` to grant access to the `.sh` files:
```bash
chmod +x compile.sh new.sh run.sh
```

**Common Bug:** "You don't have access to a.out"
To fix this, run:
```bash
chmod +x a.out
```

### 4. Compile Your Code

Run the `compile.sh` script each time you change your zip folder. You only need to do it once if there are no changes.
```bash
./compile.sh <your zip file>
```

### 5. Run the Tests

Run the tests using:
```bash
./run.sh
```

---

## Results

The tests check for time, output matching, and memory leaks. Each test will display whether it failed or not, and the number of failed tests will be printed at the end!

For the tests that failed, check the file `tests_failed.txt`.

For the differences in the output, check `Files/diff/<test number>`.

---

## Generating More Tests

All the Python code used is attached, so you can do whatever you want with it. To simply make new tests, use:
```bash
./new.sh
```
Be warned, it takes a lot of time, so you should change the values beforehand in the generate Python scripts.

- The file `generate_tests.py` holds two variables: `test_count` and `number_of_lines`.
- The file `input_generate.py` determines the range of values for IDs and money.

---
