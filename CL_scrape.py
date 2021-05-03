# Beautiful Soup library that is used for scraping site data
from bs4 import BeautifulSoup
# request library used to download the site data
from urllib import request

import CL_data_objects as do



Edison_Twsp = do.Township('Edison')

Edison_Twsp.links['news'] = 'https://edisonnj.org/newslist.php'
Edison_Twsp.links['town_meetings'] = 'https://www.edisonnj.org/zoommeetings/index.php'
Edison_Twsp.links['calendar'] = 'https://edisonnj.org/calendar.php'


New_Jersey_News = 'https://nj.gov/governor/news/news/562021/approved/news_archive.shtml'

def scrape_state_news():
    web_data = request.urlopen(New_Jersey_News)

    parsed_data = BeautifulSoup(web_data, 'html.parser')

    file = open('./scraped_html/new_jersey_news.html', 'w')
    
    file.write(str(parsed_data.prettify()))

    file.close()

def parse_state_news():
    web_page = open('./scraped_html/new_jersey_news.html')

    parsed_data = BeautifulSoup(web_page, 'html.parser').find_all('div', class_='press-item')

    state_news = []

    for element in parsed_data:
        data_row = {}
        for item in element.find_all('div'):
            if item['class'] == ['date']:
                # print(item.span.text.strip(), item.div.text.strip())
                data_row['date'] = item.span.text.strip() + ' ' + item.div.text.strip()
            
            elif item['class'] == ['content']:
                # print(item.h4.text.strip())
                data_row['text'] = item.h4.text.strip()
                # print('https://nj.gov' + item.p.a['href'])
                data_row['link'] = 'https://nj.gov' + item.p.a['href']

        state_news.append(data_row)

    return state_news



def get_data():

    news_data = request.urlopen(Edison_Twsp.links['news'])


    parsed_data = BeautifulSoup(news_data, 'html.parser').select('div.post p')
    for story in parsed_data:
        print('''
            link: 'https://edisonnj.org/{}'
            text: {}
        '''.format(story.a['href'].replace(' ', '%20'), story.text))

        Edison_Twsp.news.append({'link':story.a['href'].replace(' ', '%20'), 'text':story.text})

    return Edison_Twsp


def scrape_edison_town_meetings():

    web_data = request.urlopen(Edison_Twsp.links['town_meetings'])

    parsed_data = BeautifulSoup(web_data, 'html.parser')

    file = open('./scraped_html/edison_town_meeting.html', 'w')
    
    file.write(str(parsed_data.prettify()))

    file.close()


def parse_edison_town_meetings():
    web_page = open('./scraped_html/edison_town_meeting.html')

    parsed_data = BeautifulSoup(web_page, 'html.parser').select('div.post')

    for element in parsed_data:
        print(element.get_text())

def scrape_edison_department_contacts():
    web_data = request.urlopen('https://edisonnj.org/how_do_i/contact_us.php')

    parsed_data = BeautifulSoup(web_data, 'html.parser')

    file = open('./scraped_html/edison_department_info.html', 'w')
    
    file.write(str(parsed_data.prettify()))

    file.close()


def parse_edison_department_contacts():
    web_page = open('./scraped_html/edison_department_info.html')

    parsed_data = BeautifulSoup(web_page, 'html.parser')

    # Get the table data
    parsed_data = parsed_data.find(class_='post').table

    table = []

    for table_row in parsed_data.find_all('tr'):
        data = []
        for table_data in table_row.find_all('td'):
            
            for string in table_data.stripped_strings:
                data.append(string)
                if table_data.a:
                    data.append(table_data.a['href'].split(':')[1])
        table.append(data)
                

    for row in table:
        print(row)


# I am unable to scrape the county news using beautiful soup, because the 
#   data is loaded onto the page through additional browser requests. I
#   would need to use selenium or another advanced tool to properly scrape the 
#   site. So right now the data was scraped manually.
def scrape_middlesex_county_news():
    web_data = request.urlopen('http://www.middlesexcountynj.gov/News/Pages/default.aspx')

    parsed_data = BeautifulSoup(web_data, 'html.parser')

    # Needed to add the encoding to write the data
    file = open('./scraped_html/middlesex_county_news.html', 'w', encoding='utf-8')
    
    file.write(str(parsed_data))

    file.close()

def parse_middlesex_county_news():
    web_page = open('./scraped_html/middlesex_county_news.html')

    parsed_data = BeautifulSoup(web_page, 'html.parser')

    news_items = parsed_data.find_all('div', class_='news')

    middlesex_county_news = []

    for item in news_items:
        data = {}
        # print()
        # print(item.h4.a.get_text())
        # print('http://www.middlesexcountynj.gov' + item.h4.a['href'])
        # print(item.span.get_text())

        data['text'] = item.h4.a.get_text()
        data['link'] = 'http://www.middlesexcountynj.gov' + item.h4.a['href']
        data['date'] = item.span.get_text()

        middlesex_county_news.append(data)
    
    return middlesex_county_news




if __name__ == '__main__':
    # scrape_edison_town_meetings()
    # parse_edison_town_meetings()

    # scrape_edison_department_contacts()
    # parse_edison_department_contacts()

    # scrape_state_news()
    # parse_state_news()

    # scrape_middlesex_county_news()
    # parse_middlesex_county_news()

    print(parse_middlesex_county_news())