# Retail Sales & Customer Analytics

## Overview
This project performs **end-to-end analytics** on a retail sales dataset to uncover insights about **revenue trends, customer behavior, and product performance**. The analysis includes data cleaning, exploratory data analysis (EDA), and visualization of key metrics.

The project outputs **graphs** and a **PDF report** summarizing the analysis.

---

## Features
- **Data Cleaning & Transformation**  
  - Handles missing values  
  - Calculates `revenue` per order  

- **Exploratory Data Analysis (EDA)**  
  - Monthly revenue trends  
  - Top customers by lifetime value  
  - Average order value by city  
  - Product performance (total revenue per product)  
  - Weekly revenue patterns  
  - Correlation heatmap of key metrics  

- **Visualization**  
  - Each chart can be displayed individually or exported to a **single PDF** (`Retail_Analysis.pdf`) with one chart per page  

- **Database Integration**  
  - Uses SQLite (`retail.db`) to store `sales` and `customers` tables  
  - SQL queries via `pandas.read_sql`  

---

## Technologies Used
- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- SQLAlchemy (SQLite backend)  

---

## Project Structure
```
project/
│
├── data/
│   ├── sales.csv        # Sales dataset
│   └── customers.csv    # Customers dataset
│
├── scripts/
│   ├── eda_multi_charts.py   # EDA & visualization script
│   ├── load_to_sql.py        # Load CSV data into SQLite
│
├── retail.db            # SQLite database (after running load_to_sql.py)
├── Retail_Analysis.pdf  # Generated PDF report with all charts
└── README.md            # Project documentation
```

---

## Usage

1. **Setup Environment**
```bash
pip install pandas matplotlib seaborn sqlalchemy
```

2. **Load Data into Database**
```bash
python scripts/load_to_sql.py
```

3. **Run EDA & Generate PDF**
```bash
python scripts/eda_multi_charts.py
```

4. **Output**
- Interactive charts appear one by one  
- PDF report `Retail_Analysis.pdf` generated in project root  

---

## Notes
- Ensure **customer_id format** in `sales.csv` and `customers.csv` matches (e.g., `C001` vs `1`).  
- Revenue is calculated as:  
```
revenue = quantity * price
```  
- Modify or extend visualizations in `eda_multi_charts.py` as per your analysis requirements.  

---

## Author
Prabhjot Singh