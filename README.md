# Zomato Bengaluru Restaurant Data Analysis

A data analysis project using the Zomato Bengaluru restaurant dataset. The project covers data cleaning, exploratory data analysis, SQL analysis, Excel exploration, and Power BI dashboard development.

## Tools
- Python — data cleaning, preprocessing, EDA
- Excel — pivot tables and initial exploration
- SQL — aggregations, filtering and grouped analysis
- Power BI — dashboard, KPIs and interactive analysis

## Repository Structure
```text
zomato-bengaluru-data-analysis/
├── data/
│   └── zomato.xlsx
├── python/
│   ├── Zomato_Data_Cleaning.py
│   └── Zomato_EDA.py
├── sql/
├── excel/
├── powerbi/
├── report/
└── README.md
```

## Python Workflow
1. Load the original Excel dataset.
2. Remove unnamed columns.
3. Inspect and handle missing values.
4. Remove exact duplicate rows.
5. Clean rating and cost fields.
6. Standardize selected categorical text fields.
7. Treat cost outliers using the IQR method.
8. Create a `cost_category` derived column.
9. Save the cleaned dataset.

## EDA Covered
- Rating distribution
- Average cost distribution
- Vote distribution
- Restaurant count by location
- Restaurant count by restaurant type
- Restaurant count by cuisine

## Planned Deliverables
- Cleaned dataset
- Python cleaning and EDA scripts
- Excel workbook with pivots and charts
- SQL analysis queries
- Multi-page Power BI dashboard
- Insights report

## Important
The Python scripts originally used local Windows paths. Before publishing, the scripts should use project-relative paths so they work on another computer.

## How to Run
```bash
pip install pandas numpy matplotlib seaborn openpyxl
python python/Zomato_Data_Cleaning.py
python python/Zomato_EDA.py
```
