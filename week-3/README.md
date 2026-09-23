# Week 3 — Object-Oriented Programming (OOPs) + Libraries

This folder contains the practice exercises, assignments, and mini-project completed as part of Week 3 of the Skill Nexis Python Programming Internship.

## Topics Covered

- Classes
- Objects
- Constructors
- Inheritance
- Polymorphism
- Exception Handling
- `math`
- `random`
- `datetime`
- File Handling
- Python Libraries

## Practice Questions

1. Read a file and count total lines.
2. Merge two text files.
3. Load and analyze a CSV file using Pandas.
4. Plot a line graph using Matplotlib.
5. Create and read a JSON file.

## Assignments

### 1. Bank Account Class

A `BankAccount` class with methods for:

- Deposit
- Withdraw
- Display balance

### 2. Library Management System

An OOP-based library system supporting:

- Add books
- Remove books
- Issue books
- Return books
- Display books

### 3. Calculator Class with Exception Handling

A calculator implemented as a class with:

- Addition
- Subtraction
- Multiplication
- Division
- Invalid input handling
- Division-by-zero handling

## Mini Project — Billing System

An OOP-based billing system containing:

### Product Class

Attributes:

- Name
- Price
- Quantity

### Bill Class

Responsibilities:

- Store products
- Calculate subtotal
- Calculate tax
- Calculate final total
- Display the final bill in tabular format

## Folder Structure

```text
week-3/
│
├── practice/
│   ├── 01_count_lines.py
│   ├── 02_merge_text_files.py
│   ├── 03_pandas_csv_analysis.py
│   ├── 04_matplotlib_line_graph.py
│   ├── 05_json_create_read.py
│   ├── sample_data.csv
│   └── practice_data.json
│
├── assignment-1-bank-account/
│   └── bank_account.py
│
├── assignment-2-library-management/
│   └── library_management.py
│
├── assignment-3-calculator/
│   └── calculator.py
│
├── mini-project-billing-system/
│   ├── billing_system.py
│   └── README.md
│
└── README.md
```

## Required Libraries

The assignments use only Python's standard library.

The Pandas practice requires:

```bash
pip install pandas
```

The Matplotlib practice requires:

```bash
pip install matplotlib
```

## How to Run

Examples:

```bash
python practice/01_count_lines.py
python assignment-1-bank-account/bank_account.py
python assignment-2-library-management/library_management.py
python assignment-3-calculator/calculator.py
python mini-project-billing-system/billing_system.py
```

## Week 3 Status

Completed
