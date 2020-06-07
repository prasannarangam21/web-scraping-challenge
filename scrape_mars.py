from splinter import Browser
from bs4 import BeautifulSoup as bs
def init_browser():
   executable_path = {'executable_path': 'chromedriver.exe'}
   browser = Browser('chrome', **executable_path, headless=False)
def scrape():
    browser = init_browser()
   # NASA Mars News Site Web Scraper
def mars_news(browser):
    # Visit the NASA Mars News Site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
   # NASA JPL (Jet Propulsion Laboratory) Site Web Scraper
def featured_image(browser):
    # Visit the NASA JPL (Jet Propulsion Laboratory) Site
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    # Ask Splinter to Go to Site and Click Button with Class Name full_image
    # <button class="full_image">Full Image</button>
    full_image_button = browser.find_by_id("full_image")
    full_image_button.click()
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