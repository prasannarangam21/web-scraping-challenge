from flask import Flask, render_template, redirect
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
from scrape_mars import scrape
# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# # Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_info = mongo.db.collection.find_one()
    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrapper():
    # Run the scrape function
    mars_info = mongo.db.collection
    # Update the Mongo database using update and upsert=True
    mars_data = scrape()
    mars_info.replace_one({},mars_data,upsert=True)
    # Redirect back to home page
    return redirect("/")
    
# Define Main Behavior
if __name__ == "__main__":
    app.run()
