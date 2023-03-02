import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"

# Make request to url
response = requests.get(url)
response.content

# Parse the HTML response
soup = BeautifulSoup(response.content, 'html.parser')

# Defining the lists to store the value of each feature
products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product               
os = []                  #List to store operating system
hd = []                  #List to store resolution

# Extracting all the features together
for data in soup.findAll('div',class_='_3pLy-c row'):
        
        names = data.find('div', attrs={'class':'_4rR01T'})
        products.append(names.text) # Add product name to list

        price = data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        prices.append(price.text) # Add price to list

        try:
            rating = data.find('div', attrs={'class':'_3LWZlK'})
            ratings.append(rating.text)   #Add rating specifications to list 
        except:
             continue    

        specification = data.find('div', attrs={'class':'fMghEO'})        
        # Extract each specification separately
        for each in specification:
            col = each.find_all('li', attrs={'class':'rgWa7D'})

            os_ = col[0].text
            os.append(os_) # Add operating system specifications to list

            hd_ = col[1].text
            hd.append(hd_) # Add resolution specifications to list           
            
                
# Storing the data into the structured format in the Data Frame
df = pd.DataFrame({'Product Name':products,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
df.head(10)

# Create a dataframe from the scraped data
df = pd.DataFrame(df)

# Save the dataframe to an Excel file
df.to_excel("Flipkart_Scrapped_data1.xlsx", index=False)
