import requests
import pandas as pd


## Sample code to write API data to csv

if __name__ == "__main__":
    response = requests.get(r"https://ghoapi.azureedge.net/api/LEAD_5")
    df = pd.DataFrame()
    for i in response.json()['value']:
        df_ = pd.DataFrame(columns = i.keys())
        for j in df.columns:
            df_[j] = [i[j]]
        df = df.append(df_)
    df.to_csv(r"C:\Users\u1374014\api_call_demo\api_df.csv",index=False)