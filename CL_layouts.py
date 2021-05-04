#===============================================================================
# Author: Christian Liguori
# Date: 05/04/21
# Program Name: CL_layouts.py
# This file contains all of the functions to create the layouts that are used to 
#   create the windows of the GUI, except for the layouts used only in
#   one window. 
#===============================================================================


#===============================================================================
# Library Imports
#===============================================================================
# The PySimpleGUI library used to render GUIs
from tkinter import font
import PySimpleGUI as sg
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
# Layout Functions
#===============================================================================
# Functions to create and return new layout elements.
# This is to support creating multiple windows, because with PySimpleGUI, once
#   a layout is used in a window, it cannot be used in another window. To deal
#   with this limitation, a new layout with new elements is created for 
#   every window.
#===============================================================================

# Function to create the top banner of the UI. It is like the main menu of the
#   app.
def create_top_banner():
    # The top banner is made up of two columns, one with the text of the 
    #   app and the other holds the buttons for the different options. Then,
    #   both of those columns are joined inside of another column that 
    #   makes up the top row of the GUI.
    top_banner = [
        [
            sg.Column([
                [sg.Text(
                    'Get Involved NJ', 
                    font='Any 20', 
                    background_color=DARK_HEADER_COLOR, 
                    enable_events=True)]
            ],expand_x=True, background_color=DARK_HEADER_COLOR),
            
            sg.Column([
                [sg.Button('Home'), 
                sg.Button('Quit')]
            ], background_color=DARK_HEADER_COLOR)
        ]
    ]

    return [
        sg.Column(
            top_banner, 
            expand_x=True, 
            background_color=DARK_HEADER_COLOR
        )
    ]
#===============================================================================


#===============================================================================
# Function to create the heading for the GUI. The heading contains the 
#   window specific options.
def create_heading():
    heading = [
        [sg.Text('Welcome to the Get Involved NJ App.')],
        [sg.Text('Select a town to get started.')]
    ]

    return [sg.Column(heading, expand_x=True)]
#===============================================================================


#===============================================================================
# Function to create the heading for the township window. The heading contains 
#   the window specific options.
def create_township_heading(township_name):
    heading = [
        [
            sg.Column([
                [sg.Text(township_name, font='Any 20')]
            ], expand_x=True),

            sg.Column([
                [sg.Button('News'), 
                sg.Button('Dept. Info'), 
                sg.Button('Town Meeting Info')]
            ])
        ]
    ]

    return [sg.Column(heading, expand_x=True)]
#===============================================================================


#===============================================================================
# Function to create the footer for the UI. It contains some information on
#   the creation of the app.
def create_footer():
    footer = [
        [sg.Text(
            'Created by Christian Liguori for CPS 3320' + 
            ' @ Kean University - 05/05/21'
        ,background_color=DARK_HEADER_COLOR, font='Any 10')]
    ]

    return [sg.Column(footer, expand_x=True, element_justification='c', 
    background_color=DARK_HEADER_COLOR)]
#===============================================================================