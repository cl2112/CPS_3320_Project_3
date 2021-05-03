
# PySimpleGUI for displaying the data
import PySimpleGUI as sg


import CL_scrape as scrape

# now display

Edison = scrape.get_data()

layout = []

menu_layout = [[sg.Text('HERE GOES THE MENU')]]

layout.append([sg.Frame('',menu_layout,background_color='#f3f3f3')])


# layout.append([sg.Text('HERE GOES THE MENU')])

for story in Edison.news:
    layout.append([sg.Text(story['text'])])

layout.append([sg.Text('HERE GOES THE FOOTER')])

window = sg.Window('Get Involved', layout)

event, values = window.read()

window.close()


# Program flow
