# syahirachna_ocr
Tkinter and Python based OCR GUI test bed.

With this program you can test your various text image enhancement modules by slightly modifying codes in main_ocr.py files.

Currently this module is using Tesseract OCR. But I will try to make my own OCR for recognition.
The program works with image as well as pdf files.

To run the software run the 'syahirachna_ocr.py'

Dependencies are given in requirements.txt. For installation of these run <' pip install -r requirements.txt '>

For installing the requirements in virtual environment you can refer to following webpage:
  https://www.dev2qa.com/how-to-install-python-packages-using-requirements-text-file/

How to run :
1. Open the image or PDF.
2. Select language.
3. Select Font.
4. Select Mode.

  a. Uniform Mode : Assume a single uniform block of text.
  
  b. Regular mode : Automatic page segmentation
  
 (Note : It is necessary to select all the options before running the program)
 
5. Press convert, if you want to run OCR on one image shown in the left pane or Press Convert All, to apply OCR on all images.

In future I will be trying to create a library of this code so that it would be more easier to integrate your codes but for now try working on this and give suggestions to improve it.
