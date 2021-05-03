## News
class News_Story():
    def __init__(self, title, text, link):
        self.title = title
        self.text = text
        self.link = link

class Data_Store():
    def __init__(self, entity_name, link_dict):
        self.entity_name = entity_name
        self.link_dict = link_dict

class Township():
    name = ''
    departments = {}
    links = {
        'home': '',
        'department_contact_info': '',
        'town_meeting_info': '',
        'agendas'
        'news': '',
        'elections:': '',

    }
    news = []

    def __init__(self, name):
        self.name = name


# Edison Township data
departments_page = 'https://edisonnj.org/departments/index.php'

