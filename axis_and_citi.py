
import tabula

import requests

import pandas as pd

#AXIS BANK
file_url_axis_bank = "https://www.axisbank.com/docs/default-source/default-document-library/axis-bank-mclr-website-18-january-2023.pdf"
r=requests.get(file_url_axis_bank,stream=True)
with open("python1.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)

url="python1.pdf"
dfs = tabula.read_pdf(url, pages='all')
tabula.convert_into("python1.pdf", "axis.csv", output_format="csv", pages='all')


#CITI BANK
file_url_citi_bank = "https://www.online.citibank.co.in/portal/Standalone/Apr16/Credit-Cards/pdf/MCLR/MCLR.pdf"
r=requests.get(file_url_citi_bank,stream=True)
with open("python2.pdf","wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)

url="python2.pdf"
dfs = tabula.read_pdf(url, pages='all')
tabula.convert_into("python2.pdf", "citi.csv", output_format="csv", pages='all')





