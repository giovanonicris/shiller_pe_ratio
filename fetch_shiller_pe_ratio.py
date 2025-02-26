import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL of the multpl.com Shiller P/E Ratio page
url = 'https://www.multpl.com/shiller-pe/table/by-year'

# sen a GET request
response = requests.get(url)
if response.status_code == 200:
    # parse
    soup = BeautifulSoup(response.content, 'html.parser')
    # look for table with data
    table = soup.find('table')
    # convert table to data frame
    df = pd.read_html(str(table))[0]
    print(df.head())
else:
    print(f"Can't retrieve data: {response.status_code}")
