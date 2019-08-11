from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import time


# Define scrape function
def scrape():
    mars_library = {}
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Mars News
    url1 = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url1)
    html = browser.html
    soup = bs(html, "html.parser")
    news_title = soup1.find_all('div', class_='content_title')[0].find('a').text.strip()
    news_p = soup.find_all('div', class_='rollover_description_inner')[0].text.strip()
    mars_library['news_title'] = news_title
    mars_library['news_p'] = news_p

    # Mars Space Images
    url2='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response2 = requests.get(url2)
    soup2 = bs(response2.text, 'html.parser')
    image=soup2.find_all('img')[3].get('src').strip()
    featured_image_url=url2+image
    mars_library['mars_space'] = image

    # Mars Weather
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3)
    html = browser.html
    soup3 = bs(html, "html.parser")
    mars_weather1 = soup3.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text
    mars_weather2 = mars_weather1[:-26]
    mars_library['mars_weather'] = mars_weather2


    # Mars Facts
    url4 = 'https://space-facts.com/mars/'
    tables = pd.read_html(url4)
    data = tables[0]
    mars_facts=data.to_html
    mars_library['mars_facts'] = mars_facts


    # Mars Hemispheres
    url6='https://astrogeology.usgs.gov'
    hemisphere=soup5.find_all('div',class_='item')
    title = []
    img_url = []
    hemisphere_image_urls={}
    for x in range(4):
        img_url.append(url6+hemisphere[x].find('a').get('href').strip()+'.tif/full.jpg')
        title.append(hemisphere[x].find('a').text.strip())
        hemisphere_image_urls['title']=title
        hemisphere_image_urls['img_url']=img_url
    return mars_library