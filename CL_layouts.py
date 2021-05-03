from tkinter import font
from tkinter.constants import CENTER
import PySimpleGUI as sg

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))

# ------------------------------------------------------------------------------
# Functions to create and return new layout elements.
# ------------------------------------------------------------------------------
# This is to support creating multiple windows, because with PySimpleGUI, once
#   a layout is used in a window, it cannot be used in another window. To deal
#   with this limitation, a new layout is created for every window.
# ------------------------------------------------------------------------------
def create_top_banner():
    top_banner = [
        [
            sg.Column([[sg.Text('Get Involved NJ', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True)]],expand_x=True, background_color=DARK_HEADER_COLOR),
            sg.Column([[sg.Button('Home'), sg.Button('Quit')]], background_color=DARK_HEADER_COLOR)
        ]
    ]

    return [sg.Column(top_banner, expand_x=True, background_color=DARK_HEADER_COLOR)]

def create_heading():
    heading = [
        [sg.Text('Welcome to the Get Involved NJ App.')],
        [sg.Text('Select a town to get started.')]
    ]

    return [sg.Column(heading, expand_x=True)]

def create_township_heading(township):
    heading = [
        [
            sg.Column([[sg.Text(township.name, font='Any 20')]], expand_x=True),
            sg.Column([[sg.Button('News'), sg.Button('Dept. Info'), sg.Button('Town Meeting Info')]])
        ]
    ]

    return [sg.Column(heading, expand_x=True)]

def create_footer():
    footer = [
        [sg.Text('Created by Christian Liguori for CPS 3320 @ Kean University    05/05/21')]
    ]

    return [sg.Column(footer, expand_x=True, element_justification='c')]