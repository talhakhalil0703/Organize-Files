import shutil
import os
import re
import sys
from tkinter import *
from tkinter import filedialog

window =  Tk()
window.title('File Organization')

def find_file_directory(data_path, stringendswith):
    file_directory = []
    for root, dirs, files in os.walk(data_path):
        for file in files:
            if file.endswith(stringendswith):
                file_directory.append(os.path.join(root, file))

    file_directory.sort()
    return file_directory

def find_substring_all_occurences(stringtocheck, substring):
    indexes = []
    for index, letter in enumerate(stringtocheck):
        if letter == substring:
            indexes.append(index)
    return indexes

def movetofolder(datapath, substring, foldername):
    allfiles = find_file_directory(datapath, substring)
    for file in allfiles:

        newdestinationindex = max(find_substring_all_occurences(allfiles[0], '/'))
        if not os.path.exists(file[0:newdestinationindex] + '/' + foldername):
            os.makedirs(file[0:newdestinationindex] + '/' + foldername)
        newdest = file[0:newdestinationindex] + '/' + foldername + file[newdestinationindex:]
        shutil.move(file, newdest)

what_pathname = Entry(window, width = 40)
what_file_extensions = Entry(window, width = 40)
what_folder_move_to = Entry(window, width = 40)

def movefiles():
    pathname = what_pathname.get()
    extension = what_file_extensions.get()
    foldername = what_folder_move_to.get()
    movetofolder(pathname, extension, foldername)
    print('Done')

def exit_program():
    sys.exit(0)

def browse_clicked():
    window.filename = filedialog.askdirectory()
    what_pathname.delete(0, END)
    what_pathname.insert(END, window.filename)

what_pathname_label = Label(window, text = 'What is the pathname: ')
what_file_extensions_label = Label(window, text = 'What do the file extensions end with: ')
what_folder_move_to_label = Label(window, text = 'What is the name of the folder you want them to: ')

what_pathname_label.grid(column = 0, row = 0)
what_file_extensions_label.grid(column = 0, row = 1)
what_folder_move_to_label.grid(column = 0, row = 2)
what_pathname.grid(column = 1, row = 0)
what_file_extensions.grid(column = 1, row = 1)
what_folder_move_to.grid(column = 1, row = 2)

move_files_button = Button(window, text = 'Move Files', command = movefiles)
exit_button = Button(window, text = 'Exit', command = exit_program)
browse_button = Button(window, text = 'Browse', command = browse_clicked)

move_files_button.grid(column = 0, row = 3)
exit_button.grid(column = 1, row = 3)
browse_button.grid(column = 2, row = 0, padx = (20,20))

window.mainloop()
