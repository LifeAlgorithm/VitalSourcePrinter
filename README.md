# VitalSourcePrinter
Code to legally and automatically print your purchased e-books from VitalSource.com

This program automates the printing of PDF's from the VitalSource Bookshelf. The VitalSource Bookshelf only lets the user print 2 pages at a time, and manually doing this for the entire book is tedious and time consuming. This program automatically prints any selection or the entirety of an e-book, page by page, and rapidly concatenates everything into a single PDF file. As this program makes use of keyboard automation, this process assumes that the user is away from the computer for the duration of the process, though the user at any time can stop the script from continuing. 

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

Now you're ready to get started. In the case that you find the remainder of this tutorial visually hard to follow, be sure to check out the tutorial video.

First let's open up VitalSource Book Shelf. Double click on the ebook you want to print to get it to pop-out. Now that we have it in place, let's make a new folder for our printed ebook to be located. For a simple example, I will make a folder on my desktop called "Ebook"

The next part is very important. The script will not work unless two conditions are met. Firstly, you need to have a PDF printer that doesn't automatically open the newly printed PDF. For example, Adobe does this. You will need to disable this functionality if want the script to work. In the future, the script can be improved to account for this situation. One working PDF printer that comes with Windows is "Microsoft Print to PDF" and I reccommend using that if you are on Windows. I'm currently not too familiar with PDF printers for OS X and other systems and it would be appreciated if anyone can give an example of the analog for "Microsoft Print to PDF." Otherwise, any PDF printer that doesn't open new PDF's automatically, or one that can turn off this feature, will work.

The second condition is that a "sample pdf" needs to be printed at the location of your ebook folder. This needs to be done to ensure that all intermediary PDF files being printed from VitalSource Bookshelf are in that ebook folder so the script knows where to look for them. A strange analogy that may explain this situation: "all the customers need to stay inside the (in-door) restaurant or else there will be no business." All the intermediary files need to be in the folder or else the script will have nothing to concatenate. 
Ctrl + P and print a sample 2 page PDF to your ebook folder and that will set VitalSource to do its printing there.

Next download VitalSourcePrinter.py if you haven't already. This is the script we will be running to print our ebook. Open VitalSourcePrinter.py in your environment of choice. Python usually comes with a default environment called IDLE that can be used if you don't have an environment that supports Python. This can be easily performed by right clicking the .py file and clicking "edit with IDLE"

For viewing and operational purposes, it's a good idea to have the code view and the VitalSource ebook window close to each other. Once the script runs, it will automate keyboard actions so you need to be able to call focus to the VitalSource ebook window by clicking on it before the keyboard automations start. This will be touched upon soon.

Now run the script. Follow the prompt and input the desired page ranges for roman numerals and regular numbers. If no roman numerals are desired, input "None" or "none". Only valid numbers and roman numerals work. 

Side note: Typing names like "inside front cover" won't be recieved by the script, and hence if you would like pages with specific names to be included, you would need to manually print those out and separately concatenate them to the finished Ebook pdf. This could be another feature to be added in the future.

After the page ranges are entered, the program will prompt you to pick a folder. You must pick the ebook folder, or else the script won't function in accordance with VitalSource. I prefer not to come up with another terrible restaurant analogy to explain why but the main reason is because files won't be found properly. After picking the folder, a countdown of 8 seconds will begin before the printing automation starts. Click on the ebook window and the script will run. To stop the script at any time, mouse over to the console window where the script is running and close it. It will say "the program is still running, do you want to kill it?" Choose "yes". Once complete, you will see the message "done!" and the elapsed time in hours.

A 1270 page ebook takes around 3.5 hours to print. That's about 6 pages a minute. Not too bad, though not perfect. The lengthy time is due to the design of the code, which was informed by trial and error. There were situations where names and keyboard operations would skip or not perform correctly due to happening too fast for VitalSource BookShelf to process. Moreover, intermediary files generated by VitalSource BookShelf were not recognized by the system if there was no waiting time after their generation, so waiting time was introduced to catch this error. At the end of the day (pun intended), you can use this script to print any ebook you want while sleeping, or when you are away from your computer of course.

I hope this program is helpful and if any problems or issues arise, I encourage you to reach out to me and I will do my best to fix them. Any ideas, suggestions, or improvements would also be welcome.

~LifeAlgorithm
