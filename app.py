import flask
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__, template_folder="template")

# using PyMongo to establish connection 
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_mission")



@app.route("/")
def index():
    mars_info = mongo.db.collection.find_one()
    return render_template("index.html", mars_info = mars_info) 


# Route that will trigger the scrape function

@app.route("/scrape")
def scrape():
    # run the scrape function
    mars_info = scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)

    
