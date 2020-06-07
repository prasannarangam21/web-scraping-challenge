from flask import Flask, render_template
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
# Create an instance of our Flask app.
app = Flask(__name__)
# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
# Connect to a database. Will create one if not already available.
db = client.mars_db
# Flask Routes
@app.route("/")
def index():
    mars=
    return render_template("index.html", mars=mars)
# Scrape Route to Import `scrape_mars.py` Script & Call `scrape` Function
@app.route("/scrape")
def scrapper():
    mars = 
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return "Scraping Successful"

# Define Main Behavior
if __name__ == "__main__":
    app.run()
