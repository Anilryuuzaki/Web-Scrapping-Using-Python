#import the necessary libraries 
import requests 
from bs4 import BeautifulSoup 
import pandas as pd

#define the recursive function 
def webscrap(url): 
    #get the page content 
    page = requests.get(url) 
    #parse the page content 
    soup = BeautifulSoup(page.content, 'html.parser') 
    #find all the links in the page 
    statewise_list = soup.find('div',{'class': "card-body text-center"}) 
   
    #for each link call the webscrap() function recursively 
    for state in statewise_list: 
        link_url = state.find_all('h5',{'class': "card-title text-center text-success"}) 
        print(link_url)
#class="card-title text-center text-success"    class="card-body text-center"
#call the webscrap() function with the starting URL 
url = "https://schools.org.in/"
webscrap(url)

df = pd.DataFrame({'State':'link_url'})
df.head(10)

# Create a dataframe from the scraped data
df = pd.DataFrame(df)

# Save the dataframe to an Excel file
df.to_excel("Schools_data.xlsx", index=False)
