# IMDb Dataset Analysis

Small analysis script exploring the included `imdb_top_1000.csv` dataset.

## Contents
- `project.py` — example script that loads the CSV, displays basic info and plots.
- `imdb_top_1000.csv` — dataset used by the script.

## Requirements
- Python 3.8+
- pandas
- matplotlib

Install dependencies with:

```bash
pip install pandas matplotlib
```

## Usage

Run the script from the project root:

```bash
python project.py
```

The script prints a dataframe summary and shows two plots: a histogram of IMDb ratings and a runtime vs rating scatter plot.

## Notes
- The dataset is included in the repository; avoid committing larger derived data files.
