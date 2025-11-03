import pandas as pd

def ingest_matrix(file_path):
    """Load a CSV file containing 2x2 matrices."""
    return pd.read_csv(file_path)
