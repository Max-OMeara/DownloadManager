import PySimpleGUI as sg
import os
import shutil
from PIL import Image

# Function to resize and save the image
def resize_image(input_path, output_path, new_size):
    with Image.open(input_path) as img:
        img = img.resize(new_size)
        img.save(output_path)

# Function to organize downloads
def organize_downloads(download_folder):
    # Check if a folder was selected
    if download_folder:
        # Obtain all the files from the selected folder
        files = [f for f in os.listdir(download_folder) if os.path.isfile(os.path.join(download_folder, f))]

        # Create folders based on file type
        for file in files:
            filetype = file.split('.')[-1]
            new_folder_name = os.path.join(download_folder, filetype + '_folder')

            # Check if the folder exists or not
            if not os.path.exists(new_folder_name):
                os.mkdir(new_folder_name)

            # Move the file to the corresponding folder
            src_path = os.path.join(download_folder, file)
            dest_path = os.path.join(new_folder_name, file)
            shutil.move(src_path, dest_path)

        sg.popup("Downloads organized successfully!")


# Define the text for the steps
steps_text = (
    "Steps to Use:\n"
    "\n"
    "1. Click 'Select Downloads Folder' to choose the folder you want\n    to organize.\n"
    "\n"
    "2. The application will create subfolders based on file types in the\n    selected folder and organize your downloads.\n"
    "\n"
    "3. A success message will be displayed when the organization\n    is complete."
)


# Define the layout of the GUI
sg.theme("LightGrey2")  # Set the theme for a more professional look

# Resize the image and save it with a new name
resize_image('manager.png', 'small_manager.png', (300, 300))  # Change (100, 100) to your desired dimensions

layout = [
    [
        sg.Column(
            [
                [sg.Text("Downloads Organizer", font=("Helvetica", 20))],
                [sg.Button("Select Downloads Folder", size=(20, 1), key="-SELECT-FOLDER-")],
                [sg.Text("", size=(20, 1), key="-RESULT-", text_color="green")],
                [sg.Image(filename='small_manager.png', key='-IMAGE-')],  # Use the resized image
            ],
            vertical_alignment='top',
        ),
        sg.VSeperator(),
        sg.Column(
            [
                [sg.Text(steps_text, font=("Helvetica", 14))],
            ],
            vertical_alignment='top',
        ),
    ],
]

# Create the window
window = sg.Window("Downloads Organizer", layout, size=(800, 400))

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "-SELECT-FOLDER-":
        download_folder = sg.popup_get_folder("Select Downloads Folder", title="Downloads Organizer")
        if download_folder:
            window["-RESULT-"].update("Organizing downloads...")
            organize_downloads(download_folder)
            window["-RESULT-"].update("Downloads organized!")

# Close the window
window.close()
