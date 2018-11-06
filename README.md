# Text_Extraction
A python based image reading system which can store the location and count of each word appearing in the textutal image.Noise Reduction along with Binarization has also been done.

DEPENDENCIES:
    1)numpy
    2)PIL to open,save and transform image.
    3)pyplot from matplotlib for plotting image(noise reduced and binarized).This is optional.
    4)pytesseract for OCR working
    5)subprocess to create hocr file which could be then converted to DataFrame.
    6)lxml,etree for extracting position of text in the image.
    7)pandas :- to convert the parsed file pointer of hocr file to dataframe.

Steps to run the file:
    The code is written in python3 and to run the file  type the following command in terminal
        $python3 main.py
Output prints on the terminal.
