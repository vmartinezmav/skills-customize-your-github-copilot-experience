# 📘 Assignment: Testing Python Programs with unittest

## 🎯 Objective

Learn to write automated tests with Python's built-in `unittest` framework. Use tests to check expected behavior and find a bug in a small function.

## 📝 Tasks

### 🛠️ Test Basic Functions

#### Description
Complete the test methods in the starter code for the `add` and `is_even` functions. Run the tests with `python3 starter-code.py` and use the results to check your work.

#### Requirements
Completed program should:

- Use `unittest.TestCase` and appropriate assertion methods
- Test `add` with positive and negative numbers
- Test `is_even` with an even number, an odd number, and zero
- Run the test suite with `unittest.main()`


### 🛠️ Find and Fix a Function Bug

#### Description
Write tests for `calculate_discount`, which should return the final price after a percentage discount. Run the tests, use any failures to find the bug in the function, and correct its implementation.

#### Requirements
Completed program should:

- Test a regular discount, a 0% discount, and a 100% discount
- Confirm that a price of `100` with a `20` percent discount returns `80`
- Fix `calculate_discount` so all tests pass
- Run the complete test suite and confirm that it passes