from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

   
    url = "https://github.com/assegidsamuel/webscraping/blob/master/WebScraping-Homework/News_NASA_Mars_Exploration_Program.html/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get news title
    news_title = news_soup.title.text

    # Get paragraph
    news_p = news_soup.body.find('p').text

    # Get featured image
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars" + image
    
    #get mars facts
    html_table = tables.html

    # Store data in a dictionary
   hemisphere_image_urls = {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"},
    
                        {"title": "Cerberus Hemisphere","img_url":"https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg "},
                        
                        {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"},
                        {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
                        
        

    # Close the browser after scraping
    browser.quit()

    # Return results
    return costa_data
