import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Project paths
# --------------------------------------------------

project_root = Path(__file__).resolve().parents[1]

input_file = (
    project_root
    / "data"
    / "raw"
    / "Online Retail.xlsx"
)

# --------------------------------------------------
# Load data
# --------------------------------------------------

print("Loading dataset...")

df = pd.read_excel(input_file)

print("\n========== DATASET OVERVIEW ==========")

print(f"Rows    : {len(df):,}")
print(f"Columns : {len(df.columns)}")

print("\nColumns:")
for column in df.columns:
    print(f" - {column}")

# --------------------------------------------------
# Data types
# --------------------------------------------------

print("\n========== DATA TYPES ==========")

print(df.dtypes)

# --------------------------------------------------
# Missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========")

missing = pd.DataFrame({
    "missing_count": df.isnull().sum(),
    "missing_percentage": (
        df.isnull().mean() * 100
    ).round(2)
})

print(missing)

# --------------------------------------------------
# Duplicate records
# --------------------------------------------------

print("\n========== DUPLICATES ==========")

duplicate_count = df.duplicated().sum()

print(f"Duplicate records: {duplicate_count:,}")

# --------------------------------------------------
# Numeric validation
# --------------------------------------------------

print("\n========== QUANTITY ==========")

print(f"Minimum Quantity : {df['Quantity'].min()}")
print(f"Maximum Quantity : {df['Quantity'].max()}")
print(
    f"Negative Quantity records : "
    f"{(df['Quantity'] < 0).sum():,}"
)

print("\n========== UNIT PRICE ==========")

print(f"Minimum UnitPrice : {df['UnitPrice'].min()}")
print(f"Maximum UnitPrice : {df['UnitPrice'].max()}")
print(
    f"Zero/negative UnitPrice records : "
    f"{(df['UnitPrice'] <= 0).sum():,}"
)

# --------------------------------------------------
# Invoice analysis
# --------------------------------------------------

print("\n========== INVOICE ANALYSIS ==========")

cancelled = (
    df["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
    .sum()
)

print(f"Cancelled invoices: {cancelled:,}")

# --------------------------------------------------
# Customer analysis
# --------------------------------------------------

print("\n========== CUSTOMER ANALYSIS ==========")

print(
    f"Unique customers: "
    f"{df['CustomerID'].nunique():,}"
)

print(
    f"Missing CustomerID: "
    f"{df['CustomerID'].isnull().sum():,}"
)

# --------------------------------------------------
# Country analysis
# --------------------------------------------------

print("\n========== COUNTRY ANALYSIS ==========")

print(
    f"Unique countries: "
    f"{df['Country'].nunique():,}"
)

print("\nTop 10 countries by transaction count:")

print(
    df["Country"]
    .value_counts()
    .head(10)
)

# --------------------------------------------------
# Revenue analysis
# --------------------------------------------------

df["Revenue"] = (
    df["Quantity"] *
    df["UnitPrice"]
)

print("\n========== REVENUE ==========")

print(
    f"Total Revenue: "
    f"{df['Revenue'].sum():,.2f}"
)

print(
    f"Average transaction revenue: "
    f"{df['Revenue'].mean():,.2f}"
)

# --------------------------------------------------
# Date analysis
# --------------------------------------------------

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"]
)

print("\n========== DATE RANGE ==========")

print(
    f"Minimum Invoice Date: "
    f"{df['InvoiceDate'].min()}"
)

print(
    f"Maximum Invoice Date: "
    f"{df['InvoiceDate'].max()}"
)

print("\n========================================")
print("Profiling completed successfully.")
print("========================================")