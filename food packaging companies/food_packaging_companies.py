# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the URL
url = 'https://www.iqsdirectory.com/food-packaging/food-packaging-2/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the company listings on the page
listings = soup.findAll('li')

# Initialize empty lists to store the data
company_names = []
# websites = []
descriptions = []

# Loop over the company listings and extract the data
for listing in listings:
    # Extract the company name
    company_name = listing.find('span', {'itemprop': 'name'}).text.strip()
    company_names.append(company_name)
    
    # Extract the description
    description = listing.find('p', {'class': 'cdesc'}).text.strip()
    descriptions.append(description)

# Create a pandas DataFrame to store the data
data = {'Company Name': company_names, 'Description' : descriptions}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('food_packaging_companies.xlsx', index=False)
