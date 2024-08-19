# Download Manager

## Project Overview

The Download Manager is a Python application designed to help users organize their downloaded files by categorizing them into subfolders based on file types. This tool features a simple graphical user interface (GUI) created with PySimpleGUI, allowing users to easily select a folder and automatically organize its contents. 

## Purpose

This project was created as a learning exercise to improve my Python skills and to manage the space on my computer. By automating the process of organizing downloaded files, I aimed to reduce clutter and enhance the overall organization of my system’s storage.

## Features

- **Automatic File Organization**: The application scans the selected download folder and creates subfolders for different file types, moving files into their corresponding folders.
- **Simple and Intuitive GUI**: The user interface, built with PySimpleGUI, is easy to navigate and use, making file organization a quick and hassle-free task.
- **Image Resizing**: The application includes a function to resize images, ensuring that any graphics used in the GUI are appropriately scaled.

## Technologies Used

- **Python**: The core programming language used to develop the application.
- **PySimpleGUI**: A Python library used to create the graphical user interface.
- **PIL (Pillow)**: A Python Imaging Library used for image processing tasks like resizing.
- **os and shutil**: Standard Python libraries used for file handling and manipulation.

## File Structure

- **manager.py**: The main script that contains the code for the Download Manager application.
- **manager.png**: An image used in the GUI.
- **small_manager.png**: A resized version of `manager.png` for use in the application.
- **broom.ico**: An icon for the application window.

## Installation

To run this project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/download-manager.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd download-manager
   ```

3. **Install dependencies**:
   Make sure you have Python installed, then install the required libraries using pip:
   ```bash
   pip install pysimplegui pillow
   ```

4. **Run the application**:
   ```bash
   python manager.py
   ```

## How to Use

1. **Select Downloads Folder**: Click the "Select Downloads Folder" button to choose the folder you want to organize.
2. **Automatic Organization**: The application will create subfolders based on file types in the selected folder and organize your downloads.
3. **Completion Message**: A success message will be displayed when the organization is complete.

## Contributing

Contributions to this project are welcome! If you have ideas for new features or improvements, feel free to fork the repository, make your changes, and submit a pull request.

## Future Plans

- **Customizable Folder Names**: Allow users to customize the names of the subfolders created for each file type.
- **Advanced Sorting Options**: Implement additional sorting criteria, such as file size, date, or custom tags.
- **Enhanced User Interface**: Improve the GUI with more options and feedback during the organization process.

## License

This project is open-source and available to use, modify, and distribute it as needed.

## Acknowledgments

This project was created to help me practice Python programming and to manage the storage space on my computer. It has been a valuable learning experience, and I hope it can be useful to others as well.

---

Feel free to adapt the README according to any additional details or changes in your project.
