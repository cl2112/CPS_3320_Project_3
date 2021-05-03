from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title('Get Involved')
root.geometry('480x360')

content_frame = Frame(root, padding='5')
content_frame.grid(column=0, row=0, sticky=(N, S, E, W))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = Entry(content_frame, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(N,S,E,W))

# button = Button(content_frame, text ="Check!", command=root.destroy)
# button.grid()

Label(content_frame, text='middle middle').grid()

root.mainloop()