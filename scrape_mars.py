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
    html = browser.html
    soup = BeautifulSoup(html_image, 'html.parser')
    image = soup.select_one("figure.lede a img").get("src")
    image_url = f"https://www.jpl.nasa.gov{image}"
    return image_url
    
   
   # Mars Weather Twitter Account Web Scraper
def twitter_weather(browser):
    # Visit the Mars Weather Twitter Account
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html_image, 'html.parser')
    latest_tweets = soup.find("span",text=re.compile(r"InSight")).text
    return latest_tweets


   # Mars Facts Web Scraper
def mars_facts():
   facts_url = 'http://space-facts.com/mars/'
   browser.visit(facts_url)
   # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
   mars_df = mars_facts_table[0]
   # Assign the columns `['Description', 'Value']`
   mars_df.columns = ['Description','Value']
   # Set the index to the `Description` column without row indexing
   mars_df.set_index('Description', inplace=True)
   # Save html code to folder Assets
   html_table = mars_df.to_html()
   return html_table

   # Mars Hemispheres Web Scraper
def hemisphere(browser):
    # Visit the USGS Astrogeology Science Center Site
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)   
    #Find the links to hemispheres
    all_links = browser.find_by_css("a.product-item h3")
    hemispheres = []
    for i,link in enumerate(all_links):
    hemisphere={}
    browser.find_by_css("a.product-item h3")[i].click()
    hemisphere["url"] = browser.links.find_by_partial_text("Sample").first["href"]
    hemisphere["title"] = browser.find_by_css("h2.title").text
    hemispheres.append(hemisphere)
    browser.back()
    return hemispheres