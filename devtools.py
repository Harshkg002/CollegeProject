import os

def center_window(w,width,height):
    screen_width = w.winfo_screenwidth()
    screen_height=w.winfo_screenheight()
    x=(screen_width//2)-(width//2)
    y=(screen_height//2)-(height//2)
    w.geometry(f'{width}x{height}+{x}+{y}')


def find_file(filename):
    """
    Search for a file.
    Returns the complete file path if found, otherwise returns None.
    """
    script_directory = os.path.dirname(os.path.realpath(__file__))
    files_in_script_dir = os.listdir(script_directory) 

    if filename in files_in_script_dir:
        return os.path.join(script_directory, filename)
    else:
        return None
