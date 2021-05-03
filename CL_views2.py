from datetime import time
import PySimpleGUI as sg

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
    
    for story in state_news:
        row = []
        chara_count = 0
        while chara_count < len(story['text']):
            cut_text = story['text'][chara_count: chara_count+80]
            # print('\nstory', story['text'], '\ncut_text', cut_text)
        
            row.append(
                [sg.Text(cut_text)]
            )
            chara_count += 80

        state_news_content.append([sg.Column(row)])
        state_news_content.append([sg.HorizontalSeparator()])
        

    layout = [
        layouts.create_top_banner(),
        layouts.create_heading(),
        [[sg.Text('Townships')], [sg.Button('Edison')]],
        [sg.Column(state_news_content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300))],
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

    return sg.Window('Get Involved NJ - Town Information', layout, size=(720, 540), finalize=True, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)



# def main():
#     # window variables
#     win_town = None
#     win_main = sg.Window([[sg.Text("HERERERER")]], finalize=True)


#     while True:             # Event Loop
#         # window, event, values = sg.read_all_windows(timeout=100) # read all events from all windows

#         window, event, values = sg.read_all_windows(timeout=100)
        
#         # if event in (sg.WIN_CLOSED, 'Exit', 'Quit'):
#         #     break
    

#         print(window, event, values)


#     win_main.close()


# main()

def main():
    # Design pattern 1 - First window does not remain active
    window2 = None
    window1 = make_main_window()

    while True:
        window, event, values = sg.read_all_windows()
        if event in (sg.WIN_CLOSED, 'Quit') and window == window1:
            break

        if window == window1:
            # window1['-OUTPUT-'].update(values['-IN-'])
            pass

        if event == 'Edison' and not window2:
            window1.hide()
            window2 = make_town_window()

        if window == window2 and (event in (sg.WIN_CLOSED, 'Exit', 'Home')):
            window2.close()
            window2 = None
            window1.un_hide()
    window1.close()


if __name__ == '__main__':
    main()