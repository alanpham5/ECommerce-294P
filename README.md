# E-Commerce Event Log Exploration

This repository contains the `exploration.ipynb` notebook, which analyzes user behavior data from an e-commerce platform. This platform to query the dataset referenced below is meant for data analysis for a UC Irvine Masters of Computer Science course.

## ⚠️ Storage Requirements

> **Note:** The dataset requires **at least 15 GB** of free disk space to store the database file locally. Make sure your system has sufficient space before running the notebook.

---

## 🔧 Setup Instructions

To ensure reproducibility and prevent dependency conflicts, it is recommended to use a virtual environment.

### 1. Clone this Repository

```bash
git clone <repo-url>
cd <repo-directory>
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, install dependencies manually based on imports in the notebook, e.g.,:

```bash
pip install pandas numpy matplotlib seaborn sqlite3 tqdm
```

---

## 🏗️ Aggregating and Saving Data

The notebook includes a preprocessing step to aggregate raw user event logs into a session-level structure. This step is controlled by the `aggregate_data` flag:

```python
aggregate_data = True
```

When `aggregate_data` is set to `True`, the notebook will:

1. **Download compressed data files** (`.csv.gz`) from the internet if they are not already present locally.
2. **Process and aggregate the data using DuckDB**, an efficient in-process SQL OLAP database engine.
3. Group and enrich records at the session level, including tagging whether a view led to an "add to cart" or a purchase.
4. Save the final, processed data into a local **SQLite database**, which will be used for all downstream analysis.

> This step requires downloading multiple large files and performing heavy aggregation, so it may take considerable time and disk space (at least **15 GB** recommended).

For subsequent runs, once the data has been aggregated and stored in the SQLite database, you can skip reprocessing by setting:

```python
aggregate_data = False
```

This allows the notebook to load directly from the database, speeding up execution significantly.

---

## 🗃️ Database Structure

The project uses a DuckDB database that stores user event logs. Below is the schema of the main events table:

| Column Name     | Data Type   | Description                                                 |
| --------------- | ----------- | ----------------------------------------------------------- |
| `user_id`       | `VARCHAR`   | Anonymized user ID                                          |
| `user_session`  | `VARCHAR`   | Session ID, used to group interactions per visit            |
| `product_id`    | `VARCHAR`   | Unique identifier for the product                           |
| `brand`         | `VARCHAR`   | Product brand                                               |
| `category_id`   | `BIGINT`    | Unique identifier for the product's category                |
| `category_code` | `VARCHAR`   | Hierarchical category code (e.g., `electronics.smartphone`) |
| `price`         | `DOUBLE`    | Price of the product at the time of the event               |
| `view_time`     | `TIMESTAMP` | Timestamp of the product view                               |
| `added_to_cart` | `BOOLEAN`   | Whether the item was added to cart during the session       |
| `purchased`     | `BOOLEAN`   | Whether the item was purchased during the session           |

> The database file must be located in the same directory as the notebook, or the notebook’s path to it must be updated accordingly.

---

## 📓 Notebook Overview

`exploration.ipynb` includes:

- Initial data loading and sanity checks
- Exploratory analysis of user behavior patterns
- Event frequency breakdowns by session, product, and category
- Price distribution visualizations
- Session-level summaries
