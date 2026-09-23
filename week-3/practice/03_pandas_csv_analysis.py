import pandas as pd

filename = input("Enter CSV file name: ").strip()

try:
    data = pd.read_csv(filename)

    print("\nFirst 5 rows:")
    print(data.head())

    print("\nDataset information:")
    print(data.info())

    print("\nBasic statistics:")
    print(data.describe(include="all"))

except FileNotFoundError:
    print("Error: CSV file not found.")
except Exception as error:
    print(f"Unable to analyze CSV file: {error}")
