# Diabetes Readmission Analysis — SQL & Python

## Project Overview
This project analyzes hospital encounters for patients with diabetes using Python and MySQL. It explores readmission patterns and how readmission rates vary by age group and length of hospital stay.

## Dataset
- **Source:** UCI Machine Learning Repository
- **Dataset:** Diabetes 130-US Hospitals for Years 1999–2008
- **Original records:** 101,766 hospital encounters
- **Original features:** 48 columns
- **Cleaned dataset:** 101,766 encounters and 45 data columns

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- MySQL
- SQL
- Git and GitHub

## Project Workflow
1. Downloaded and inspected the dataset.
2. Profiled data quality and missing values.
3. Removed three columns due to constant values or extensive missingness.
4. Saved the cleaned dataset as a CSV file.
5. Imported the cleaned data into MySQL.
6. Analyzed readmission patterns using SQL and Python.
7. Compared results across both tools.

## Key Findings
- 11.16% of encounters were labeled as readmitted within 30 days.
- The highest observed rate among age groups was 14.24% for the 20–30 age group.
- The highest observed rate by length of stay was 14.35% for encounters with a 10-day hospital stay.
- Readmission rates varied across age groups and lengths of hospital stay.

## Data Quality Notes
- The `weight` column was excluded because approximately 96.9% of its values were missing.
- The `examide` and `citoglipton` columns were excluded because all records had the same value.
- Other missing values were retained where appropriate.
- The available dataset version does not contain a patient identifier, so the analysis describes hospital encounters rather than unique patients.

## Limitations
This is a descriptive analysis. The observed patterns do not establish causation. Missing data and the absence of a patient identifier also limit interpretation.

## Repository Structure
```text
Portfolio_02_SQL_Python/
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   └── readmission_by_stay.png
├── sql/
│   └── readmission_analysis.sql
├── src/
├── requirements.txt
└── README.md
```

## Data Source
UCI Machine Learning Repository:  
https://archive.ics.uci.edu/dataset/296/diabetes%2B130-us+hospitals+for+years+1999-2008

**License:** CC BY 4.0

## Disclaimer
This project is for educational and portfolio purposes only. It is not intended for clinical decision-making.
