# web-scraping-challenge

## STEP 1.

In this assignment, a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page was built under the given oputlines as following.

1. Completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

2. Created a Jupyter Notebook file called mission_to_mars.ipynb and used it to complete all of the scraping and analysis tasks. Scraping was done as in the following outlines.

#### Mars News:
- Scraping NASA Mars News Site and collecting the latest News Title and Paragraph Text was perfomed. The texts were assigned to a variable for later use.

#### Featured Image: 
- The url for JPL Featured Space Image was visited using splinter to navigate the site and findign the image url for the most recent Featured Mars Image and assigned the url string to a variable called featured_image_url.
- Making sure to find the image url to the full size in .jpg format.
- Makign sure to save a complete url string of the image.
    
#### Mars Facts: 
- Visited the Mars Facts webpage and scraped the table containing facts about the planet including Diameter, Mass, etc using Pandas and converting the data to HTML table string.

#### Mars Hemispheres:
- From the USGS Astrogeology site obtained high resolution images for each of Mar’s hemispheres. Both the image url string for the full resolution hemisphere image and the Hemisphere title containing the hemisphere name are saved. 

- Python dictionary was used to store the data using the keys img_url and title.

- The dictionary with the image url string and the hemisphere title was appended to a list containing one dictionary for each hemisphere.


## STEP 2.

- Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

- Started by converting Jupyter notebook codes into a Python script called scrape_mars.py with a function called scrape that executes all of the scraping codes from above and return one Python dictionary containing all of the scraped data.

- Next, a route called /scrape was created that imports scrape_mars.py script and calls the scrape function.

- The returned values were stored in Mongo as a Python dictionary.

- Created a root route / that queries Mongo database and passes the mars data into an HTML template to display the data.

- Created a template HTML file called index.html that takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 

## Results:
- the web app that displays the information in a single HTML is created. The screenshots of the final site is provided as .png files in the repository. 

__________
Thank you





