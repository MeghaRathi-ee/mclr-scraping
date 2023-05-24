import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

url = "https://www.icicibank.com/about-us/article/news-icici-bank-marginal-cost-of-funds-based-lending-rate-mclr--20163004123526382"
r = requests.get(url)

list_header = []
data = []

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find_all('table')[0].find("tr")

for items in table:
    try:
        list_header.append(items.get_text())
    except:
        continue

HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

dataFrame = pd.DataFrame(data=data, columns=list_header)

# Add the date to the extracted data
current_date = datetime.date.today().strftime("%Y-%m-%d")
dataFrame['Date'] = current_date

dataFrame.to_csv('icici.csv', index=False)
