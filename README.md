# data_structures_wet2_tests
Tests For Data Structures Wet Homework 2 - Spring 2024

These Tests were made with <3 - jk you're on your own I'm not fixing any issues unless some test is wrong!

## Your not so Friendly Guide For Testing

All of the tests were randomly generated!

If you notice any mistakes send me a message / open an issue in github or you can make pull request.

Good Luck!

## steps

0. Make sure you are in the Tests directory in your terminal!

1. Move/Copy your *zip file* to inside the Tests folder (your file should be in the same directory as all of the supplied files and folders).
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

2. use chmod to gain access to .sh files: ```chmod +x compile.sh new.sh run.sh```

3. run [compile.sh](compile.sh) each time you change your zip folder, you only need to do it once if not changed. using ``` ./compile.sh <your zip file>``` 

4. run the tests using ```./run.sh```

## Results

The tests check for Time, Output matching, Memory Leaks. 

Each one is displayed whether faild or not and the number of failed tests will be printed at the end!

For the tests failed check the file *tests_failed.txt*

For the differences in the output check *Files/diff/<test number>* 


## Generating More Tests

All of the python code used is attached so do what ever you want with it, to simply just make new tests use ```./new.sh``` , but be warned it takes a lot of time so you should 
change the values before hand in the generate python scripts.

file *generate_tests.py* holds two variables - test count & the number of lines used

file *input_generate.py* determines the range of values for ids and money
