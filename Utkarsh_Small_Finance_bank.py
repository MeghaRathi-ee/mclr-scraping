import tabula
import requests
import pandas as pd
from datetime import date

file_url_utkarsh_bank = "https://www.utkarsh.bank/uploads/home_sidebar_form/MCLR-Feb,2022.pdf"
r = requests.get(file_url_utkarsh_bank, stream=True)

with open("utkarsh.pdf", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)

today = date.today()
formatted_date = today.strftime("%Y-%m-%d")
csv_file_name = f"utkarsh_small_finance_bank_{formatted_date}.csv"

url = "utkarsh.pdf"
dfs = tabula.read_pdf(url, pages='all')
print(dfs)

tabula.convert_into("utkarsh.pdf", csv_file_name, output_format="csv", pages='all')
