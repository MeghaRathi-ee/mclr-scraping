import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date

# Send a GET request to the website
url = "https://bandhanbank.com/rates-charges"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the table by its class or ID
div_rccollapseOne5 = soup.find("div", id="rccollapseOne5")  # Find the div element with id "rccollapseOne5"
table = div_rccollapseOne5.find("table")  # Find the table within the div element

# Extract the table data
table_data = []
rows = table.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    row_data = [col.get_text(strip=True) for col in cols]
    table_data.append(row_data)

# Create a DataFrame from the table data
df = pd.DataFrame(table_data[1:], columns=table_data[0])

# Add the date to the extracted data
current_date = date.today().strftime("%Y-%m-%d")
df["Date"] = current_date

# Save the DataFrame to a CSV file
csv_file_name = f"bandhanbank_rates_{current_date}.csv"
df.to_csv(csv_file_name, index=False)
