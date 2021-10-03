
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd
from pprint import pprint
from urllib.parse import urlsplit
import pymongo

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
collection = db.items


def init_browser():
    # capture path to chrome driver 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    mars_info = {}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # scrape latest news headline and para
    news_title=soup.find('ul', class_='item_list').\
                find('li', class_='slide').\
                find('div', class_= 'content_title').text

    news_para=soup.find("div", class_='article_teaser_body').text

    mars_info['news_title'] = news_title
    mars_info['news_para'] = news_para 
    

    # Featured image

    featured_image = "https://www.nasa.gov/image-feature/jpl/perseverance-s-first-full-color-look-at-mars"
    browser.visit(featured_image)

    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(featured_image))
    
    # click on featured image using xpath
    xpath = '//*[@id="468477"]/div[2]/div[2]/a/img'
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()

    time.sleep(1)

    #get image url using BeautifulSoup
    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    featured_img_url = soup.find('img')['src']
    mars_info['featured_img_url'] = featured_img_url


    # Mars Facts
    url_facts = "https://space-facts.com/mars/"
    table = pd.read_html(url_facts)
    table[0]

    df_mars_facts = table[0]
    df_mars_facts.columns = ["Parameter", "Values"]
    fact_table = df_mars_facts.set_index(["Parameter"])

    mars_html_table = fact_table.to_html()
    mars_html_table = mars_html_table.replace("\n", "")
    mars_info['mars_facts_table'] = mars_html_table

    # Mars Hemisphere
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)

    #Get base url
    hemisphere_base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(hemisphere_url))
    
    # list of xpaths for mars hemispheres
    xpaths = ['//*[@id="product-section"]/div[2]/div[1]/a/img', '//*[@id="product-section"]/div[2]/div[2]/a/img', '//*[@id="product-section"]/div[2]/div[3]/a/img', '//*[@id="product-section"]/div[2]/div[4]/a/img']
    hemisphere_img_urls = []

    for xpath in xpaths:
        hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemisphere_url)

        results = browser.find_by_xpath(xpath)
        img = results[0]
        img.click()
        time.sleep(1)

        #get image url using BeautifulSoup
        html_image = browser.html
        soup = BeautifulSoup(html_image, "html.parser")
        img_url = soup.find("img", class_='wide-image')["src"]

        time.sleep(1)
        img_url = hemisphere_base_url + img_url
        title = soup.find("h2",class_="title").text

        hemisphere_img_urls.append({'title': title, 'image_url':img_url})
        
        mars_info['hemisphere_img_urls'] = hemisphere_img_urls
        
    browser.quit()

    # collection.insert_one(mars_info)
    
    return mars_info

    


