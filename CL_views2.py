#===============================================================================
# Author: Christian Liguori
# Date: 05/04/21
# Program Name: CL_views2.py
# This file contains all of the functions that are used to create the 
#   windows for the GUI. It also contains the event loop that handles all
#   of the logic for the windows.
#===============================================================================


#===============================================================================
# Library Imports
#===============================================================================
# The PySimpleGUI library used to render GUIs
from tkinter import font
from tkinter.constants import W
import PySimpleGUI as sg

# Importing the layout functions that create layout pieces
import CL_layouts as layouts

# Importing the scrape functions that scrape and parse the web data
import CL_scrape as scrape
#===============================================================================


#===============================================================================
# Theme for the app. Sets the default styling of the app.
#===============================================================================
theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

# Adding the styling as a theme for the app
sg.theme_add_new('Dashboard', theme_dict) 
#===============================================================================


#===============================================================================
# The color scheme for the GUI. Taken from a PySimpleGUI example.
#===============================================================================
BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))
#===============================================================================


#===============================================================================
# Window creation functions
#===============================================================================
# These functions handle the creation of the final layouts of each window. They
#   combine the generic layouts and the window specific layouts. Each window
#   function generates the GUI elements that house the parsed data.
#===============================================================================
# State Windows
#===============================================================================
# Function to make the main window, which contains the state news.
def make_main_window():
    # Get the web data
    state_news = scrape.parse_state_news()

    # Variable to hold the constructed GUI elements
    state_news_content = []
    
    # For each story from the state news page, create a row and add to it
    #   the date and the story text, with the story text broken up into
    #   100 character long strings so that it will fit in the container. Then
    #   append the row and a separator to the content list.
    for story in state_news:
        row = []
        row.append([sg.Text(story['date'])])
        chara_count = 0
        while chara_count < len(story['text']):
            cut_text = story['text'][chara_count: chara_count+100]
        
            row.append(
                [sg.Text(cut_text)]
            )
            chara_count += 100

        state_news_content.append([sg.Column(row)])
        state_news_content.append([sg.HorizontalSeparator()])
        
    # Variable containing the total layout for the page. Combines the generic 
    #   layouts from the CL_layouts file and the window specific layouts.
    layout = [
        layouts.create_top_banner(),
        [
            sg.Column([
                [sg.Column([
                    [sg.Text('Counties:', font='Any 16')]
                ], expand_x=True), 
                sg.Column([
                    [sg.Button('Middlesex')]
                ])]
            ], expand_x=True)
        ],
        [sg.Column([
            [sg.Text('New Jersey State News', 
                font='Any 18', background_color=DARK_HEADER_COLOR
            )]
        ], background_color=DARK_HEADER_COLOR, expand_x=True)],

        [sg.Column(
            state_news_content, expand_x=True, expand_y=True, 
            scrollable=True, vertical_scroll_only=True, 
            vertical_alignment='top', size=(540, 300))
        ],
        layouts.create_footer()
    ]

    # Return a window object containing the finalized layout.
    return sg.Window(
        'Get Involved NJ', layout, size=(720, 540), margins=(0,0), 
        finalize=True, background_color=BORDER_COLOR, 
        no_titlebar=False, grab_anywhere=False
    )
#===============================================================================


#===============================================================================
# County windows
#===============================================================================
# Function to make the county window that contains the county news.
def make_county_window():
    # Get the web data
    county_news = scrape.parse_middlesex_county_news()

    # Variable to hold the constructed GUI elements
    county_news_content = []

    # For each story from the county news page, create a row and add to it
    #   the date and the story text, with the story text broken up into
    #   100 character long strings so that it will fit in the container. Then
    #   append the row and a separator to the content list.
    for story in county_news:
        row = []
        row.append([sg.Text(story['date'])])
        chara_count = 0
        while chara_count < len(story['text']):
            cut_text = story['text'][chara_count: chara_count+100]
            # print('\nstory', story['text'], '\ncut_text', cut_text)
        
            row.append(
                [sg.Text(cut_text)]
            )
            chara_count += 100

        county_news_content.append([sg.Column(row)])
        county_news_content.append([sg.HorizontalSeparator()])

    # Variable containing the total layout for the page. Combines the generic 
    #   layouts from the CL_layouts file and the window specific layouts.
    layout = [
        layouts.create_top_banner(back_button=True),
        [
            sg.Column([
                [sg.Column([
                    [sg.Text('Towns', font='Any 16')]
                ], expand_x=True), 
                sg.Column([
                    [sg.Button('Edison')]
                ])]
            ], expand_x=True)
        ],
        [sg.Column([
            [sg.Text('Middlesex County News', 
                font='Any 18', background_color=DARK_HEADER_COLOR
            )]], expand_x=True, background_color=DARK_HEADER_COLOR)],

        [sg.Column(
            county_news_content, expand_x=True, expand_y=True, 
            scrollable=True, vertical_scroll_only=True, 
            vertical_alignment='top', size=(540, 300))
        ],
        layouts.create_footer()
    ]

    # Return a window object containing the finalized layout.
    return sg.Window(
        'Get Involved NJ - County Information', layout, size=(720, 540), 
        margins=(0,0), finalize=True, background_color=BORDER_COLOR, 
        no_titlebar=False, grab_anywhere=False)
#===============================================================================


#===============================================================================
# Town Windows
#===============================================================================
# Function to make the town news window, which is the default window for towns.
def make_town_news_window():
    # Get the web data
    town_news = scrape.parse_edison_news()

    # Variable to hold the constructed GUI elements
    town_news_content = []

    # For each story from the town news page, append the story text and
    #   a separator.
    for story in town_news:
        town_news_content.append([sg.Text(story['text'], size=(100, None))])
        town_news_content.append([sg.HorizontalSeparator()])

    # Variable containing the total layout for the page. Combines the generic 
    #   layouts from the CL_layouts file and the window specific layouts.
    layout = [
        layouts.create_top_banner(back_button=True),
        [
            sg.Column([[
                sg.Column([
                    [sg.Text('Edison', font='Any 16')]
                ], expand_x=True),

                sg.Column([
                    [sg.Button('News'), 
                    sg.Button('Dept. Info'), 
                    sg.Button('Town Meeting Info')]
                ])
            ]], expand_x=True)
        ],
        [sg.Column([
            [sg.Text('Edison Township News', 
                font='Any 18', background_color=DARK_HEADER_COLOR
            )]
        ], background_color=DARK_HEADER_COLOR, expand_x=True)],

        [sg.Column(
            town_news_content, expand_x=True, expand_y=True, 
            scrollable=True, vertical_scroll_only=True, 
            vertical_alignment='top', size=(540, 300))
        ],
        layouts.create_footer()
    ]

    # Return a window object containing the finalized layout.
    return sg.Window(
        'Get Involved NJ - Town Information', layout, size=(720, 540), 
        finalize=True, margins=(0,0), background_color=BORDER_COLOR, 
        no_titlebar=False, grab_anywhere=False
    )
#===============================================================================





#===============================================================================
def make_town_department_window():
    town_dept_contacts = scrape.parse_edison_department_contacts()

    town_dept_contacts_content = []
    # town_dept_contacts_content.append([sg.Text('Edison Township Dept. Info')])

    for table_entry in town_dept_contacts:
        row = []
        
        for item in table_entry:
            row.append(sg.Text(item))
        

        town_dept_contacts_content.append([sg.Column([row])])
        town_dept_contacts_content.append([sg.HorizontalSeparator()])


    layout = [
        layouts.create_top_banner(back_button=True),
        [
            sg.Column([[
                sg.Column([
                    [sg.Text('Edison', font='Any 16')]
                ], expand_x=True),

                sg.Column([
                    [sg.Button('News'), 
                    sg.Button('Dept. Info'), 
                    sg.Button('Town Meeting Info')]
                ])
            ]], expand_x=True)
        ],
        [sg.Column([[sg.Text('Edison Township Dept. Contact Info', font='Any 18', background_color=DARK_HEADER_COLOR)]], background_color=DARK_HEADER_COLOR, expand_x=True)],
        [sg.Column(town_dept_contacts_content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300))],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ - County Information', layout, size=(720, 540), margins=(0,0), finalize=True, background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)
#===============================================================================


#===============================================================================
def make_town_meeting_window():
    town_meetings = scrape.parse_edison_town_meetings()

    town_meetings_content = []
    # town_meetings_content.append([sg.Text('Edison Township Meeting Info')])

    for table_entry in town_meetings:
        print(table_entry)
        row = []
        
        row.append([sg.Text(table_entry[0]), sg.Text(table_entry[1])])
        row.append([sg.Text(table_entry[2])])
        row.append([sg.Text('Meeting ID: ' + table_entry[3])])
        row.append([sg.Text('Passcode: ' + table_entry[4])])
        

        town_meetings_content.append([sg.Column(row)])
        town_meetings_content.append([sg.HorizontalSeparator()])


    layout = [
        layouts.create_top_banner(back_button=True),
        [
            sg.Column([[
                sg.Column([
                    [sg.Text('Edison', font='Any 16')]
                ], expand_x=True),

                sg.Column([
                    [sg.Button('News'), 
                    sg.Button('Dept. Info'), 
                    sg.Button('Town Meeting Info')]
                ])
            ]], expand_x=True)
        ],
        [sg.Column([[sg.Text('Edison Township Meeting Info', font='Any 18', background_color=DARK_HEADER_COLOR)]], background_color=DARK_HEADER_COLOR, expand_x=True)],
        [sg.Column(town_meetings_content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300))],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ - County Information', layout, size=(720, 540), margins=(0,0), finalize=True, background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)
#===============================================================================


#===============================================================================
def make_progress_window():

    layout = [
        [sg.Column([
            [sg.Text('Gathering data...', font='Any 20')],
            [sg.Text('Please wait.', font='Any 20')],
        ], expand_x=True, expand_y=True, element_justification='center')],
        
        [sg.ProgressBar(len(scrape.scrape_functions) - 1, key='PROGRESS_BAR', size=(100, 20))]
    ]

    return sg.Window('Get Involved NJ - County Information', layout, size=(360, 150), margins=(0,0), finalize=True, background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)

#===============================================================================


#===============================================================================
# Function that contains all of the event logic that handles the transitions
#   between the windows.
def main():
    # Variables for storing the created windows.
    win_town_meetings = None
    win_town_dept = None
    win_town_news = None
    win_county = None
    win_main = None
    win_progress = make_progress_window()

    # Execute each of the scrape functions while updating the progress bar on
    #   the progress window.
    for i in range(len(scrape.scrape_functions)):
        scrape.scrape_functions[i]()
        win_progress['PROGRESS_BAR'].update(i)

    # Hide the progress window
    win_progress.hide()

    # Create the main window
    win_main = make_main_window()

    # Close and Destroy the progress window
    win_progress.close()
    win_progress = None

    # Always running event loop that catches all of the events fired by
    #   the windows.
    while True:
        # Funtion that reads any events fired by the windows. The timeout 
        #   field determines how often it will check for new events.
        window, event, values = sg.read_all_windows(timeout=100)

        # Event handlers
        # 1st Level
        if window == win_main:
            if event in (sg.WIN_CLOSED, 'Quit'):
                break

            if event == 'Middlesex':
                win_main.hide()
                win_county = make_county_window()
                # Now in 2nd Level

        
        # 2nd Level
        if window == win_county:
            if event in (sg.WIN_CLOSED, 'Quit'):
                break

            if event in ('Back', 'Home'):
                win_county.hide()
                win_main.un_hide()
                win_county.close()
                win_county = None

            if event == 'Edison':
                win_county.hide()
                win_town_news = make_town_news_window()
                # Now in 3rd Level

        # 3rd Level
        if window in (win_town_dept, win_town_news, win_town_meetings):
            if event in (sg.WIN_CLOSED, 'Quit'):
               break

            if event == 'Back':
                window.hide()
                win_county.un_hide()
                window.close()
                win_town_dept = None
                win_town_meetings = None
                win_town_news = None

            if event == 'Home':
                window.hide()
                win_main.un_hide()
                win_county.close()
                window.close()
                win_town_dept = None
                win_town_meetings = None
                win_town_news = None
                win_county = None

            if event == 'News' and window != win_town_news:
                window.hide()
                win_town_news = make_town_news_window()
                window.close()
                win_town_dept = None
                win_town_meetings = None

            if event == 'Dept. Info' and window != win_town_dept:
                window.hide()
                win_town_dept = make_town_department_window()
                window.close()
                win_town_meetings = None
                win_town_news = None

            if event == 'Town Meeting Info' and window != win_town_meetings:
                window.hide()
                win_town_meetings = make_town_meeting_window()
                window.close()
                win_town_dept = None
                win_town_news = None
        
    win_main.close()
#===============================================================================


#===============================================================================
if __name__ == '__main__':
    main()
#===============================================================================