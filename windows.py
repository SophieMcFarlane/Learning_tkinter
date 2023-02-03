def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcesssDpiAwareness(1)
    except:
        pass