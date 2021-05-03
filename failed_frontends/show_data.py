from tkinter import *
from tkinter import ttk

class News_Display:

    def __init__(self, root, data):
        root.title = 'News for ___'


        s= ttk.Scrollbar(root, orient=VERTICAL).grid(column=1)
        
        content_frame = ttk.Frame(root, padding='5', yscrollcommand=s.set)
        content_frame.grid(column=0, row=0, sticky=(N,S,E,W))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)


        ttk.Label(content_frame, text='News for ___', justify='left').grid(column=0)
        
        s.config(command=content_frame.yview)

        for item in data:
            print(item)
            ttk.Label(content_frame, text=item['text'], justify='left').grid(column=0)
            ttk.Label(content_frame, text=item['link'], justify='left').grid(column=0)
            ttk.Label(content_frame, text='  CHECK', justify='left').grid(column=0)


