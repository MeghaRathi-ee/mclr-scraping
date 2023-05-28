import requests
import pandas as pd
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.federalbank.co.in/loan-rate"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the MCLR rates
table = soup.find("table")

# Extract the table rows
rows = []
for tr in table.find_all("tr"):
    row = [td.text.strip() for td in tr.find_all("td")]
    if row:
        rows.append(row)

# Determine the number of columns based on the row with the maximum number of cells
num_columns = max(len(row) for row in rows)

# Create column names ("Column 0", "Column 1", ...)
headers = [f"Column {i}" for i in range(num_columns)]

# Create a DataFrame from the table data
df = pd.DataFrame(rows, columns=headers)

# Specify the output CSV file path
csv_path = "federal_bank_mclr.csv"

# Write the DataFrame to the CSV file
df.to_csv(csv_path, index=False)

print("CSV file created successfully.")
