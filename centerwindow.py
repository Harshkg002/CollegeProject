def center_window(w,width,height):
    screen_width = w.winfo_screenwidth()
    screen_height=w.winfo_screenheight()
    x=(screen_width//2)-(width//2)
    y=(screen_height//2)-(height//2)
    w.geometry(f'{width}x{height}+{x}+{y}')