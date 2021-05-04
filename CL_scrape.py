#===============================================================================
# Author: Christian Liguori
# Date: 05/04/21
# Program Name: CL_scrape.py
# This file contains all of the scrape and parsing functions that retrieve and
#   organize the data for the app that comes from external sources.
#===============================================================================


#===============================================================================
# Library Imports
#===============================================================================
# Beautiful Soup library that is used for parsing site data
from bs4 import BeautifulSoup

# request library used to download the site data
from urllib import request

# Import the data objects used to organize the data.
import CL_data_objects as do
#===============================================================================


#===============================================================================
# State Functions
#===============================================================================
# Variable to store the NJ state web site link.
New_Jersey_state_news_link = \
    'https://nj.gov/governor/news/news/562021/approved/news_archive.shtml'


#===============================================================================
# Function to download the web page with the official NJ state news.
def scrape_state_news():
    # Download the web page html
    web_data = request.urlopen(New_Jersey_state_news_link)

    # Parse the data through beautiful soup to organize the raw html
    parsed_data = BeautifulSoup(web_data, 'html.parser')

    # Create an html file to store the web data 
    file = open('./scraped_html/new_jersey_news.html', 'w')
    
    # Write an organized version of the web data to the local file
    file.write(str(parsed_data.prettify()))

    # Close the file to free up resources
    file.close()
#===============================================================================


#===============================================================================
# Function to parse and organize the NJ state news from the web page.
def parse_state_news():
    # Open the file with the scraped data
    web_page = open('./scraped_html/new_jersey_news.html')

    # Organize the data with beautiful soup
    parsed_data = BeautifulSoup(web_page, 'html.parser')

    # Grab all of the divs with a class of 'press-item'
    parsed_data = parsed_data.find_all('div', class_='press-item')

    # Variable to store the processed data
    state_news = []

    # for each div found, loop through each child element and extract the 
    #   text from it in the correct format.
    for element in parsed_data:
        data_row = {}
        for item in element.find_all('div'):
            if item['class'] == ['date']: 
                data_row['date'] = item.span.text.strip() + ' ' + \
                    item.div.text.strip()
            
            elif item['class'] == ['content']:
                data_row['text'] = item.h4.text.strip()
                data_row['link'] = 'https://nj.gov' + item.p.a['href']

        # append the data row to the list
        state_news.append(data_row)

    return state_news
#===============================================================================


#===============================================================================
# County Functions
#===============================================================================
# I am unable to scrape the county news using beautiful soup, because the 
#   data is loaded onto the page through additional browser requests. I
#   would need to use selenium or another advanced tool to properly scrape the 
#   site which is outside of the project's scope. So right now the data was 
#   scraped manually.
def scrape_middlesex_county_news():
    web_data = request.urlopen(
        'http://www.middlesexcountynj.gov/News/Pages/default.aspx')

    parsed_data = BeautifulSoup(web_data, 'html.parser')

    # Needed to add the encoding to write the data
    file = open(
        './scraped_html/middlesex_county_news.html', 'w', encoding='utf-8')
    
    file.write(str(parsed_data))

    file.close()
#===============================================================================


#===============================================================================
# Function to parse and organize the Middlesex county news from the web page.
def parse_middlesex_county_news():
    # Open the file with the scraped data
    web_page = open('./scraped_html/middlesex_county_news.html')

    # Organize the data with beautiful soup
    parsed_data = BeautifulSoup(web_page, 'html.parser')

    # Grab all of the divs with a class of 'news'
    news_items = parsed_data.find_all('div', class_='news')

    # Variable to store the processed data
    middlesex_county_news = []

    # For each div grabbed, get the text and link from the child anchor element,
    #   and get the text from the child span element. The append the contents
    #   of the div to the list.
    for item in news_items:
        data = {}

        data['text'] = item.h4.a.get_text()
        data['link'] = 'http://www.middlesexcountynj.gov' + item.h4.a['href']
        data['date'] = item.span.get_text()

        middlesex_county_news.append(data)
    
    return middlesex_county_news
#===============================================================================


#===============================================================================
# Township Functions
#===============================================================================
# Variables to hold the Edison township web site links.
Edison_Twsp_news_link = \
    'https://edisonnj.org/newslist.php'
Edison_Twsp_town_meetings_link = \
    'https://www.edisonnj.org/zoommeetings/index.php'



#===============================================================================
# Function to download the web page with the official Edison Twsp. news.
def scrape_edison_news():
    # Download the web page html
    web_data = request.urlopen(Edison_Twsp_news_link)

    # Parse the data through beautiful soup to organize the raw html
    parsed_data = BeautifulSoup(web_data, 'html.parser')

    # Create an html file to store the web data 
    file = open('./scraped_html/edison_township_news.html', 'w')
    
    # Write an organized version of the web data to the local file
    file.write(str(parsed_data.prettify()))

    # Close the file to free up resources
    file.close()
#===============================================================================


#===============================================================================
# Function to parse and organize the Edison Twsp. news from the web page.
def parse_edison_news():
    # Open the file with the scraped data
    web_page = open('./scraped_html/edison_township_news.html')

    # Organize the data with beautiful soup
    parsed_data = BeautifulSoup(web_page, 'html.parser')

    # Grab the paragraph elements inside of the div element with the post class
    parsed_data = parsed_data.select('div.post p')
    
    # Variable to store the processed data
    town_news = []

    # For each paragraph found, grab the link from the child anchor tag, and
    #   clean the spaces in the url, and grab the text of the paragraph. Then
    #   store it in a dictionary and append it to the list of news.
    for story in parsed_data:
        town_news.append(
            {
                'link':story.a['href'].replace(' ', '%20'), 
                'text':story.text.strip()
            }
        )

    return town_news
#===============================================================================


#===============================================================================
# Function to download the web page with the Edison Twsp. town meeting info.
def scrape_edison_town_meetings():
    # Download the web page html
    web_data = request.urlopen(Edison_Twsp_town_meetings_link)

    # Parse the data through beautiful soup to organize the raw html
    parsed_data = BeautifulSoup(web_data, 'html.parser')

    # Create an html file to store the web data 
    file = open('./scraped_html/edison_town_meeting.html', 'w')
    
    # Write an organized version of the web data to the local file
    file.write(str(parsed_data.prettify()))

    # Close the file to free up resources
    file.close()
#===============================================================================


#===============================================================================
# Function to parse and organize the Edison Twsp. news from the web page.
def parse_edison_town_meetings():
    # Open the file with the scraped data
    web_page = open('./scraped_html/edison_town_meeting.html')

    # Organize the data with beautiful soup
    parsed_data = BeautifulSoup(web_page, 'html.parser')
    
    # Grab all of the table row elements on the page
    parsed_data = parsed_data.table.find_all('tr')

    # Variable to store the processed data
    meeting_info = []
    
    # For each table row, grab all of the table data elements in it, cleaning 
    #   up any unicode characters. If the table data element contains an
    #   anchor element, grab the link, else grab the text. Append the data to
    #   row as long as it is not empty.
    for row in parsed_data:
        row_data = []
        for entry in row.find_all('td'):
            text = entry.text.replace('\xa0', '').strip()
            
            if entry.a:
                text = entry.a['href']
            
            if text != '':
                row_data.append(text)

        if row_data != []:
            meeting_info.append(row_data)

    return meeting_info
#===============================================================================


#===============================================================================
# Function to download the web page with the Edison Twsp. dept. contact info.
def scrape_edison_department_contacts():
    # Download the web page html
    web_data = request.urlopen('https://edisonnj.org/how_do_i/contact_us.php')

    # Parse the data through beautiful soup to organize the raw html
    parsed_data = BeautifulSoup(web_data, 'html.parser')

    # Create an html file to store the web data 
    file = open('./scraped_html/edison_department_info.html', 'w')
    
    # Write an organized version of the web data to the local file
    file.write(str(parsed_data.prettify()))

    # Close the file to free up resources
    file.close()
#===============================================================================


#===============================================================================
# Function to parse and organize the Edison Twsp. dept. info from the web page.
def parse_edison_department_contacts():
    # Open the file with the scraped data
    web_page = open('./scraped_html/edison_department_info.html')

    # Organize the data with beautiful soup
    parsed_data = BeautifulSoup(web_page, 'html.parser')

    # Get the table data
    parsed_data = parsed_data.find(class_='post').table

    # Variable to store the processed data
    table = []

    # For each table row, grab all of the table data elements. Then, for each
    #   table data elements, grab all of the cleaned text strings, using the
    #   stripped_strings helper function of beautiful soup, grabbing and 
    #   cleaning the link if one is found. The text is then appended to the
    #   list of data.
    for table_row in parsed_data.find_all('tr'):
        data = []
        for table_data in table_row.find_all('td'):
            
            for string in table_data.stripped_strings:
                data.append(string)
                if table_data.a:
                    data.append(table_data.a['href'].split(':')[1])
        table.append(data)

    return table
#===============================================================================


#===============================================================================
# List that stores references to each of the scraping functions. The Middlesex 
#   county news is scraped manually because the way the web site renders the
#   data dynamically. 
scrape_functions = [
    scrape_state_news,
    # scrape_middlesex_county_news,
    scrape_edison_news,
    scrape_edison_department_contacts,
    scrape_edison_town_meetings
]

#===============================================================================
# Function that calls all of the scrape functions .
def scrape_all():
    for func in scrape_functions:
        func()
#===============================================================================


#===============================================================================
# If run as main file functions
#===============================================================================
# If this file is run as the main file, then it call a function. This was used
#   for testing and when working through the data parsing.
if __name__ == '__main__':
    # scrape_edison_town_meetings()
    # parse_edison_town_meetings()

    # scrape_edison_department_contacts()
    # parse_edison_department_contacts()

    # scrape_state_news()
    # parse_state_news()

    # scrape_middlesex_county_news()
    # parse_middlesex_county_news()

    # print(parse_middlesex_county_news())
    # print(parse_edison_department_contacts())
    # print(parse_edison_town_meetings())
    scrape_all()
    pass