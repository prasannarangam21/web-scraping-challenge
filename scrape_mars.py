from splinter import Browser
from bs4 import BeautifulSoup as bs

def scrape():
   executable_path = {'executable_path': 'chromedriver.exe'}
   browser = Browser('chrome', **executable_path, headless=False)
   news_title,news_p = mars_news(browser)

   # NASA Mars News Site Web Scraper
def mars_news(browser):
    # Visit the NASA Mars News Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    element = soup.select_one("ul.item_list li.slide")
    news_title = element.find("div",class_="content_title").text
    news_p = element.find("div",class_="article_teaser_body").text
    return news_title,news_p


   # NASA JPL (Jet Propulsion Laboratory) Site Web Scraper
def featured_image(browser):
    # Visit the NASA JPL (Jet Propulsion Laboratory) Site
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    
   
   # Mars Weather Twitter Account Web Scraper
def twitter_weather(browser):
    # Visit the Mars Weather Twitter Account
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    
    # Parse Results HTML with BeautifulSoup
    html = browser.html
    weather_soup = BeautifulSoup(html, "html.parser")

   # Mars Facts Web Scraper
def mars_facts():

   # Mars Hemispheres Web Scraper
def hemisphere(browser):
    # Visit the USGS Astrogeology Science Center Site
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)   