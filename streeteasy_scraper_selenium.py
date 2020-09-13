#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[7]:


browser = webdriver.Chrome("/Users/VickyWu/Downloads/chromedriver")


# In[10]:


# Income resitricted co-ops for sale in the Bronx 
# Scrap the "Address" "Price" "Details" "URL" information from all the listings that fit the above criteria 


base_url_bronx = ('https://streeteasy.com/coops/bronx/status:open%7Cincome_restricted:yes?page=')

all_bronx = []

page_listing_bronx = []

last_page = 3

for i in range(1, last_page+1):
    
    browser.get(base_url_bronx + str(i))
    
    listings = browser.find_elements_by_css_selector('article.item')
    
    for listing in listings:
        one_listing = {
            'address' : listing.find_element_by_css_selector('.details-title a').text,
            'price' :  listing.find_element_by_css_selector('.price').text,
            'details' : [d.text.strip() for d in listing.find_elements_by_css_selector('ul.details_info li, li.details_info')],
            'url' : listing.find_element_by_css_selector('.details-title a').get_attribute('href')}
        
        page_listing_bronx.append(one_listing)
        
    all_bronx += page_listing_bronx


# In[ ]:


import csv


keys = all_bronx[0].keys()

with open('bronx_streeteasy.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_bronx)


# In[ ]:


#Same for Brooklyn

base_url_2 = ('https://streeteasy.com/coops/brooklyn/status:open%7Cincome_restricted:yes?page=')

all_brooklyn = []

page_listing = []

last_Page = 4

for i in range(1, last_Page+1):
    
    driver.get(base_url_2 + str(i))
    
    listings = driver.find_elements_by_css_selector('article.item')
    
    for listing in listings:
        one_listing = {
            'address' : listing.find_element_by_css_selector('.details-title a').text,
            'price' :  listing.find_element_by_css_selector('.price').text,
            'details' : [d.text.strip() for d in listing.find_elements_by_css_selector('ul.details_info li, li.details_info')],
            'url' : listing.find_element_by_css_selector('.details-title a').get_attribute('href')}
        
        page_listing.append(one_listing)
        
    all_brooklyn += page_listing


# In[ ]:


import csv


keys = all_brooklyn[0].keys()

with open('brooklyn_streeteasy.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_brooklyn)


# In[ ]:


# Same for Manhattan

base_url_manhattan = ('https://streeteasy.com/coops/manhattan/status:open%7Cincome_restricted:yes?page=')

all_manhattan = []

page_listing_manhattan = []

last_page = 15

for i in range(1, last_page+1):
    
    browser.get(base_url_manhattan + str(i))
    
    listings = browser.find_elements_by_css_selector('article.item')
    
    for listing in listings:
        one_listing = {
            'address' : listing.find_element_by_css_selector('.details-title a').text,
            'price' :  listing.find_element_by_css_selector('.price').text,
            'details' : [d.text.strip() for d in listing.find_elements_by_css_selector('ul.details_info li, li.details_info')],
            'url' : listing.find_element_by_css_selector('.details-title a').get_attribute('href')}
        
        page_listing_manhattan.append(one_listing)
        
    all_manhattan += page_listing_manhattan


# In[ ]:


import csv


keys = all_manhattan[0].keys()

with open('manhattan_streeteasy.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_manhattan)


# Part Two: Go into each listing and scrap "Days on Market", "Agent Name" and "About"

# In[ ]:


from selenium.common.exceptions import NoSuchElementException


# In[ ]:


all_manhattan = pd.read_csv('streeteasy_manhattan.csv')
all_manhattan = list(all_manhattan['url'])

all_brooklyn = pd.read_csv('brooklyn_streeteasy.csv')
all_brooklyn = list(all_brooklyn['url'])

all_bronx = pd.read_csv('bronx_streeteasy.csv')
all_bronx = list(all_bronx['url'])


# In[ ]:


# Bronx

bronx_listings=[]

for i in range(0, len(all_bronx)):
    
    driver.get(all_bronx[i])
    
    a_listing = {

            'days_on_market' : {},
            'agent_name' : {},
            'description' : {}
        }
    
#days on market
    try: 
        days_on_market = driver.find_element_by_class_name('Vitals').text
        a_listing['days_on_market'] = days_on_market
    except NoSuchElementException:
        pass

#agent name
    try: 
        agent_name =  driver.find_element_by_class_name('ListingAgents').text
        a_listing['agent_name'] = agent_name   
    except NoSuchElementException:
        pass
    
#description 
    try: 
        description = driver.find_element_by_class_name('Description-block').text
        a_listing['description'] = description 
    except NoSuchElementException:    
        pass
  
        
    bronx_listings.append(a_listing)
        


# In[ ]:


# Brooklyn

brooklyn_listings=[]

for i in range(0, len(all_brooklyn)): 
    
    driver.get(all_brooklyn[i])
    
    a_listing = {

            'days_on_market' : {},
            'agent_name' : {},
            'description' : {}
        }
    
#days on market
    try: 
        days_on_market = driver.find_element_by_class_name('Vitals').text
        a_listing['days_on_market'] = days_on_market
    except NoSuchElementException:
        pass

#agent name
    try: 
        agent_name =  driver.find_element_by_class_name('ListingAgents').text
        a_listing['agent_name'] = agent_name   
    except NoSuchElementException:
        pass
    
#description 
    try: 
        description = driver.find_element_by_class_name('Description-block').text
        a_listing['description'] = description 
    except NoSuchElementException:    
        pass
  
        
    brooklyn_listings.append(a_listing)
        


# In[ ]:


# For Manhattan

manhattan_listings=[]

for i in range(0, len(all_manhattan)): 
    
    driver.get(all_manhattan[i])
    
    a_listing = {

            'days_on_market' : {},
            'agent_name' : {},
            'description' : {}
        }
    
#days on market
    try: 
        days_on_market = driver.find_element_by_class_name('Vitals').text
        a_listing['days_on_market'] = days_on_market
    except NoSuchElementException:
        pass

#agent name
    try: 
        agent_name =  driver.find_element_by_class_name('ListingAgents').text
        a_listing['agent_name'] = agent_name   
    except NoSuchElementException:
        pass
    
#description 
    try: 
        description = driver.find_element_by_class_name('Description-block').text
        a_listing['description'] = description 
    except NoSuchElementException:    
        pass
  
        
    manhattan_listings.append(a_listing)
        


# In[ ]:


from copy import deepcopy


# In[ ]:


#Bronx listings

bronx_copy = deepcopy(bronx_listings)
bronx_ = []

for i in range(0, len(bronx_copy)):
    
    a_listing = {

            'days_on_market' : str(bronx_copy[i]['days_on_market']).replace('\n',' '),
            'agent_name' : str(bronx_copy[i]['agent_name']).replace('\n',' '),
            'description' : str(bronx_copy[i]['description']).replace('\n',' ')
        }
    
    bronx_.append(a_listing)
    
keys = bronx_[0].keys()

with open('bronx_additional.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(bronx_)


# In[ ]:


brooklyn_copy = deepcopy(brooklyn_listings)

brooklyn_ = []

for i in range(0, len(brooklyn_copy)):
    
    a_listing = {

            'days_on_market' : str(brooklyn_copy[i]['days_on_market']).replace('\n',' '),
            'agent_name' : str(brooklyn_copy[i]['agent_name']).replace('\n',' '),
            'description' : str(brooklyn_copy[i]['description']).replace('\n',' ')
        }
    
    brooklyn_.append(a_listing)
    
    
keys = brooklyn_[0].keys()

with open('brooklyn_additional.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(brooklyn_)


# In[ ]:


manhattan_copy = deepcopy(manhattan_listings)

manhattan_ = []

for i in range(0, len(manhattan_copy)):
    
    a_listing = {

            'days_on_market' : str(manhattan_copy[i]['days_on_market']).replace('\n',' '),
            'agent_name' : str(manhattan_copy[i]['agent_name']).replace('\n',' '),
            'description' : str(manhattan_copy[i]['description']).replace('\n',' ')
        }
    
    manhattan_.append(a_listing)
    
    
keys = manhattan_[0].keys()

with open('manhattan_additional.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(manhattan_)


# In[13]:


import csv


keys = bronx_[0].keys()

with open('bronx_additional.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(bronx_)


# In[ ]:


import csv


keys = brooklyn_[0].keys()

with open('brooklyn_additional.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(brooklyn_)


# In[ ]:


import csv


keys = manhattn_[0].keys()

with open('manhattan_additional.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(manhattan_)

