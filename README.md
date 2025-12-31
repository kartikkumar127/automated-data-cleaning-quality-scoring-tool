# automated-data-cleaning-quality-scoring-tool
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
>>>Step 1: Clone the Repository
git clone https://github.com/yourusername/automated-data-cleaning-quality-tool.git
cd automated-data-cleaning-quality-tool

>>>Step 2: Install Dependencies
pip install -r requirements.txt

>>>Step 3: Run Streamlit App
streamlit run app.py
