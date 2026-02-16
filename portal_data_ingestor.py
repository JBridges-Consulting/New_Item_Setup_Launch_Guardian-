import pandas as pd

def process_portal_drop(file_path):
    # This simulates the agent 'picking up' the file you just downloaded
    df = pd.read_csv(file_path)
    
    print(f"--- AGENT INGESTION: RETAILER PORTAL DROP ---")
    print(f"Successfully processed {len(df)} store records.")
    return df

# In the demo, you'd show yourself dropping the CSV into the folder
raw_data = process_portal_drop('data/weekly_portal_export.csv')