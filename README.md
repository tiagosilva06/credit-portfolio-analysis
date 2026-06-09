# 📊 Credit Portfolio Analysis

A data analysis project built with PySpark and Python to analyze credit portfolio profitability, default rates, and financial sensitivity across loan vintages (safras).

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Features](#features)
- [Key Analysis](#key-analysis)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [Author](#author)

---

## About the Project

**Problem:** Financial institutions need to monitor the profitability of their credit portfolios across different vintages (safras), identify which products generate the most default risk, and simulate how changes in default rates impact overall margins — all of this at scale, with large volumes of data.

**Decision:** Build a data pipeline using PySpark for distributed processing, applying ETL techniques to generate, transform, and analyze 10,000 synthetic loan records across multiple credit products and vintages.

**Result:** A fully functional analytical pipeline that calculates P&L by vintage, measures default rates by product, and simulates sensitivity scenarios — enabling data-driven credit policy decisions.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3.13** | Main language |
| **PySpark 3.5** | Distributed data processing and DataFrame transformations |
| **Pandas** | Data manipulation and aggregation |
| **Matplotlib & Seaborn** | Data visualization |
| **Jupyter Notebook** | Interactive analysis and storytelling |

---

## Architecture

The project follows an ETL pipeline architecture:

```
Data Generation (Extract)
        ↓
PySpark Transformations (Transform)
  → P&L calculation (interest revenue, expected loss, net margin)
  → Lambda functions for default loss computation
        ↓
Pandas Aggregations (Transform)
  → P&L by vintage (safra)
  → Default rate by product
  → Sensitivity scenarios
        ↓
Visual Output (Load)
  → Charts saved to /data
```

---

## Features

- ✅ Synthetic credit portfolio generation (10,000 records)
- ✅ ETL pipeline — Extract, Transform, Load
- ✅ P&L calculation by vintage (safra) using PySpark DataFrames
- ✅ Lambda functions for default loss transformation
- ✅ Default rate analysis by product
- ✅ Sensitivity analysis — net margin impact with default rate increases from 0% to 50%
- ✅ Visual dashboards with charts

---

## Key Analysis

### 📈 P&L by Vintage (Safra)
**Problem:** Which months generated the most profitable credit portfolios?  
**Decision:** Group all loan records by origination month (safra) and aggregate revenue, loss, and net margin.  
**Result:** Monthly P&L evolution across 2022–2024, identifying the best and worst performing vintages.

---

### 🔴 Default Rate by Product
**Problem:** Which credit products carry the highest default risk?  
**Decision:** Calculate the default rate per product using lambda functions to classify payment status.  
**Result:** Cartão de Crédito showed the highest default rate (~34%), while Financiamento showed the lowest (~32%).

---

### ⚠️ Sensitivity Analysis
**Problem:** How resilient is the portfolio to increases in default rates?  
**Decision:** Simulate 6 scenarios with default rate increases from 0% to +50% and measure the impact on total net margin.  
**Result:** At +50% default rate increase, the portfolio turns negative — providing a clear risk threshold for credit policy decisions.

---

## Getting Started

### Prerequisites

- Python 3.13
- Git

### Running the Project

1. Clone the repository:

```bash
git clone https://github.com/tiagosilva06/credit-portfolio-analysis
cd credit-portfolio-analysis
```

2. Create and activate virtual environment:

```bash
python -m venv venv

# Windows
source venv/Scripts/activate

# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install pyspark==3.5.1 pandas matplotlib seaborn
```

4. Open the notebook:

```bash
jupyter notebook main.ipynb
```

---

## Project Structure

```
credit-portfolio-analysis/
├── data/          # Generated charts and outputs
├── notebooks/     # Additional notebooks
├── main.ipynb     # Main analysis notebook
└── README.md
```

---

## Author

**Tiago Silva**  
[GitHub](https://github.com/tiagosilva06) • [LinkedIn](https://linkedin.com/in/tiago-silvadev)

---

> Built with Python and PySpark — targeting the financial data engineering ecosystem.