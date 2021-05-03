# block_3 = [[sg.Text('Block 3', font='Any 20')],
#             [sg.Input(), sg.Text('Some Text')],
#             [sg.Button('Go'), sg.Button('Exit')]  ]


# block_2 = [[sg.Text('Block 2', font='Any 20')],
#             [sg.T('This is some random text')],
#             [sg.Image(data=sg.DEFAULT_BASE64_ICON)]  ]

# block_4 = [[sg.Text('Block 4', font='Any 20')],
#             [sg.T('This is some random text')],
#             [sg.T('This is some random text')],
#             [sg.T('This is some random text')],
#             [sg.T('This is some random text')]]


# layout = [[sg.Column(top_banner, size=(960, 60), pad=(0,0), background_color=DARK_HEADER_COLOR)],
#           [sg.Column(top, size=(920, 90), pad=BPAD_TOP)],
#           [sg.Column([[sg.Column(block_2, size=(450,150), pad=BPAD_LEFT_INSIDE)],
#                       [sg.Column(block_3, size=(450,150),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
#            sg.Column(block_4, size=(450, 320), pad=BPAD_RIGHT)]]


# layout = [
#     [sg.Column(top_banner, expand_x=True, background_color=DARK_HEADER_COLOR)],
#     [sg.Column(heading, expand_x=True)],
#     [sg.Column(content, expand_y=True, expand_x=True)],
#     [sg.Column(footer, expand_x=True)]
# ]

# def create_town_window():
#     town_content = [
#         [sg.Text('Town News')]
#     ]
    
#     layout = [
#         [sg.Column(top_banner, expand_x=True, background_color=DARK_HEADER_COLOR)],
#         [sg.Column(heading, expand_x=True)],
#         [sg.Column(town_content, expand_y=True, expand_x=True)],
#         [sg.Column(footer, expand_x=True)]
#     ]

#     return sg.Window('Get Involved NJ - Edison', layout, size=(720, 540), margins=(0,0), background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)

# window = sg.Window('Get Involved NJ', layout, size=(720, 540), margins=(0,0), background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=False)



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# content = [
    #     [
    #         sg.Column([[sg.Text('Townships')], [sg.Button('Edison')]], expand_y=True, expand_x=True),
    #         sg.Column(state_news_content, expand_x=True, scrollable=True, vertical_scroll_only=True)
    #     ]
    # ]
    
    # layout = [
    #     layouts.create_top_banner(),
    #     layouts.create_heading(),
    #     [
    #         sg.Column(state_news_content, expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True, vertical_alignment='top', size=(540, 300)), 
    #         sg.Column([[sg.Text('Townships')], [sg.Button('Edison')]], expand_y=True, expand_x=True)
    #     ],
    #     layouts.create_footer()
    # ]


