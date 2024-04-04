import requests
from bs4 import BeautifulSoup
import json

# URL of the page to scrape
url = "https://kpopping.com/database/company/founded-in-2023"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all rows within the tbody tag
rows = soup.find_all('tbody')

# Initialize an empty list to store company data
companies = []

# Iterate over each row and extract company information
for row in rows:
    cells = row.find_all('td')
    if len(cells) == 3:  # Ensure the row has the expected number of cells
        company_name = cells[0].text.strip()
        company_owner = cells[1].text.strip()
        year_founded = cells[2].text.strip()
        companies.append({
            'company_name': company_name,
            'company_owner': company_owner,
            'year_founded': year_founded
        })

# Write the list of companies to a JSON file
with open('companies.json', 'w') as json_file:
    json.dump(companies, json_file, indent=4)

print("Data saved to companies.json")
