import pandas as pd
from pathlib import Path

# Project paths
project_root = Path(__file__).resolve().parents[1]

input_file = project_root / "data" / "raw" / "Online Retail.xlsx"
output_file = project_root / "data" / "sample" / "online_retail_sample.csv"

# Read the original dataset
df = pd.read_excel(input_file)

# Create a reproducible sample
sample_df = df.sample(
    n=1000,
    random_state=42
)

# Save sample as CSV
sample_df.to_csv(
    output_file,
    index=False
)

print(f"Original records : {len(df):,}")
print(f"Sample records   : {len(sample_df):,}")
print(f"Sample saved to  : {output_file}")