import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"

# Make request to url
response = requests.get(url)
response.content

# Parse the HTML response
soup = BeautifulSoup(response.content, 'html.parser')

# It gives us the visual representation of data
print(soup.prettify())

# Extracting the name of the Product
name = soup.find('div', class_="_4rR01T")
print(name)

# To get just the name we will use the below code
name.text

# Extracting the rating of the Product
rating = soup.find('div',class_="_3LWZlK")
print(rating)

# To get rating of a product we use below code
rating.text

# Extracting the other details of the product
specification = soup.find('div',class_="fMghEO")
print(specification)

# Get other details and specifications of the product
specification.text

# To get each specification separately we run below code
for each in specification:
    spec = each.find_all('li',class_='rgWa7D')
    print(spec[0].text)
    print(spec[1].text)
    print(spec[2].text)
    # print(spec[4].text)
    # print(spec[5].text)
    # print(spec[7].text)

# Extracting the price of the product
price = soup.find('div',class_='_30jeq3 _1_WHN1')
print(price)

# To get price of the product
price.text    

# Defining the lists to store the value of each feature
products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
# apps = []                #List to store supported apps                
os = []                  #List to store operating system
hd = []                  #List to store resolution
# warranty = []               #List to store warranty details

# Extracting all the features together
for data in soup.findAll('div',class_='_3pLy-c row'):
        names = data.find('div', attrs={'class':'_4rR01T'})
        price = data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating = data.find('div', attrs={'class':'_3LWZlK'})
        specification = data.find('div', attrs={'class':'fMghEO'})
        
        # Extract each specification separately
        for each in specification:
            col = each.find_all('li', attrs={'class':'rgWa7D'})
            os_ = col[0].text
            hd_ = col[1].text
            # sound_ = col[2].text
            # warranty_= col[3].text

        # All the features are extracted and stored in the respective lists.
        products.append(names.text) # Add product name to list
        prices.append(price.text) # Add price to list
        # apps.append(app) # Add supported apps specifications to list
        os.append(os_) # Add operating system specifications to list
        hd.append(hd_) # Add resolution specifications to list
        # warranty.append(warranty_) # Add sound specifications to list
        ratings.append(rating.text)   #Add rating specifications to list           



# Printing the length of list
print(len(products))
print(len(ratings))
print(len(prices))
# print(len(apps))
# print(len(warranty))
print(len(os))
print(len(hd))


# Storing the data into the structured format in the Data Frame
df = pd.DataFrame({'Product Name':products,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
df.head(10)

# Create a dataframe from the scraped data
df = pd.DataFrame(df)

# Save the dataframe to an Excel file
df.to_excel("Flipkart_Scrapped_data.xlsx", index=False)
