import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://kpopping.com/database/company/founded-in-2024"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find the tbody tag
tbody_tag = soup.find('tbody')

# Extract the text within the tbody tag
tbody_content = tbody_tag.get_text()

# Print the text content within the tbody tag
print(tbody_content)
