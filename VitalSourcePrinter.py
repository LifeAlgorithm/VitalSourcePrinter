
'''
This script is designed to legally and automatically print your purchased e-books from VitalSource.com

See ReadMe at https://github.com/LifeAlgorithm/VitalSourcePrinter and/or watch tutorial video for instructions
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

    numeral_map = tuple(zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
            ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I') ))

    def int_to_roman(i):
        result = []
        for integer, numeral in numeral_map:
            count = i // integer
            result.append(numeral * count)
            i -= integer * count
        return ''.join(result)

    def roman_to_int(n):
        i = result = 0
        for integer, numeral in numeral_map:
            while n[i:i + len(numeral)] == numeral:
                result += integer
                i += len(numeral)
        return result

    #Source of roman numeral coverters = http://code.activestate.com/recipes/81611-roman-numerals/

    print("Welcome to the VitalSource Ebook Printer. \n")

    while(True):
        try:
            RomanStart = input("Roman Numeral Start (or 'No'): ")
            if RomanStart == 'No' or RomanStart == 'no':
                print("")
                break
            elif roman_to_int(RomanStart.upper()):
                RomanEnd = input("Roman Numeral End (If one page enter same page as first): ").upper()
                if (roman_to_int(RomanStart.upper())) > (roman_to_int(RomanEnd.upper())):
                    print("\nFirst page must be less than last page.\n")
                    continue
                print("First roman numeral is ", int_to_roman(roman_to_int(RomanStart.upper())), " second is ", int_to_roman(roman_to_int(RomanEnd.upper())))
                proceed = input("Proceed? (Y/N): ")
                if proceed == 'Y' or proceed == 'y':
                    print("")
                    break
                else:
                    continue            
            else:
                print("Please enter valid roman numerals. Type 'No' to skip roman numerals.\n")          
        except:
            print("Please a valid roman numeral. Type 'No' to skip roman numerals.\n")

    if not (RomanStart == 'No' or RomanStart == 'no'):
        RomanList = []
        a = roman_to_int(RomanStart.upper())
        b = roman_to_int(RomanEnd.upper())

        for i in range(a,(b+1)):
            RomanList += [int_to_roman(i)]
        RomanBookList = [x.lower() for x in RomanList]

    while(True):
        try:
            NumberStart = int(input("First page: "))
            NumberEnd = int(input("Last page: "))
            if (type(NumberStart) != int) or (type(NumberStart) != int):
                print("Please enter valid numbers.\n")
                continue
            elif (NumberStart > NumberEnd):
                print("First page must be less than last page.\n")
                continue                    
            else:
                break          
        except:
            print("Please enter valid page numbers.\n")

    NumberList = []
    for i in range(int(NumberStart), int(NumberEnd)+1):
        NumberList += [ str(i) ]

    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.deiconify()
    root.lift()
    root.focus_force()
    # credits to http://stackoverflow.com/questions/3375227/how-to-give-tkinter-file-dialog-focus

    filedir = filedialog.askdirectory() + '/'

    if len(NumberList)%2 != 0 :
        NumberList += [ NumberList[-1] ]

    if not (RomanStart == 'No' or RomanStart == 'no'):
        if roman_to_int(RomanEnd.upper()):
            if len(RomanBookList)%2 != 0 :  #ugly coding, but it gets the job done
                RomanBookList += [ RomanBookList[-1] ]
                
    print("\nClick on the active VitalSource window to get started.\nThe program will start in: 8")
    for seconds in range(8):
        time.sleep(1)
        if seconds == 7:
            print("Starting now...\n")
            break
        print(str(8 - (seconds + 1))) 
                
    if not (RomanStart == 'No' or RomanStart == 'no'):  

        PageEntry1 = RomanBookList[0]
        PageEntry2 = RomanBookList[1]
                            
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

        print("Page: " + '1' + ' of ' + str(len(RomanBookList) ))
        for page in range(2, len(RomanBookList), 2):
                pyautogui.hotkey('ctrl', 'p')
                pyautogui.press('tab', 2, interval = 0.25)
                pyautogui.press('delete', 5, interval = 0.25)
                pyautogui.typewrite(RomanBookList[page], interval = 0.25)
                pyautogui.press('tab', interval = 0.25)
                pyautogui.press('delete', 5, interval = 0.25)
                pyautogui.typewrite(RomanBookList[page + 1], interval = 0.25)
                pyautogui.typewrite(['tab', 'tab', 'enter', 'enter'], interval = 0.5 )        
                pyautogui.typewrite("File2", interval = 0.25)
                pyautogui.press('enter', interval = 0.25)
                time.sleep(1.5)
                pdf1File = open(filedir + 'Ebook.pdf', 'rb')
                try:
                        pdf2File = open(filedir + 'File2.pdf', 'rb')
                except:
                        time.sleep(1)
                        pdf2File = open(filedir + 'File2.pdf', 'rb')
                pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
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
                os.remove(filedir + 'Ebook.pdf')
                os.remove(filedir + 'File2.pdf')
                os.rename(filedir + 'Ebook1.pdf', filedir + 'Ebook.pdf')
                print("Page: " + str(page + 2) + ' of ' + str(len(RomanBookList)))         
        print("\nRoman Numerals Done\n")

    else:
        PageEntry1 = NumberList[0]
        PageEntry2 = NumberList[1]
                            
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

    def NumberProcess(start):
        for page in range(start, len(NumberList), 2):
                pyautogui.hotkey('ctrl', 'p', interval = 0.25)
                pyautogui.press('tab', 2, interval = 0.25)
                pyautogui.press('delete', 5, interval = 0.25)
                pyautogui.typewrite(NumberList[page], interval = 0.25)
                pyautogui.press('tab', interval = 0.25)
                pyautogui.press('delete', 5, interval = 0.25)
                pyautogui.typewrite(NumberList[page + 1])
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
                pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
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
           
                print("Page: " + str(page + 2) + ' of ' + str(len(NumberList) ))           

    if not (RomanStart == 'No' or RomanStart == 'no'):
        NumberProcess(0)
    else:
        NumberProcess(2)
        
    elapsed_time = time.time() - start_time
    print("\nDone!")
    print("This took " + "%.2f" % (elapsed_time/3600) + " hours.")

if __name__ == "__main__": main()


''' Final note

I hope this script serves you well. A lot of the actual code was written for basic functionality and not neccessarily optimization.
Suggestions for refactoring and improvement are always appreciated.

'''
