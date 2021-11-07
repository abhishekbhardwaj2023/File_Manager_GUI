from tkinter import *
import shutil
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


# open a file box window
def open_window():
    read = easygui.fileopenbox()
    return read


# open file function
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")


# copy file function
def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied !")


# delete file function
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)
    else:
        mb.showinfo('confirmation', "File not found !")


# rename file function
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension = os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName = input()
    path = os.path.join(path1, newName + extension)
    print(path)
    os.rename(chosenFile, path)
    mb.showinfo('confirmation', "File Renamed !")


# move file function
def move_file():
    source = open_window()
    destination = filedialog.askdirectory()
    if (source == destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)
        mb.showinfo('confirmation', "File Moved !")


# function to make a new folder
def make_folder():
    new_folder_path = filedialog.askdirectory()
    print("Enter name of new folder")

    new_folder = input()
    path = os.path.join(new_folder_path, new_folder)

    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")


# function to remove a folder
def remove_folder():
    del_folder = filedialog.askdirectory()
    os.rmdir(del_folder)
    mb.showinfo('confirmation', "Folder Deleted !")


# function to list all the files in folder
def list_files():
    folder_list = filedialog.askdirectory()
    sort_list = sorted(os.listdir(folder_list))
    i = 0
    print("Files in ", folder_list, "folder are:")
    while i < len(sort_list):
        print(sort_list[i] + '\n')
        i += 1


root = Tk()
root.configure(bg= 'black')


# label
Label(root, text="Python GUI File Manager", font=("Helvetica", 16), fg="red", bg='black').grid(row=0, column=1)
Label(root, text="By Abhishek Bhardwaj", font=("Helvetica", 8), fg="#000fff000", bg='black').grid(row=1, column=1, columnspan=2)

# Buttons
Button(root, text="Open a File", command=open_file, width=30, bg='#000fff000').grid(row=3, column=0)
Button(root, text="Copy a File", command=copy_file, width=30, bg='magenta').grid(row=4, column=0)
Button(root, text="Delete a File", command=delete_file, width=30, bg='red').grid(row=5, column=2)
Button(root, text="Rename a File", command=rename_file, width=30, bg='cyan').grid(row=3, column=2)
Button(root, text="Move a File", command=move_file, width=30, bg='yellow').grid(row=4, column=2)
Button(root, text="Make a Folder", command=make_folder, width=60, bg='yellow').grid(row=2, column=0, columnspan=3)
Button(root, text="Remove a Folder", command=remove_folder, width=30, bg='red').grid(row=5, column=0)
Button(root, text="List all Files in Directory", command=list_files, width=60, bg='blue').grid(row=6, column=0, columnspan=3)

root.mainloop()
