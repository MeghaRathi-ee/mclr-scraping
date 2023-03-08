import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = "https://www.hdfcbank.com/personal/resources/rates"

r = requests.get(url, headers=HEADERS)

list_header = []
data = []

soup=BeautifulSoup(r.text,"html.parser") 
# print(soup.encode("utf-8"))

# id = document.querySelectorAll("[data-pid='widget-hdfc-invest-advisory-9174617'] table")[0].find('tr')
div = soup.find_all('div', attrs={"data-pid":"widget-hdfc-invest-advisory-9174617"})[0]

table = div.find("table")
# print(table.find("tr"))
heading = table.find("tr")

for items in heading:
    try:
        list_header.append(items.get_text())
    except:
        continue

HTML_data = table.find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)



# dataFrame = pd.DataFrame(data = data, columns = list_header)
# dataFrame.to_csv('hdfc.csv')

# Extract MCLR rates
mclr_table = table
mclr_rows = HTML_data  # skip header row
mclr_data = {}
for row in mclr_rows:
    cols = row.find_all("td")
    tenor = cols[0].text.strip()
    rate = cols[1].text.strip()
    mclr_data[tenor] = rate

# Print MCLR rates
print("HDFC MCLR Rates:")
for tenor, rate in mclr_data.items():
    print(tenor, ":", rate)
