# Quantium Sales Inisght Dashboard

This project is a data analysis and interactive dashboard built as part of the **Quantium Virtual Experience Program** on Forage. It explores sales trends for Quantium's "Pink Morsel" product and allows region-specific insights through an interactive interface.

---

## Project Overview

The goal of this project was to help **Soul Foods** (a Quantium client) determine whether **sales increased after a price change on January 15, 2021**. The dashboard uses sales data from three CSV files and features:

- **Line chart of daily sales over time**
- **Region filter via radio buttons** (north, east, south, west, all)
- A custom pink-themed UI
- Automated testing with Pytest & Dash’s testing tools
- A CI-friendly test script (`run_tests.sh`)

---

## File Structure
```bash
quantium-starter-repo/ 
│ ├── data/ 
│ ├── daily_sales_data_0.csv 
│ ├── daily_sales_data_1.csv 
│ ├──  daily_sales_data_2.csv 
│ └── formatted_sales_data.csv  # Processed and cleaned dataset 
│ ├── assets/ 
│ └── style.css
├── dash_app.py         # Main Dash application 
├── process_data.py       
├── test_dash_app.py  
├── run_tests.sh        # Bash script to run tests (CI-ready) 
├── .gitignore          # Ignores venv and temp files 
└── README.md 
```
---

## How to Run the App

1. **Clone this repo**
2. **Create a virtual environment** (or activate one)
3. Install dependencies:
    ```bash
    pip install dash pandas plotly pytest dash[testing]
    ```
4. Run the Dash app:
    ```bash
    python dash_app.py
    ```
5. Open on browser if not automatically

---

## Running Tests
To run the test suite with Pytest:
```bash
./run_tests.sh
```
💡Use Git Bash, WSL, or macOS/Linux terminal to run the script.

---

## Key Insights
Using the dashboard, it’s clear that: Sales increased significantly after the Pink Morsel price change on Jan 15, 2021.

---

## Tech Stack
- Python 3.11
- Dash
- Pandas
- Selenium
- Pytest
- Bash scripting (for CI compatibility)

---

Quantium Software Engineering Job Simulation on Forage - April 2025

 * Developed an interactive Dash application that enabled the client to assess
   the impact of price changes on sales and profitability.
 * Implemented a test suite to verify the Dash application is working and a bash
   script to automatically run the test suite.
 * Developed an intuitive user interface to make the application enjoyable and
   engaging for the client to interact with.