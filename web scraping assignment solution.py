#!/usr/bin/env python
# coding: utf-8

#  web scraping assignment 

# Q1 Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[1]:


from bs4 import BeautifulSoup
import pandas as pd
import requests
page=requests.get('https://en.wikipedia.org/wiki/Main_Page')
page
bs = BeautifulSoup(page.content, "html.parser")
header_tags = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
header_texts=[tag.get_text() for tag in header_tags]
df = pd.DataFrame(header_texts, columns=["Header"])
df


#  Q 2.Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
# from https://presidentofindia.nic.in/former-presidents.htm and make data frame.
# 

# In[32]:


from bs4 import BeautifulSoup 
import requests
import pandas as pd
pres = requests.get('https://presidentofindia.nic.in/former-presidents')

pres
soup = BeautifulSoup(pres.content)
soup
president_name = [] 
for i in in_pres.find_all('div', class_="desc-sec"):
    president_name.append(i.text.replace('\n',''))
    
president_name
df_pres = pd.DataFrame({'Name of President and Term of office':president_name })
df_pres
pat = '(\D+)'
all_names = df_pres['Name of President and Term of office'].str.extract(pat,expand=False)
all_names

df1 = pd.DataFrame({'Name of President': all_names,
                     'Term of Office': ['25th July, 2017 - 25th July 2022','25th July 2012 - 25th July 2017','25th July 2007 - 25th July 2012','July 2002 - 25th July 2007',' 25 July, 1997 - 25 July 2002','25 July, 1992 - 25 July, 1997','25 July, 1987 - 25 July, 1992','25 July, 1982 - 25 July, 1987',' 25 July, 1977 - 25 July, 1982','24 August, 1974 - 11 February, 1977','24 August, 1969 - 24 August, 1974',' 13 May, 1967 - 03 May, 1969','13 May, 1962 - 13 May , 1967','26 January, 1950 - 13 May, 1962']})
df1


# 3) Write a python program to scrape cricket rankings from icc-cricket.com.You have to scrape and make data frame
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team  and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.

# In[9]:


#) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/team-rankings/mens/odi"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

teams = []
for row in soup.find_all("div", class_="si-table-data-wrap"):
    team = row.find("h3",class_="si-team-name").text.strip()
    
matches = []    
for row in soup.find_all("div", class_="si-table-data si-matches"):    
    match = row.find("span", class_="si-text").text.strip()
                      
points = []                     
for row in soup.find_all("div",class_="si-table-data si-pts"):
    point = row.find("span", class_="si-text").text.strip()
                      
ratings = []   
for row in soup.find_all("div",class_="si-table-data si-rating" ):                     
    rating =row.find("span",class_="si-text").text.strip()
    
    teams.append(team)
    matches.append(match)
    points.append(point)
    ratings.append(rating)

    
data = {"Team": teams, "Matches": matches, "Points": points, "Rating": ratings}
df = pd.DataFrame(data)
print("Top 10 ODI Teams in Men's Cricket:")
print(df)





# In[10]:


# b) Top 10 ODI Batsmen along with the records of their team  and rating

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.icc-cricket.com/rankings/team-rankings/mens/odi"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)


# In[ ]:





# 4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating

# In[19]:


#a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.


# In[ ]:


5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
make data frame
i) Headline
ii) Time
iii) News Link


# In[96]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


page=requests.get("https://www.cnbc.com/world/?region=world")
# page
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

headLines = []
newsLinks = []
times = []
for article in soup.find_all("div", class_="LatestNews-container"):
    headline = article.find("a", class_="LatestNews-headline").text.strip()
    time = article.find("time", class_="LatestNews-timestamp").text.strip()
    link = article.find("a", href=True)["href"]
    
    headLines.append(headline)
    times.append(time)
    newsLinks.append(link)
    
print(len(headLines),len( times),len( newsLinks))   

df = pd.DataFrame({
        'HeadLine': headLines,
        'Time': times,
        'NewsLink': newsLinks
    })    
    
print(df)

    


# 6) Write a python program to scrape the details of most downloaded articles from AI in last 90
# days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details and make data frame
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[95]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
response = requests.get(url)
response
soup = BeautifulSoup(response.content, "html.parser")
soup
titles = []
authors = []
dates=[]
urls=[]
for article in soup.find_all("li", class_="sc-9zxyh7-1 sc-9zxyh7-2 kOEIEO hvoVxs"):
    title = article.find("h2",class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg").text.strip()
    author = article.find("span", class_="sc-1w3fpd7-0 dnCnAO").text.strip()
    date = article.find("span", class_="sc-1thf9ly-2 dvggWt").text.strip()
    url = article.find("a",href=True)["href"]
    
    titles.append(title)
    authors.append(author)
    dates.append(date)
    urls.append(url)
print(len(titles),len(authors),len(dates),len(urls))
df=pd.DataFrame({'Paper Title':titles,'Authors':authors,'Published Date':date,'Paper URL':urls})
df
      


# 7) Write a python program to scrape mentioned details from dineout.co.in and make data frame
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[ ]:





# In[94]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.dineout.co.in/delhi-restaurants'

response = requests.get(url)
response
soup = BeautifulSoup(response.content, 'html.parser')
soup

titles=[]
for detail in soup.find_all('div',class_="restnt-info cursor"):
    titles .append(detail.text)
titles 

location=[]
for detail in soup.find_all('div',class_="restnt-loc ellipsis"):
     location.append(detail.text)
location 

images=[]
for detail in soup.find_all("img",class_="no-img"):
    images.append(detail['data-src'])

images

ratings=[]
for detail in soup.find_all("div",class_="restnt-rating rating-4"):
    ratings.append(detail.text)

ratings

cuisines = []
for detail in soup.find_all("span",class_="double-line-ellipsis"):
    cuisine = detail.find('a')
    cuisines.append(cuisine.text)
    cuisines
    
print(len(titles),len(location),len(ratings),len(images),len(cuisines))

df=pd.DataFrame({'Restaurant Name': restaurantNames ,
                 'Location':locations ,
                 'Ratings':ratings,
                 'Image URL': images,'Cuisines':cuisines}) 
df
   
    
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




