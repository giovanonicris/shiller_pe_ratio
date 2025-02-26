import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL from multpl.com Shiller P/E page
url = 'https://www.multpl.com/shiller-pe/table/by-year'

def fetch_shiller_pe_data():
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Locate the table in the HTML
        table = soup.find('table')
        if table:
            df = pd.read_html(str(table))[0]  # Read table into pandas

            # Print to debug
            print(df.head())  # Ensure data is correctly extracted

            # Save the cleaned CSV
            output_file = 'shiller_pe_data.csv'
            df.to_csv(output_file, index=False)
            print(f"Shiller PE data successfully saved to {output_file}")
        else:
            print("No table found on the webpage!")
            exit(1)
    else:
        print(f"Failed to retrieve data: Status code {response.status_code}")
        exit(1)

if __name__ == "__main__":
    fetch_shiller_pe_data()
