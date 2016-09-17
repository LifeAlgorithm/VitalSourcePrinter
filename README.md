# VitalSourcePrinter
Code to legally and automatically print your purchased e-books from VitalSource.com

To get started you are going to need a working version of Python 3 because as of this time the only working script is written in Python 3.

If you're just installing Python 3 for the first time or reinstalling it, I highly recommend using Python 3.4.0 or higher as this version comes built with a feature called pip that easily allows you to install approved third party packages not included with Python by default. To find more information about pip, visit: https://pypi.python.org/pypi/pip 

Note: If you're on Linux or Ubuntu, pip doesn't come with 3.4.0 or higher. The part of this section involving pip is referenced from https://automatetheboringstuff.com, a book that is a large inspiration for this program and one that I would highly recommend to anyone learning python. To learn how to get pip on Ubuntu or Linux, visit https://automatetheboringstuff.com/appendixa/

You're also going to need the VitalSource Bookshelf software, which you can find at: https://support.vitalsource.com/hc/en-us/articles/201344733-Bookshelf-Download-Page

The next things you need are the following third party packages: 
- PyPDF2
- pyautogui

You of course must have Python 3 to install these packages. The easiest way to securely download and install these packages involves calling pip from your command prompt / terminal. If you don't have pip installed, you will have to manually download and insert these packages:
https://docs.python.org/3/install/

This guide will proceed using pip. Navigate to your terminal and type the following one line at a time:

Windows users

- pip install PyPDF2
- pip install pyautogui

OS X and Linux users:

- pip3 install PyPDF2
- pip3 install pyautogui

Now you're ready to get started.





