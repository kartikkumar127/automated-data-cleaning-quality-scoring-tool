# Automated-Data-Cleaning-Quality-Scoring-Tool
A Streamlit-based web application that automates data cleaning for CSV and Excel files and provides a **data quality score** before and after cleaning.

## Features
- Upload multiple CSV / Excel files
- Remove missing values & duplicates
- Fill missing values (Mean, Median, Mode)
- Strip extra spaces & normalize columns
- Convert numeric data types
- Drop selected columns
- Data quality scoring (0–100)
- Download cleaned dataset

## Tech Stack
- Python
- Pandas
- Streamlit

## Data Quality Metrics
- Missing values
- Duplicate rows
- Formatting issues
- Overall quality score

## How to Run
#Step 1: Clone the Repository

git clone https://github.com/kartikkumar127/automated-data-cleaning-quality-tool.git

cd automated-data-cleaning-quality-tool

#Step 2: Install Dependencies

pip install pandas
pip install streamlit

#Step 3: Run Streamlit App

streamlit run app.py

## Business Problem

Organizations often work with messy data containing missing values, duplicates, and inconsistent formatting.
This leads to incorrect insights, slow analysis, and unreliable reporting.

## Solution

This project provides a no-code automated data cleaning tool that:

Cleans CSV & Excel files

Removes duplicates and missing values

Standardizes data

Calculates a Data Quality Score (0–100)

## Use Cases

Prepare data for Power BI / SQL / Excel

Clean large datasets efficiently
Enable non-technical users to clean data

Standardize data across teams

## Business Impact

Saves 60–70% time spent on data cleaning

Improves data accuracy & consistency

Handles large real-world datasets
