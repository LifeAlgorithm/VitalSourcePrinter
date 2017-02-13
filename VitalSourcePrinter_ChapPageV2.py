'''
This script is designed to legally and automatically print your purchased e-books from VitalSource.com

See ReadMe at https://github.com/LifeAlgorithm/VitalSourcePrinter and/or watch tutorial video for instructions

This version is for printing chapter pages with the Ctrl + pagedown requirement
'''

try:   
    import PyPDF2
    import pyautogui
    import os
    import sys
    import time
    import warnings
    from tkinter import *
    import tkinter.filedialog as filedialog
except:
    print("Please install PyPDF2 and pyautogui. Refer to video or documentation for help")
    sys.exit()


def main():

    start_time = time.time() 
    warnings.filterwarnings("ignore") #Gets rid of harmless warnings on the console for excess whitespace


    print("Welcome to the VitalSource Ebook Printer!\nThis version is for chapter pages of the form 'Chapter-Page'\n")

    chapCount = int(input("Enter chapter count: "))
    chapList = list(range(1, chapCount+1))
    printList = list()
    for chapIndex in range(1, chapCount+1):
        chapPageList = int(input("Pages in chapter " + str(chapIndex) + ": "))
        for chapPageIndex in range(1, chapPageList + 1):
            printList.append(str(chapIndex) + "-" + str(chapPageIndex))
        

    #print (printList)
                             
    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.deiconify()
    root.lift()
    root.focus_force()
    # credits to http://stackoverflow.com/questions/3375227/how-to-give-tkinter-file-dialog-focus

    filedir = filedialog.askdirectory() + '//'

    if len(printList)%2 != 0 : #ensures an even amount of print entries
        printList += [ printList[-1] ]

    tempHyIndex = printList[0].find("-")
    currentChapter = printList[0][0:tempHyIndex] #first chapter]            
                             
    print("\nClick on the active VitalSource window to get started.\nThe program will start in: 8")
    for seconds in range(8):
        time.sleep(1)
        if seconds == 7:
            print("Starting now...\n")
            break
        print(str(8 - (seconds + 1))) 
                  
    PageEntry1 = printList[0]
    PageEntry2 = printList[1]
                                             
    pyautogui.hotkey('ctrl', 'p')
    pyautogui.press(keys = 'tab', presses = 2, interval = 0.25)
    pyautogui.press('delete', 5)
    pyautogui.typewrite(PageEntry1)
    pyautogui.press('tab')
    pyautogui.press('delete', 5)
    pyautogui.typewrite(PageEntry2)
    pyautogui.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.25 )
    pyautogui.typewrite("Ebook", interval = 0.50)
    pyautogui.press('enter', interval = 0.5)
    time.sleep(0.25)

    
    for page in range(2, len(printList), 2):
                    
                    tempHyIndex = printList[page].find("-")
                    tempChapter = printList[page][0:tempHyIndex]
                    if currentChapter != tempChapter:
                      currentChapter = tempChapter
                      pyautogui.hotkey('ctrl', 'pagedown', interval = 0.25)
                             
                    pyautogui.hotkey('ctrl', 'p', interval = 0.25)
                    pyautogui.press('tab', 2, interval = 0.25)
                    pyautogui.press('delete', 5, interval = 0.25)
                    pyautogui.typewrite(printList[page], interval = 0.25)
                    pyautogui.press('tab', interval = 0.25)
                    pyautogui.press('delete', 5, interval = 0.25)
                    pyautogui.typewrite(printList[page + 1])
                    pyautogui.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.75)
                    pyautogui.typewrite("File2", interval = 0.5)
                    pyautogui.press('enter', interval = 0.5)
                    time.sleep(5)
                    while (os.path.isfile(filedir + "Ebook.pdf") != True):
                               time.sleep(2)
                    while (os.path.isfile(filedir + "File2.pdf") != True):
                               time.sleep(2) 
                    try:
                            pdf1File = open(filedir + 'Ebook.pdf', 'rb')
                            pdf2File = open(filedir + 'File2.pdf', 'rb')
                    except:
                            while (os.path.isfile(filedir + Ebook.pdf) != True):
                               time.sleep(10)
                            while (os.path.isfile(filedir + File2.pdf) != True):
                               time.sleep(10) 
                    try: 
                            pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
                    except:
                            time.sleep(5)
                            pdf1Reader = PyPDF2.PdfFileReader(pdf1File)

                    try:
                            pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
                    except:
                            time.sleep(5)
                            pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
                    
                    pdfWriter = PyPDF2.PdfFileWriter()   
                    for pageNum in range(pdf1Reader.numPages):
                            pageObj = pdf1Reader.getPage(pageNum)
                            pdfWriter.addPage(pageObj)
                    for pageNum in range(pdf2Reader.numPages):
                            pageObj = pdf2Reader.getPage(pageNum)
                            pdfWriter.addPage(pageObj)
                    pdfOutputFile = open(filedir + 'Ebook1.pdf', 'wb')
                    pdfWriter.write(pdfOutputFile)
                    pdfOutputFile.close()
                    pdf1File.close()
                    pdf2File.close()
                    try:
                            os.remove(filedir + 'Ebook.pdf')
                    except:
                            time.sleep(10)
                            os.remove(filedir + 'Ebook.pdf')
                            
                    try:
                            os.remove(filedir + 'File2.pdf')
                    except:
                            time.sleep(10)
                            os.remove(filedir + 'File2.pdf')

                    try:
                            os.rename(filedir + 'Ebook1.pdf', filedir + 'Ebook.pdf')
                    except:
                            time.sleep(10)
                            os.rename(filedir + 'Ebook1.pdf', filedir + 'Ebook.pdf')
       
                    print("Page: " + str(page + 2) + ' of ' + str(len(printList) ))           



    elapsed_time = time.time() - start_time
    print("\nDone!")
    print("This took " + "%.2f" % (elapsed_time/3600) + " hours.")

if __name__ == "__main__": main()

