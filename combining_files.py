from pathlib import Path
import pandas as pd
import json

all_rows = []

# Load the files
folder = Path("Datasets/")

for csv_file in folder.iterdir():
    print(f"Reading: {csv_file}")

    new_csv_df = pd.read_csv(csv_file)
    filename = csv_file.stem

    # Add the original filename
    new_csv_df['original_file'] = filename

    # Add the row ID
    new_csv_df['row_id'] = [
        f"{filename}_{i}"
        for i in range(1, len(new_csv_df) + 1)
    ]

    # Add to combined dataset
    all_rows.extend(new_csv_df.to_dict(orient="records"))

# Save the JSON file
print(all_rows)