import pandas as pd
import os

def store_user_info(name, email):
    data = {'Name': [name], 'Email': [email]}
    df = pd.DataFrame(data)
    # Append to CSV or create new
    if os.path.exists("user_data.csv"):
        df.to_csv("user_data.csv", mode='a', header=False, index=False)
    else:
        df.to_csv("user_data.csv", index=False)