"""
This file contains the code to fix the windows
OSError when printing many lines on the console.

Colorama is used here, which is a module to allow
ANSI string filtering (for the carriage returns).

In addition win_unicode_console
"""

# os and sys for os detection and 
# writing/flushing lines to console.
import os, sys 
import colorama
import win_unicode_console

def init_writing():
    """
    Here we just call the function to init
    ANSI filtering. This HAS to be called 
    when using Windows, but Unix systems have
    this enabled automatically.
    """

    # This module is a quick workaround for Unicode 
    # varying byte length in windows. 
    win_unicode_console.enable()
    colorama.init(convert=True)

def update_line(text, chars=["\033[F","\r"]): 
    """
    This function will output text on
    the same line. I.e update the line
    with the new text using ANSII.

    Only use this for CLIs as info is printed to stdout, 
    so redirecting text outputs won't work, unless you
    manually change the sys.stdout pointer manually. 

    Args:
        text - The text to override current line with.
        chars - Carriage return characters. 
    """

    # Encode to ASCII (only for Windows)
    output = text.encode("utf-8").decode("ascii")

    # If windows is being used, flush explicitly or 
    # cmd won't output properly.
    if os.name == 'nt':
        # Print text and update cursor
        sys.stdout.write(output)
        sys.stdout.flush()

        sys.stdout.write(chars[1])
        sys.stdout.flush()	

    else:
        sys.stdout.write(text + "\n")
        sys.stdout.write(chars[0])

# Note that I wrote this code a couple of years ago when I 
# did some work on Python CLIs. If this didn't work, please
# contact me (Mat Gomes) and I will be happy to help.