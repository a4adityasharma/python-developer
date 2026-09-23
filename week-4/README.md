# Week 4 — Capstone Project (Automation / Data Handling)

This folder contains the Week 4 practice exercises and the selected capstone project for the Skill Nexis Python Programming Internship.

## Focus

Week 4 combines Python programming with automation and data handling.

The supplied Week 4 material provides three capstone choices:

1. Employee Data Analysis Project
2. COVID-19 Data Tracker
3. Email Automation Tool

For this submission, **Option 1 — Employee Data Analysis Project** has been implemented.

## Practice Set

### 1. Contact Book

Dictionary-based contact management.

### 2. Simple Calculator

Calculator implemented using functions.

### 3. Email Automation

SMTP email automation template using `smtplib`.

The template keeps sending disabled until the user's own SMTP configuration is supplied.

### 4. Weather App

Weather lookup using the OpenWeather API.

### 5. Cryptocurrency Price

Live cryptocurrency price lookup using the CoinGecko API.

## Capstone — Employee Data Analysis

### Tasks

- Load CSV using Pandas
- Calculate average salary
- Count employees by department
- Filter employees above a salary threshold
- Export filtered results to a new CSV

### Skill Gain

- Pandas
- CSV handling
- Data filtering
- Basic data analysis

## Folder Structure

```text
week-4/
│
├── practice/
│   ├── 01_contact_book.py
│   ├── 02_calculator.py
│   ├── 03_email_sending_template.py
│   ├── 04_weather_app_template.py
│   └── 05_crypto_price_template.py
│
├── capstone-employee-data-analysis/
│   ├── employee_data_analysis.py
│   ├── employees.csv
│   └── README.md
│
└── README.md
```

## Required Libraries

For the capstone:

```bash
pip install pandas
```

For the Weather and Crypto practice:

```bash
pip install requests
```

## How to Run

### Capstone

```bash
cd capstone-employee-data-analysis
python employee_data_analysis.py
```

### Practice

```bash
python practice/01_contact_book.py
python practice/02_calculator.py
python practice/03_email_sending_template.py
python practice/04_weather_app_template.py
python practice/05_crypto_price_template.py
```

## Week 4 Status

Completed