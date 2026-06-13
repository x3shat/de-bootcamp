# Mini Pipeline

A simple ETL (Extract → Transform → Load) pipeline that cleans messy sales data.

## What it does
- **Extract**: reads `data/raw_sales.csv`
- **Transform**: converts `amount` to integer, skips rows with invalid or missing values
- **Load**: writes cleaned data to `output/clean_sales.csv`
- Logs how many rows were kept vs dropped
- Prints total revenue

## Project structure
```
mini-pipeline/
├── README.md
├── requirements.txt
├── data/
│   └── raw_sales.csv
├── src/
│   └── pipeline.py
└── output/
    └── clean_sales.csv
```

## How to run

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the pipeline
python src/pipeline.py
```

## Sample output
```
2026-06-13 07:19:54 INFO clean=5 bad=3
2026-06-13 07:19:54 INFO Total revenue = 415
2026-06-13 07:19:54 INFO pipeline done
```

## What I learned
- Virtual environments for isolated dependencies
- ETL pattern (Extract / Transform / Load)
- Handling bad data with try/except
- Logging instead of printing
- Standard Python project structure
