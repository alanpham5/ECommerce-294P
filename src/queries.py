import duckdb
from pathlib import Path

DATA_FILE = Path("./data/2019-Oct.csv.gz")  # Adjust path as needed

def preview_october_data(n=10):
    query = f"""
    SELECT * FROM '{DATA_FILE}'
    LIMIT {n};
    """
    return duckdb.query(query).to_df()

if __name__ == "__main__":
    df = preview_october_data()
    print(df)