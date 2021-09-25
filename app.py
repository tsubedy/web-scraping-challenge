from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__, template_folder="template")

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
collection = db.items


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    mars_db = collection.find().next()
    return render_template("index.html", mars_info = mars_db)


# Route that will trigger the scrape function
@app.route("/scrape")

def scrape():
    # run the scrape function
    mars_db = scrape_mars.scrape_info()

    # update the Mongo database using update and upsert = true
    client.db.collecton.update({}, mars_db, upsert = True)
    
    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

    
