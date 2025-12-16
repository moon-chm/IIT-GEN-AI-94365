import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from textwrap import fill

url = "https://www.sunbeaminfo.in/internship"
response = requests.get(url, timeout=20)

soup = BeautifulSoup(response.text, "html.parser")

table1 = soup.find("div", id="collapseSix")

table_data1 = []
if table1:
    rows = table1.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if cols:
            table_data1.append([col.get_text(strip=True) for col in cols])

headers1 = ["Technology", "Aim", "Prerequisite", "Learning", "Location"]

def wrap_row(row, width=35):
    return [fill(cell, width) for cell in row]

print("\nAvailable Internship Program")
print(tabulate([wrap_row(r) for r in table_data1], headers=headers1, tablefmt="fancy_grid"))

table2 = soup.find("div", class_="table-responsive")

table_data2 = []
if table2:
    rows = table2.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if cols:
            table_data2.append([col.get_text(strip=True) for col in cols])

headers2 = ["Sr.No", "Batch", "Batch Duration", "Start Date", "End Date", "Time", "Fees(Rs.)", "Download Brochure"]

print("\nInternship Batches Schedule:")
print(tabulate([wrap_row(r) for r in table_data2], headers=headers2, tablefmt="fancy_grid"))
