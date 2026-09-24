# CS 4300 Homework 1

## Introduction to Python & Unit Testing

This project contains seven Python tasks covering introductory Python programming concepts and unit testing with pytest

## Project Structure

```text
homework1/
├── src/
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   ├── task5.py
│   ├── task6.py
│   └── task7.py
├── tests/
│   ├── test_task1.py
│   ├── test_task2.py
│   ├── test_task3.py
│   ├── test_task4.py
│   ├── test_task5.py
│   ├── test_task6.py
│   └── test_task7.py
├── task6_read_me.txt
├── requirements.txt
└── README.md
```

## Setup

Create a Python virtual environment

```bash
python3 -m venv .venv
```

Activate the virtual environment

```bash
source .venv/bin/activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

## Running the Tests

Run all tests from the `homework1` directory using

```bash
pytest
```

## Tasks

### Task 1: Introduction to Python and Testing

Prints `Hello, World!` to the console and uses pytest to verify the output

### Task 2: Variables and Data Types

Demonstrates the use of integers, floating-point numbers, strings, and booleans and tests each data type

### Task 3: Control Structures

Uses an if statement to determine whether a number is positive, negative, or zero

Uses a for loop to find the first 10 prime numbers

Uses a while loop to calculate the sum of the numbers from 1 to 100

### Task 4: Functions and Duck Typing

Implements a `calculate_discount` function that calculates the final price of a product after applying a discount

The function supports integer and floating-point values and includes input validation

### Task 5: Lists and Dictionaries

Creates a list of favorite books and uses list slicing to retrieve the first three books

Creates a dictionary containing student names and student IDs

### Task 6: File Handling

Reads `task6_read_me.txt` and counts the number of words in the file

### Task 7: Package Management

Uses the NumPy package to calculate the average of a list of numbers

Pytest tests verify that the function works with different numeric values

## Testing

Each task has a corresponding pytest file located in the `tests` directory

The tests verify the expected behavior of each Python script and function

To run the complete test suite

```bash
pytest
```