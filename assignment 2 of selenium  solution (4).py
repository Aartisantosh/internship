#!/usr/bin/env python
# coding: utf-8

# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[37]:


#iinstalling selenium
get_ipython().system('pip install selenium')


# In[38]:


#importing libraries
import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

#lets connect with web driver
driver = webdriver.Chrome()
maximize = driver.maximize_window()

#open browser
driver.get("https://www.shine.com/")
time.sleep(3)




# In[39]:


#click on the search buttone
search=driver.find_element(By.XPATH,'//i[@class="iconH-zoom-white"]')
search.click()
time.sleep(3)


# In[40]:


# job_title=driver.find_element(By.XPATH,'//input[@class="input"]')
# job_title.click()
# time.sleep(3)


# In[41]:


#search the “Data Analyst” and click search button
designation = driver.find_element(By.CLASS_NAME,"form-control")
designation.send_keys('Data Analyst')
time.sleep(3)


# In[42]:


#location
location=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Banglore')
time.sleep(3)


# In[43]:


# click on search jobs
search=driver.find_element(By.XPATH, '//div[@class="searchForm_btnWrap_advance__VYBHN"]/button[1]')
search.submit()


# In[44]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]

title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]/a')
for i in title_tags:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location) 
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company)    
    
experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    experience=i.text
    experience_required.append( experience)    
    


# In[45]:


# find lenght
print(len(job_title),len(job_location),len(company_name),len(experience_required))  




# In[46]:


# creatind data frame
df = pd.DataFrame({
    'Job Title': job_title,
    'Job Location': job_location,
    'Company Name': company_name,
    'Experience Required': experience_required
})
df
df[0:10]


# Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[50]:


#importing libraries
import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

#connect with driver
driver = webdriver.Chrome()
maximize = driver.maximize_window()

#open browser
driver.get("https://www.shine.com/")


# In[51]:


#first click
job_title=driver.find_element(By.XPATH,'//input[@class="input"]')
job_title.click()


# In[52]:


#search designation
designation = driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Scientist')


# In[53]:


#search location
location=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Banglore')
time.sleep(3)


# In[54]:


#click on search jobs
#Search=driver.find_element(By.XPATH, '//button[@class=" btn btn-secondary undefined"]')
search_jobs=driver.find_element(By.XPATH,'//div[@class="searchForm_btnWrap__Cb75F"]/div/button')
search_jobs.submit()


# In[55]:


job_title=[]
job_location=[]
company_name=[]


title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]/a')
for i in title_tags:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location) 
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company)  


# In[56]:


print(len(job_title),len(job_location),len(company_name))


# In[57]:


# creating dataframe
df = pd.DataFrame({
    'Job Title': job_title,
    'Job Location': job_location,
    'Company Name': company_name
    
})
df[0:10]


# Q3: In this question you have to scrape data using the filters available on the webpage
#  You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.shine.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scrapeddata.
# Note: All of the above steps have to be done in code. No step is to be done manually

# In[ ]:


import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
maximize = driver.maximize_window()

driver.get("https://www.shine.com/")



# In[ ]:


job_title=driver.find_element(By.XPATH,'//input[@class="input"]')
job_title.click()


# In[ ]:


designation = driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Scientist')


# In[ ]:


search_jobs=driver.find_element(By.XPATH,'//div[@class="searchForm_btnWrap__Cb75F"]/div/button')
search_jobs.submit()


# In[ ]:


filterr_by_location=driver.find_element(By.XPATH,'//li[@class="filter_filter_lists_items__wlFfo"]/button[1]')
filterr_by_location.click()


# In[ ]:


location=driver.find_element(By.XPATH,"//input[@class="styled-checkbox"]")
location.click()


# In[ ]:


filterr_by_salary=driver.find_element(By.XPATH,"//li[@class="filter_filter_lists_items__wlFfo"]/button[3]")
filterr_by_salary.click()


# In[ ]:


salary=driver.find_element(By.XPATH,"//input[@class="styled-checkbox"]")
salary.click()


# In[ ]:


show_result=driver.find_element(By.XPATH,"//button[@class="btn btn-secondary"]")
show_result.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]



# In[ ]:


title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]/a')
for i in title_tags:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags:
    location=i.text
    job_location.append(location) 
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags:
    company=i.text
    company_name.append(company) 
    
experience_tag=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    experience=i.text
    experience_tag.append(experience)     


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


df = pd.DataFrame({
    'Job Title': job_title,
    'Job Location': job_location,
    'Company Name': company_name
    'Experience Required': experience_required
})
df


# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 6. Brand
# 7. ProductDescription
# 8. Price
# The attributes which you have to scrape is ticked marked in the below image.
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url :https://www.flipkart.com/
# 2. Enter “sunglasses” in the search fieldwhere “search for products, brands and more” is written and
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the
# required data as usual.
# 4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
# click on it.
# 5. Now scrape data from this page as usual
# 6. Repeat this until you get data for 100sunglasses.
# Note: That all of the above steps have to be done by coding only and not manually.
# 

# In[58]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
maximize = driver.maximize_window()

driver.get('https://www.flipkart.com/')
time.sleep(3)

item = driver.find_element(By.CLASS_NAME, "Pke_EE")
item.send_keys('sunglasses')

search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


Brand_name= []
Product_Description = []
Price= []

Brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in Brand_tags:
    Brand=i.text
    Brand_name.append(Brand)
    
product_tags=driver.find_elements(By.XPATH,'//div[@class="_2B099V"]/a[1]')
for i in product_tags:
    product=i.text
    Product_Description.append( product)    
    
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tags:
    price=i.text
    Price.append(price)    
     
print(len(Brand_name),len(Price),len(Product_Description))    


# In[59]:


Brand_name= []
Product_Description = []
Price= []


start=0
end=3
for page in range(start,end):
    Brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand_tags:
        Brand=i.text
        Brand_name.append(Brand)
    
    product_tags=driver.find_elements(By.XPATH,'//div[@class="_2B099V"]/a[1]')
    for i in product_tags:
        product=i.text
        Product_Description.append( product)    
    
    price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_tags:
        price=i.text
        Price.append(price)   

next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')   
next_button.click()
    


# In[60]:


print(len(Brand_name),len(Price),len(Product_Description)) 


# In[61]:


df=pd.DataFrame({'Brand':Brand_name,'Price':Price,'Product Description':Product_Description})
df[0:100]


# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market
# place=FLIPKART
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# Note: All the steps required during scraping should be done through code only and not manually

# In[62]:


import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

#lets connect with web driver

driver = webdriver.Chrome()
maximize = driver.maximize_window()
#onpening the flipkart website on automated chrome window
driver.get('https://www.flipkart.com/')
time.sleep(3)


# In[63]:


#find item
item = driver.find_element(By.CLASS_NAME, "Pke_EE")
item.send_keys('iphone11 ')
#click on search 
search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[64]:


Rating = []
Review_summary = []
Full_review = []


# In[65]:


# for i in range(3):
    
#     rating = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK"]')
# # rating = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK"]/img')
#     review = driver.find_elements(By.XPATH,'//span[@class="_2_R_DZ"]/span/span[1]')
#     full_review = driver.find_elements(By.XPATH,'//span[@class="_2_R_DZ"]/span/span[3]')


#     for i in  rating:
#         Rating.append(i.text)
#     for i in  review:
#         Review_summary.append(i.text)
#     for i in  full_review:
#         Full_review.append(i.text)
    
# time.sleep(3)


# In[66]:


start=0
end=5
for page in range(start,end):
    rating_tag=driver.find_elements(By.XPATH,'//div[@class="gUuXy-"]/span/div')
    for i in rating_tag:
        rating=i.text
        Rating.append(rating)
    
    Review_tags=driver.find_elements(By.XPATH,'//div[@class="gUuXy-"]/span[2]/span/span[3]')
    for i in Review_tags:
        review=i.text
        Review_summary.append(review)    
    
    Full_review_tags=driver.find_elements(By.XPATH,'//div[@class="gUuXy-"]/span[2]')
    for i in Full_review_tags:
        Full_rev=i.text
        Full_review.append(Full_rev)   

next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')   
next_button.click()
    


# In[67]:


print(len(Rating ),len(Review_summary),len(Full_review ))  


# In[68]:


df = pd.DataFrame({'Rating':Rating,'Review summary':Review_summary,'Full review':Full_review})

df[0:100]


# In[ ]:





# In[ ]:





# Q6: Scrape data forfirst 100 sneakers you find whenyou visit flipkart.com and search for “sneakers” inthe
# search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# As shown in the below image, you have to scrape the above attributes.

# In[69]:


import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

#lets connect with web driver

driver = webdriver.Chrome()
driver.maximize_window()
#onpening the flipkart website on automated chrome window
driver.get('https://www.flipkart.com/')
time.sleep(3)


# In[70]:


# pop_close = driver.find_element_by_xpath("/html/body/div[2]/div/div/button")
# pop_close.click()


# In[73]:


#search sneakers
#search_item = driver.find_element(By.CLASS_NAME,"_3704LK")
search_item = driver.find_element(By.CLASS_NAME,"Pke_EE")
search_item.send_keys("sneakers")
time.sleep(3)


# In[81]:


#click button
#click_search_button = driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
click_search_button = driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
click_search_button.click()
time.sleep(3)


# In[82]:


Brand = []
Product_Description = []
Price = []


# In[83]:


for i in range(3):
    
    
    brand = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    product_des = driver.find_elements(By.XPATH,"//div[@class='_2B099V']/a[1]")
    price = driver.find_elements(By.XPATH,"//div[@class='_30jeq3']")


    for i in brand:
        Brand.append(i.text)
    for i in product_des:
        Product_Description.append(i.text)
    for i in price :
        Price.append(i.text)
    
time.sleep(3)


# In[84]:


#click on next button
nxt_button = driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
nxt_button.click()


# In[85]:


# print length
print(len(Brand),len(Product_Description),len(Price))


# In[86]:


# create Data frame
df = pd.DataFrame({'Brand':Brand,'Product_Description':Product_Description,'Price':Price})

df[0:100]


# Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price3. 

# In[88]:


import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

#lets connect with web driver

driver = webdriver.Chrome()
driver.maximize_window()
#onpening the flipkart website on automated chrome window
driver.get('https://www.flipkart.com/')
time.sleep(3)


# In[89]:


item = driver.find_element(By.CLASS_NAME, "Pke_EE")
item.send_keys('iphone11 ')


# In[90]:


click_search_button = driver.find_element(By.CLASS_NAME,"_2iLD__")
click_search_button.click()
time.sleep(3)


# In[91]:


intel_core7 = driver.find_element(By.XPATH,'//div[@class="_3OO5Xc"]/input')
intel_core7.click()


# In[92]:


click_search_button = driver.find_element(By.CLASS_NAME,"L0Z3Pu")
click_search_button.click()
time.sleep(3)


# In[93]:


time.sleep(5)
Title = []
Ratings = []
Price = []


# In[94]:


title = driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
rating = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK"]')
price = driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')


for i in title:Title.append(i.text)
for i in rating:Ratings.append(i.text)    
for i in price:Price.append(i.text)
    


# In[95]:


Laptop = pd.DataFrame({'Title':Title,'Price':Price})
Laptop[0:10]


# Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuotes
# 3. Than scrap a) Quote b) Author c) Type Of Quotes

# In[114]:


import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

#lets connect with web driver

driver = webdriver.Chrome()
driver.maximize_window()
#onpening the flipkart website on automated chrome window
driver.get('https://www.azquotes.com/')
time.sleep(3)


# In[115]:


top_quote = driver.find_element(By.XPATH,'//a[@href="/top_quotes.html"]')
top_quote.click()


# In[98]:


# click_search_button = driver.find_element(By.CLASS_NAME,"_2iLD__")
# click_search_button.click()
# time.sleep(3)


# In[116]:


Quote= []
Author = []
Type_Of_Quotes= []


# In[100]:


# for first 100 recorde show


quote_tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quote_tags:
    quote=i.text
    Quote.append(quote)
    
author_tags=driver.find_elements(By.XPATH,'//div[@class="author"]/a')
for i in author_tags:
    author=i.text
    Author.append(author)    
    
type_tags=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in type_tags:
    type_of=i.text
    Type_Of_Quotes.append(type_of)    
    


# In[101]:


print(len(Quote),len(Author),len(Type_Of_Quotes)) 


# In[102]:


detail = pd.DataFrame({'Quote':Quote,'Author':Author,'Type Of Quotes':Type_Of_Quotes})
detail[0:100]


# In[117]:


#for next page element

start=0
end=10
for page in range(start,end):
   # quote_tags=driver.find_elements(By.XPATH,'//div[@class="wrap-block"]/p/a[2]')
    quote_tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
    for i in quote_tags:
        quote=i.text
        Quote.append(quote)
    
   # author_tags=driver.find_elements(By.XPATH,'//div[@class="wrap-block"]/div')
    author_tags=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in author_tags:
        author=i.text
        Author.append(author)    
    
   # type_tags=driver.find_elements(By.XPATH,'//div[@class="wrap-block"]/div[2]/div')
    type_tags=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in type_tags:
        type_of=i.text
        Type_Of_Quotes.append(type_of)   

next_button=driver.find_element(By.XPATH,'//li[@class="next"]')   
next_button.click()
    


# In[118]:


print(len(Quote),len(Author),len(Type_Of_Quotes))


# In[119]:


detail = pd.DataFrame({'Quote':Quote,'Author':Author,'Type Of Quotes':Type_Of_Quotes})
detail[0:1000]


# Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead,
# Term of office, Remarks) from https://www.jagranjosh.com/.
# This task will be done in following steps:
# 1. First get the webpagehttps://www.jagranjosh.com/
# 2. Then You have to click on the GK option
# 3. Then click on the List of all Prime Ministers of India
# 4. Then scrap the mentioned data and make theDataFrame.

# In[146]:


import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

#lets connect with web driver

driver = webdriver.Chrome()
driver.maximize_window()
#onpening the flipkart website on automated chrome window
driver.get('https://www.jagranjosh.com/')
time.sleep(3)


# In[147]:


gk = driver.find_element(By.XPATH,'//ul[@class="Header_navLink__8eXbJ"]/li[3]')
gk.click()
time.sleep(3)


# In[148]:


gk_explore = driver.find_element(By.XPATH,'//a[@class="Landing_Btn__pXeh_ Landing_BtnOutlineDanger__rK5j_"]')
gk_explore = driver.find_element(By.XPATH,'//section[@class="Tags_Tags__NqnCB"]/ul/li[14]')
gk_explore.click()


# In[149]:


# gk_option = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/div/div[3]/ul/li[3]/a')
# gk_option.click()
prime_ministers_option= driver.find_element(By.XPATH,'/html/body/div/main/div[1]/div[1]/section/div/ul/li[2]/article/h3/a')
prime_ministers_option.click()


# In[135]:


prime_ministers_option = driver.find_element(By.XPATH, '//div[@class="TableData"]')
prime_ministers_option.click()
time.sleep(2)


# In[ ]:


#title = driver.find_elements(By.XPATH,'//div[@class="TableData"]')
pm_data = []
for pm in driver.find_elements(By.XPATH, '//div[@class="TableData"]'):
    columns = pm.find_elements(By.TAG_NAME, "td")
    name = columns[0].text
    born_dead = columns[1].text
    term_of_office = columns[2].text
    remarks = columns[3].text
    


# In[153]:


name=[]
born_dead =[]
term_of_office=[]
remarks=[]

name_tags=driver.find_elements(By.XPATH,'//div[@class="TableData"]/table/tbody/tr/th[2]/div')
for i in name_tags:
    name_of=i.text
    name.append(name_of)
        
born_tags=driver.find_elements(By.XPATH,'//div[@class="TableData"]/table/tbody/tr/th[3]/div')
for i in born_tags:
    born_of=i.text
    born_dead.append(born_of)
            
term_tags=driver.find_elements(By.XPATH,'//div[@class="TableData"]/table/tbody/tr/th[4]/div')
for i in term_tags:
    term_of=i.text
    term_of_office.append(term_of)
            
remark_tags=driver.find_elements(By.XPATH,'//div[@class="TableData"]/table/tbody/tr/th[5]/div')
for i in remark_tags:
    remark_of=i.text
    remarks.append(remark_of)
            
    


# In[154]:


print(len(name),len(born_dead),len(term_of_office),len(remarks))


# In[155]:


df = pd.DataFrame({
        'Name': name,
        'Born-Dead': born_dead,
        'Term of Office': term_of_office,
        'Remarks': remarks
    })
df


# In[ ]:





# In[ ]:





# Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e.
# Car name and Price) from https://www.motor1.com/
# This task will be done in following steps:
# 1. First get the webpage https://www.motor1.com/
# 2. Then You have to type in the search bar ’50 most expensive cars’
# 3. Then click on 50 most expensive carsin the world..
# 4. Then scrap the mentioned data and make the dataframe.

# In[143]:


#import all required libraries 
import selenium
import pandas as pd
from selenium import  webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
maximize = driver.maximize_window()

driver.get('https://www.motor1.com/')
time.sleep(3)


# In[144]:


search_bar = driver.find_element(By.XPATH, '//input[@class="m1-search-panel-input m1-search-form-text"]')
search_bar.send_keys('50 most expensive cars')

# search_bar = driver.search_element(By.CLASS_NAME,'m1-search-panel-input m1-search-form-text')
# search_bar.send_keys('50 most expensive cars')


# In[ ]:


search_form = driver.find_element(By.XPATH, '//button[@class="m1-search-panel-button m1-search-form-button-animate icon-search-svg"]')
search_form.submit()
time.sleep(2)
# search=driver.find_element(By.CLASS_NAME,"m1-search-panel-button m1-search-form-button-animate icon-search-svg")
# search.click()


# In[ ]:


# time.sleep(2)


# In[139]:


result_link = driver.find_element(By.XPATH, '/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a')
result_link.click()


# In[140]:


Price=[]
car_name=[]
# for car in driver.find_elements(By.CLASS_NAME, 'article-body'):
#     car_name = car.find_element(By.TAG_NAME, 'h2').text.strip()
#     car_price = car.find_element(By.TAG_NAME, 'p').text.strip()
    
    
#     car_data.append({
#         'Car Name': car_name,
#         'Price': car_price
#     })



price_tags=driver.find_elements(By.XPATH,'//div[@class="postBody description e-content"]/p/strong')
for i in price_tags:
    price=i.text
    Price.append(price)
    
car_name_tag=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in car_name_tag:
    name=i.text
    car_name.append(name)
                
    


# In[141]:


print(len(Price),len(car_name))


# In[142]:


data=[{'Price':Price,'Car Name':car_name}]

df=pd.DataFrame(data)
df[0:50]


# In[ ]:


df = pd.DataFrame({'Price':Price,'Car Name':car_name})

df[0:50]



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




