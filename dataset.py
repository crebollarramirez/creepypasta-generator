import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("thomaskonstantin/3500-popular-creepypastas")

print("Path to dataset files:", path)

# Find the Excel file in the dataset
excel_files = [f for f in os.listdir(path) if f.endswith('.xlsx')]
if excel_files:
    excel_file = os.path.join(path, excel_files[0])
    print(f"Found Excel file: {excel_file}")
    
    # Load the dataset
    df = pd.read_excel(excel_file)
    
    # Use only half of the dataset for faster processing
    half_size = len(df)
    df_half = df.head(half_size)
    
    # Save half of the body attributes to a text file
    with open('all_creepypasta_bodies.txt', 'w', encoding='utf-8') as f:
        for i, body in enumerate(df_half['body'], 1):
            f.write(str(body))
    
    print(f"Saved {len(df_half)} creepypasta bodies (half of {len(df)}) to 'all_creepypasta_bodies.txt'")


