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
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Column

import CL_layouts as layouts

import CL_scrape as scrape
#===============================================================================


#===============================================================================
theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.theme_add_new('Dashboard', theme_dict) 
#===============================================================================


BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))
#===============================================================================



#===============================================================================

#===============================================================================
def make_main_window():
    state_news = scrape.parse_state_news()

    state_news_content = []
    state_news_content.append([sg.Text('New Jersey State News', font='Any 20')])
    
    for story in state_news:
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

        state_news_content.append([sg.Column(row)])
        state_news_content.append([sg.HorizontalSeparator()])
        

    layout = [
        layouts.create_top_banner(),
        # layouts.create_heading(),
        [
            sg.Column([
                [sg.Column([
                    [sg.Text('Counties', font='Any 16')]
                ], expand_x=True), 
                sg.Column([
                    [sg.Button('Middlesex')]
                ])]
            ], expand_x=True)
        ],
        [sg.Column(state_news_content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300))],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ', layout, size=(720, 540), margins=(0,0), finalize=True, background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)
#===============================================================================


#===============================================================================

def make_town_window():
    content = []

    Edison = scrape.parse_edison_news()

    for story in Edison:
        content.append([sg.Text(story['text'])])

    layout = [
        layouts.create_top_banner(),
        layouts.create_township_heading('Edison'),
        [sg.Column(content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300))],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ - Town Information', layout, size=(720, 540), finalize=True, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)
#===============================================================================


#===============================================================================
def make_county_window():
    county_news = scrape.parse_middlesex_county_news()

    county_news_content = []
    county_news_content.append([sg.Text('Middlesex County News')])

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

    layout = [
        layouts.create_top_banner(),
        # layouts.create_heading(),
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
        [sg.Column(county_news_content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300))],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ - County Information', layout, size=(720, 540), margins=(0,0), finalize=True, background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)
#===============================================================================


#===============================================================================
def make_town_department_window():
    town_dept_contacts = scrape.parse_edison_department_contacts()

    town_dept_contacts_content = []
    town_dept_contacts_content.append([sg.Text('Edison Township Dept. Info')])

    for table_entry in town_dept_contacts:
        row = []
        
        for item in table_entry:
            row.append(sg.Text(item))
        

        town_dept_contacts_content.append([sg.Column([row])])
        town_dept_contacts_content.append([sg.HorizontalSeparator()])


    layout = [
        layouts.create_top_banner(),
        layouts.create_heading(),
        [[sg.Text('Townships')], [sg.Button('Edison')]],
        [sg.Column(town_dept_contacts_content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300))],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ - County Information', layout, size=(720, 540), margins=(0,0), finalize=True, background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)
#===============================================================================


#===============================================================================
def make_town_meeting_window():
    town_meetings = scrape.parse_edison_town_meetings()

    town_meetings_content = []
    town_meetings_content.append([sg.Text('Edison Township Meeting Info')])

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
        layouts.create_top_banner(),
        layouts.create_heading(),
        [[sg.Text('Townships')], [sg.Button('Edison')]],
        [sg.Column(town_meetings_content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300))],
        layouts.create_footer()
    ]

    return sg.Window('Get Involved NJ - County Information', layout, size=(720, 540), margins=(0,0), finalize=True, background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)
#===============================================================================


#===============================================================================
def main():
    # Design pattern 1 - First window does not remain active
    win_town_meetings = None
    win_town_dept = None
    window3 = None
    window2 = None
    window1 = make_main_window()

    while True:
        window, event, values = sg.read_all_windows(timeout=100)

        if event in (sg.WIN_CLOSED, 'Quit') and window == window1:
            break

        if window == window1:
            # window1['-OUTPUT-'].update(values['-IN-'])
            pass

        if event == 'Middlesex' and not window2 and not window3:
            window1.hide()
            window2 = make_county_window()
            print(window2)

        if event == 'Edison':
            print(window, event)
            window2.hide()
            window3 = make_town_window()


        if window == window2 and (event in (sg.WIN_CLOSED, 'Quit', 'Home')):
            window2.close()
            window2 = None
            window1.un_hide()

        if window == window3 and (event in (sg.WIN_CLOSED, 'Quit', 'Home')):
            window3.close()
            window3 = None
            window2.un_hide()

        if window == window3 and event == 'Dept. Info':
            window3.hide()
            win_town_dept = make_town_department_window()

        if window in (window3, win_town_dept) and event == 'Town Meeting Info':
            window.hide()
            win_town_meetings = make_town_meeting_window()

        if window == win_town_dept and event in (sg.WIN_CLOSED, 'Quit', 'Home'):
            win_town_dept.close()
            win_town_dept = None
            window3.un_hide()

        if window == win_town_meetings and event in (sg.WIN_CLOSED, 'Quit', 'Home'):
            win_town_meetings.close()
            win_town_meetings = None
            window3.un_hide()
        
    window1.close()
#===============================================================================


#===============================================================================
if __name__ == '__main__':
    main()
#===============================================================================