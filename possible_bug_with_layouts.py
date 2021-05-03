from os import stat
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import HorizontalSeparator

import CL_layouts as layouts

import CL_scrape as scrape

theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.theme_add_new('Dashboard', theme_dict)     # if using 4.20.0.1+
# sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
# sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))



def make_main_window():
    state_news = scrape.parse_state_news()

    state_news_content = []
    state_news_content.append([sg.Text('New Jersey State News', font='Any 20')])
    
    # for story in state_news:
    #     row = []
    #     chara_count = 0
    #     while chara_count < len(story['text']):
    #         cut_text = story['text'][chara_count: chara_count+80]
    #         # print('\nstory', story['text'], '\ncut_text', cut_text)
        
    #         row.append(
    #             [sg.Text(cut_text)]
    #         )
    #         chara_count += 80

    #     state_news_content.append([sg.Column(row)])
    #     state_news_content.append([HorizontalSeparator()])
        
        

    content = [
        [
            sg.Column(state_news_content, expand_x=True, scrollable=True, vertical_scroll_only=True),
            sg.Column([[sg.Text('Townships')], [sg.Button('Edison')]], expand_y=True, expand_x=True)
        ]
    ]
    
    layout = [
        layouts.create_top_banner(),
        layouts.create_heading(),
        [sg.Column(content, expand_y=True, expand_x=True)],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ', layout, size=(720, 540), margins=(0,0), finalize=True, background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)


def make_town_window():
    content = []

    Edison = scrape.get_data()

    for story in Edison.news:
        content.append([sg.Text(story['text'])])

    layout = [
        layouts.create_top_banner(),
        layouts.create_township_heading(Edison),
        [sg.Column(content, expand_y=True, expand_x=True, scrollable=True, vertical_scroll_only=True)],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ - Town Information', layout, size=(720, 540), finalize=True, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, grab_anywhere=False)


# window variables
win_main, win_town = make_main_window(), None

while True:             # Event Loop
    window, event, values = sg.read_all_windows() # read all events from all windows
    
    
    if window == win_main:
        if event in (sg.WIN_CLOSED, 'Exit', 'Quit'):
            break

        if event == 'Edison':
            print('Edison button clicked')
            win_main.hide()
            win_town = make_town_window()

        

    
    elif window == win_town:
        if event in (sg.WIN_CLOSED, 'Exit', 'Quit'):
            break
        
        if event in ('Home'):
            win_main.un_hide()
            win_town.close()

          
    
    else:
        print(event)




win_main.close()
if win_town:
    win_town.close()