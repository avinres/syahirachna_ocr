############################Imports########################################################
import os
import sys
from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, IntVar, \
    StringVar, BooleanVar, Button, END, Label, INSERT, Canvas, OptionMenu
import tkinter.filedialog
import tkinter.messagebox
from PIL import ImageTk as itk
from PIL import Image
import clean_im as ci
import skew_correct as sc
import sim_ocr as socr
from zoom import *
import cv2
import pdf2image
import numpy as np
############################################################################################

"""psm doc string
      "Page segmentation modes:\n"
        "  0    Orientation and script detection (OSD) only.\n"
        "  1    Automatic page segmentation with OSD.\n"
        "  2    Automatic page segmentation, but no OSD, or OCR.\n"
        "  3    Fully automatic page segmentation, but no OSD. (Default)\n"
        "  4    Assume a single column of text of variable sizes.\n"
        "  5    Assume a single uniform block of vertically aligned text.\n"
        "  6    Assume a single uniform block of text.\n"
        "  7    Treat the image as a single text line.\n"
        "  8    Treat the image as a single word.\n"
        "  9    Treat the image as a single word in a circle.\n"
        " 10    Treat the image as a single character.\n"

        //TODO: Consider publishing these modes.
        #if 0
        " 11    Sparse text. Find as much text as possible in no"
          " particular order.\n"
        " 12    Sparse text with OSD.\n"
        " 13    Raw line. Treat the image as a single text line,\n """

class syahirachna_ocr():

    def __init__(self):
        self.root = Tk()
        #root.iconbitmap("myIcon.ico")
        self.height_ = self.root.winfo_screenheight() 
        self.width_ = self.root.winfo_screenwidth()   
        self.h_ = self.height_-75
        #print("\n width x height = %d x %d (in pixels)\n" %(self.width_, self.height_))
        self.root.geometry(str(self.width_)+'x'+str(self.height_))
        self.PROGRAM_NAME = "Syahirachna OCR"
        self.root.title(self.PROGRAM_NAME)
        ######################################################################
        self.open_file_icon = PhotoImage(file='icons/open_file.gif')
        self.save_file_icon = PhotoImage(file='icons/save.gif')
        self.copy_icon = PhotoImage(file='icons/copy.gif')
        self.input_file_name = []
        self.input_images = []
        self.ispdf = 0
        self.im_count = 0
        self.img_ocr = ""
        self.font_val = ""
        self.file_name = ""
        self.lan_val = ""
        self.main()
        self.root.config(menu=self.menu_bar)
        self.root.mainloop()

    ###############################################################################
        #shortcut bar specs
    # background = "background.png"
    # photo = itk.PhotoImage(file = background)
    #global height_
    #global width_
    #global im_count
    #global input_file_name

    #global font_val
    #global lan_val


    def readme_file_open(self):
        os.startfile('presentation.pdf')

    def show_text(self,text,font_val):
        font = font_val
        if font == 'Shiva-Medium':
            self.content_text.configure(font=("Shiva", 14))
        elif font == 'Kruti-Dev':
            self.content_text.configure(font=("Kruti Dev 010", 14))
        elif font == 'Walkman-Chanakya':
            self.content_text.configure(font=("Walkman-Chanakya-901", 14))
        elif (font == 'Unicode'):
            self.content_text.configure(font=("Mangal", 14))
        elif (font == 'English'):
            self.content_text.configure(font=("Times New Roman", 14))
        #text = text.encode('utf8')

        self.content_text.delete(1.0, END)
        self.content_text.insert(1.0, text)

    def OCR(self,all_im):
        deskew_im = sc.deskew(self.img_ocr) # deskew process
        if all_im != True:
            self.im_label.process_image(img = deskew_im, is_path=False) #display deskew image
        text = socr.text_out(deskew_im, self.lan_val, self.font_val, psm = self.psm_val)
        return text

    def OCR_command(self): #OCR command is function to execute ocr in the asked manner
        #self.img_ocr_loc = self.input_file_name[im_count] 
        #self.img_ocr = cv2.imread(self.img_ocr) #read image
        text = self.OCR(all_im = False)
        self.show_text(text,self.font_val)

    def OCR_command_all(self): #OCR command all is function to execute ocr on all images
        if self.ispdf == 1:
            a = len(self.input_images)
            complete_text = ""
            for x in range (a):
                #img = self.input_file_name[x]
                text = self.OCR(all_im = True)
                complete_text = complete_text + "\n" + str(x+1)+ "\n" + text
                self.next_im()
            self.show_text(complete_text,self.font_val)
        elif self.ispdf == 0:
            a = len(self.input_file_name)
            complete_text = ""
            for x in range (a):
                #img = self.input_file_name[x]
                text = self.OCR(all_im = True)
                complete_text = complete_text + "\n" + str(x+1)+ "\n" + text
                self.next_im()
            self.show_text(complete_text,self.font_val)


    # def OCR_command(self, all_im=False): #OCR command is function to execute ocr in the asked manner
    #     print(len(self.input_file_name), "ocr_command_fn")
    #     if len(self.input_file_name) != 0:
    #         if all_im:
    #             a = len(self.input_file_name)
    #             complete_text = ""
    #             for x in range (a):
    #                 #img = self.input_file_name[x]
    #                 text = self.OCR(x)
    #                 complete_text = complete_text + "\n" + str(x)+ "\n" + txt
    #             self.show_text(complete_text,self.font_val)
    #         else:
    #             text = self.OCR(self.im_count)
    #             self.show_text(text,self.font_val)
    #     else:
    #         print("kuch nahi hai")

    def find_font(self,*args):
        #global font_val
        self.font_val = self.fontvar.get()

    def find_psm(self,*args):
        #global font_val
        self.psm_val = self.psmvar.get()

    def find_lan(self,*args):
        #global lan_val
        self.lan_val = self.lanvar.get()

    # def put_into_im_label(self,img):
    #     img_ = itk.PhotoImage(img.convert('RGBA'))
    #     self.im_label.process_image(img_)
    #     self.im_label.image = img_

    # def display_image(self,img_loc):
    #     fname = os.path.basename(self.input_file_name[self.im_count])
    #     self.label_text2.configure(text = str(fname)) #displaying the name of the image
    #     img_ = img_loc
    #     im_label_height = int(self.height_-50)
    #     im_label_width = int(self.width_*0.45)
    #     offset = 100
    #     im_width, im_height = img_.size
    #     r_width = float(im_width/(im_label_width))
    #     r_height = float(im_height/(im_label_height))
    #     #print(r_width,r_height)
    #     if (r_width < 1) & (r_height < 1):
    #         #print(img_)
    #         #img_ = img_.convert('RGBA')
    #         self.put_into_im_label(img_)
    #     elif (r_width < r_height):
    #         #print("width < height")
    #         new_height = int(im_height/r_height)-offset
    #         new_width = int(im_width/r_height)-offset
    #         #print(new_height,new_width)
    #         img_new = img_.resize((new_width,new_height))
    #         #img_new = img_new.convert('RGBA')
    #         #print(img_)
    #         #print(img_new)
    #         self.put_into_im_label(img_new)
    #     elif (r_width > r_height):
    #         #print("width > height")
    #         new_height = int((im_height)/r_width)-offset
    #         new_width = int((im_width)/r_width)-offset
    #         img_new = img_.resize((new_width,new_height))
    #         #print(img_)
    #         #print(img_new)
    #         #img_new = img_new.convert('RGBA')
    #         self.put_into_im_label(img_new)
    #     #img_dis = img_.convert('RGBA')


    # def display_image_from_loc(self,img_loc):
    #     fname = os.path.basename(self.input_file_name[self.im_count])
    #     self.label_text2.configure(text = str(fname)) #displaying the name of the image
    #     img_ = Image.open(img_loc)
    #     im_label_height = int(self.height_-50)
    #     im_label_width = int(self.width_*0.45)
    #     offset = 100
    #     im_width, im_height = img_.size
    #     r_width = float(im_width/(im_label_width))
    #     r_height = float(im_height/(im_label_height))
    #     #print(r_width,r_height)
    #     if (r_width < 1) & (r_height < 1):
    #         #print(img_)
    #         #img_ = img_.convert('RGBA')
    #         self.put_into_im_label(img_)
    #     elif (r_width < r_height):
    #         #print("width < height")
    #         new_height = int(im_height/r_height)-offset
    #         new_width = int(im_width/r_height)-offset
    #         #print(new_height,new_width)
    #         img_new = img_.resize((new_width,new_height))
    #         #img_new = img_new.convert('RGBA')
    #         #print(img_)
    #         #print(img_new)
    #         self.put_into_im_label(img_new)
    #     elif (r_width > r_height):
    #         #print("width > height")
    #         new_height = int((im_height)/r_width)-offset
    #         new_width = int((im_width)/r_width)-offset
    #         img_new = img_.resize((new_width,new_height))
    #         #print(img_)
    #         #print(img_new)
    #         #img_new = img_new.convert('RGBA')
    #         self.put_into_im_label(img_new)
    #     #img_dis = img_.convert('RGBA')


    def open_file(self):
        #print(self.im_count)
        if len(self.input_file_name) != 0:
            input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".jpg",
                                         filetypes=[("All Files", "*.*"), ("JPEG", "*.jpg"), ("JPEG", "*.jpeg"), ("PNG", "*.png"), ("TIFF", "*.tiff")], multiple=True)
            num_file_sel = len(input_file_name)
            if num_file_sel != 0 :
                self.ispdf = 0
                self.input_file_name = input_file_name
                self.im_count = 0    
                text_label1 = "Page : "+str(self.im_count+1)+'/'+str(num_file_sel)
                self.label_text1.configure(text = text_label1)
                first_im = self.input_file_name[0]
                self.img_ocr = cv2.imread(first_im)
                self.im_label.process_image(img=self.img_ocr,is_path=False)
                fname = os.path.basename(first_im)
                self.label_text2.configure(text = str(fname))
                #self.display_image_from_loc(first_im)
        else:
            self.im_count = 0
            self.input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".jpg",
                                         filetypes=[("All Files", "*.*"), ("JPEG", "*.jpg"), ("JPEG", "*.jpeg"), ("PNG", "*.png"), ("TIFF", "*.tiff")], multiple=True)
            num_file_sel = len(self.input_file_name)
            if num_file_sel != 0 :
                self.ispdf = 0
                text_label1 = "Page : "+str(self.im_count+1)+'/'+str(num_file_sel)
                self.label_text1.configure(text = text_label1)
                first_im = self.input_file_name[0]
                self.img_ocr = cv2.imread(first_im)
                self.im_label.process_image(img=self.img_ocr,is_path=False)
                fname = os.path.basename(first_im)
                self.label_text2.configure(text = str(fname))
                #self.display_image_from_loc(first_im)
    def pdftoim(self, pdf_path):
        images = pdf2image.convert_from_path(pdf_path, dpi=600, fmt='ppm', poppler_path='./system/poppler/bin')
        no_im = len(images)
        #print("number of im =", no_im)
        for i in range(no_im):
            open_cv_image = np.array(images[i]) 
            # Convert RGB to BGR 
            images[i] = open_cv_image[:, :, ::-1].copy() 
        return images

    def open_pdf_file(self):
        #print(self.im_count)
        # print("I am here in open_pdf_file")
        if len(self.input_images) != 0:
            # print("I am here in open_pdf_file if condition active")
            input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".pdf",
                                         filetypes=[("PDF", "*.pdf")], multiple=False)
            if input_file_name != None :
                self.ispdf = 1 #flag for pdf operations
                self.input_file_name = input_file_name
                self.input_images = self.pdftoim(input_file_name) #recovering images
                num_file_sel = len(self.input_images)
                text_label1 = "Page : " + str(self.im_count+1)+'/'+str(num_file_sel)
                self.label_text1.configure(text = text_label1)
                first_im = self.input_images[0]
                self.img_ocr = first_im
                self.im_label.process_image(img=self.img_ocr,is_path=False)
                fname = os.path.basename(input_file_name)
                self.label_text2.configure(text = str(fname))
                #self.display_image_from_loc(first_im)
        else:
            self.im_count = 0
            self.input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".pdf",
                                         filetypes=[("PDF", "*.pdf")], multiple=False)
            # print(self.input_file_name)
            # print(len(self.input_file_name))
            if self.input_file_name != None :
                self.ispdf = 1 #flag for pdf operations
                self.input_images = self.pdftoim(self.input_file_name) #recovering images
                num_file_sel = len(self.input_images)
                text_label1 = "Page : " + str(self.im_count+1)+'/'+str(num_file_sel)
                self.label_text1.configure(text = text_label1)
                first_im = self.input_images[0]
                self.img_ocr = first_im
                self.im_label.process_image(img=self.img_ocr,is_path=False)
                fname = os.path.basename(self.input_file_name)
                self.label_text2.configure(text = str(fname))

    def next_im(self,event=None):
        #global im_count
        if self.ispdf == 1:
            a = len(self.input_images)
            if self.im_count == a-1:
                self.im_count = 0
            else:
                self.im_count = self.im_count+1
            #print(im_count)
            text_label1 = "Page : "+str(self.im_count+1)+'/'+str(a)
            self.label_text1.configure(text = text_label1)
            self.label_text2.configure(text = str(os.path.basename(self.input_file_name)))
            self.img_ocr = self.input_images[self.im_count]
            self.im_label.process_image(img=self.img_ocr,is_path=False)
        elif self.ispdf == 0:
            if self.input_file_name :
                a = len(self.input_file_name)
                if self.im_count == a-1:
                    self.im_count = 0
                else:
                    self.im_count = self.im_count+1
                #print(im_count)
                text_label1 = "Page : "+str(self.im_count+1)+'/'+str(a)
                self.label_text1.configure(text = text_label1)
                self.label_text2.configure(text = str(os.path.basename(self.input_file_name[self.im_count])))
                self.img_ocr = cv2.imread(self.input_file_name[self.im_count])
                self.im_label.process_image(img=self.img_ocr,is_path=False)
                #self.display_image_from_loc(self.input_file_name[self.im_count])

    def prev_im(self,event=None):
        if self.ispdf == 1:
            a = len(self.input_images)
            if self.im_count == 0:
                self.im_count = a-1
            else :
                self.im_count = self.im_count-1
            #print(im_count)
            text_label1 = "Page : " + str(self.im_count+1)+'/'+str(a)
            self.label_text1.configure(text = text_label1)
            self.label_text2.configure(text = str(os.path.basename(self.input_file_name)))
            self.img_ocr = self.input_images[self.im_count]
            self.im_label.process_image(img=self.img_ocr,is_path=False)
        elif self.ispdf == 0:
            if self.input_file_name :
                a = len(self.input_file_name)
                if self.im_count == 0:
                    self.im_count = a-1
                else :
                    self.im_count = self.im_count-1
                #print(im_count)
                text_label1 = "Page : " + str(self.im_count+1)+'/'+str(a)
                self.label_text1.configure(text = text_label1)
                self.label_text2.configure(text = str(os.path.basename(self.input_file_name[self.im_count])))
                self.img_ocr = cv2.imread(self.input_file_name[self.im_count])
                self.im_label.process_image(img=self.img_ocr,is_path=False)
                #self.display_image_from_loc(self.input_file_name[self.im_count])


    def write_to_file(self,file_name):
        try:
            content = self.content_text.get(1.0, 'end')
            with open(file_name + '.txt', 'w') as the_file:
                the_file.write(content)
        except IOError:
            tkinter.messagebox.showwarning("Save", "Could not save the file.")


    def save_as(self,event=None):
        input_file_name_ = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                               filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if input_file_name_:
            #global file_name
            self.file_name = input_file_name_
            self.write_to_file(self.file_name)
            self.root.title('{} - {}'.format(os.path.basename(self.file_name), self.PROGRAM_NAME))
        return "break"


    def save(self,event=None):
        #global file_name
        if not self.file_name:
            self.save_as()
        else:
            self.write_to_file(self.file_name)
        return "break"

    def select_all(self,event=None):
        self.content_text.tag_add('sel', '1.0', 'end')
        return "break"

    def copy(self,):
        self.content_text.event_generate("<<Copy>>")
        return "break"

    def exit_program(self,event=None):
        if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):
            root.destroy()
            
    def display_about_messagebox(self,event=None):
        tkinter.messagebox.showinfo(
            "About", "{}".format("Syahirachna OCR V1.0"))
    
    
    def display_help_messagebox(self,event=None):
        tkinter.messagebox.showinfo(
            "Help", "Write a mail to : issues@syahirachna.com",
            icon='question')


    def file_menu_fn(self,bar_var):
        #file menu
        file_ = Menu(bar_var, tearoff = 0)
        #file_.add_command(label='New', accelertator='Ctrl+N', compound='left',
        #                      image=new_file_icon, underline=0, command=new_file)
        file_.add_command(label='Open Images', accelerator='Ctrl+O', compound='left',
                              image=self.open_file_icon, underline=0, command=self.open_file)
        file_.add_command(label='Open PDF file', accelerator='Ctrl+O', compound='left',
                              image=self.open_file_icon, underline=0, command=self.open_pdf_file)
        file_.add_command(label='Save', accelerator='Ctrl+S',
                              compound='left', image=self.save_file_icon, underline=0, command=self.save)
        file_.add_command(label='Save as', accelerator='Shift+Ctrl+S', command=self.save_as)
        file_.add_separator()
        file_.add_command(label='Exit', accelerator='Alt+F4', command=self.exit_program)
        return file_
        
    def edit_menu_fn(self,bar_var):
        #edit menu
        edit_ = Menu(bar_var, tearoff=0)
        edit_.add_command(label='Copy', accelerator='Ctrl+C',
                              compound='left', image=self.copy_icon, command=self.copy)
        edit_.add_command(label='Select All', underline=7,
                              accelerator='Ctrl+A', command=self.select_all)
        return edit_

    def about_menu_fn(self,bar_var):
        about_ = Menu(bar_var, tearoff=0)
        about_.add_command(label='About', command=self.display_about_messagebox)
        about_.add_command(label='Help', command=self.display_help_messagebox)
        about_.add_command(label='Readme', command=self.readme_file_open)
        #self.B3 = Button(InputFrame, text='Graphical Plots', command=handler, bd=5, width=13, font="14")
        #about_.add_command(Label='Legal Information', command=display_legal_msg)
        return about_

    def menu_fn(self, root):
        menubar = Menu(self.root)
        file_menu = self.file_menu_fn(menubar)
        menubar.add_cascade(label = 'File', menu=file_menu)
        view_menu = self.edit_menu_fn(menubar)
        menubar.add_cascade(label = 'View', menu=view_menu)
        about_menu = self.about_menu_fn(menubar)
        menubar.add_cascade(label = 'About', menu=about_menu)
        return menubar
        
    ######################################################################
    #Initializing root
    def main(self):
        shortcut_bar = Frame(self.root, height=25, background='gray') #
        shortcut_bar.pack(expand='no', fill='x')
        open_sc = Button(shortcut_bar, text="Open Image Files", command=self.open_file)
        open_sc.pack(side='left')
        open_sc = Button(shortcut_bar, text="Open PDF File", command=self.open_pdf_file)
        open_sc.pack(side='left')
        copy_sc = Button(shortcut_bar, text="Copy", command=self.copy)
        copy_sc.pack(side = 'right')
        sel_all_sc = Button(shortcut_bar, text="Select All", command=self.select_all)
        sel_all_sc.pack(side = 'right')

        ##############################################################################
        #info_bar_spec
        info_bar = Frame(self.root,  height=25)
        info_bar.pack(expand='no', fill='x')
        info_bar.pack_propagate(0)
        #prev_button
        prev_button = Button(info_bar, text = "Previous", command = self.prev_im)
        prev_button.pack(expand='no', side = 'left')        
        #label_text for image name display
        self.label_text2 = Label(info_bar, width = 50)
        self.label_text2.pack(expand='no', side = 'left')
        #next button
        next_button = Button(info_bar, text = "Next", command = self.next_im)
        next_button.pack(expand='no', side = 'left')        
        #label text for total number of selected image
        self.label_text1 = Label(info_bar, width = 20)
        self.label_text1.pack(expand='no', side = 'left')


        #print(im_count)
        #if len(self.input_file_name)>0:
        #    print(self.input_file_name[self.im_count])


        #################################################################################
        #image frame
        self.frame_im = Frame(self.root, height = int(self.h_), width= int(self.width_*0.45), background = "white")
        #self.frame_im.place(height = self.h_, width=self.width_*0.45)
        self.frame_im.pack(expand='no', side = 'left')
        self.frame_im.pack_propagate(False)
        self.im_label = CanvasImage(self.frame_im, int(self.h_), int(self.width_*0.45))
        self.im_label.grid(row=0,column=0,sticky='news')


        #################################################################################
        #button_drop_down frame
        self.frame_button_drop = Frame(self.root, height = self.h_, width=self.width_*0.1) #, background = "thistle4"
        #self.frame_button_drop.place(height = self.h_, width=self.width_*0.1)
        self.frame_button_drop.pack(expand='no', side = 'left')
        self.frame_button_drop.pack_propagate(False)
        #dropdown menu
        #language select
        self.lanvar = StringVar(self.frame_button_drop)
        self.choices_lan = {'English','Hindi','Bengali','Oriya','Punjabi'} #dictionary
        self.lanvar.set('Options') # default option
        self.lanMenu = OptionMenu(self.frame_button_drop, self.lanvar, *self.choices_lan)
        Label(self.frame_button_drop, text="Choose a language").pack(expand='no', side = 'top')
        self.lanMenu.pack(expand='no', side = 'top')
        self.lanvar.trace('w', self.find_lan)
        #font select
        self.fontvar = StringVar(self.frame_button_drop)
        self.choices_font = {'Unicode','English', 'Shiva-Medium','Kruti-Dev','Walkman-Chanakya'} #dictionary
        self.fontvar.set('Options') # default option
        self.fontMenu = OptionMenu(self.frame_button_drop, self.fontvar, *self.choices_font)
        Label(self.frame_button_drop, text="Choose Font").pack(expand='no', side = 'top')
        self.fontMenu.pack(expand='no', side = 'top')
        self.fontvar.trace('w', self.find_font)
        
        #psm select
        self.psmvar = StringVar(self.frame_button_drop)
        self.choices_psm = {'Uniform Text Mode','Normal Mode'} #dictionary
        self.psmvar.set('Options') # default option
        self.psmMenu = OptionMenu(self.frame_button_drop, self.psmvar, *self.choices_psm)
        Label(self.frame_button_drop, text="Choose Mode").pack(expand='no', side = 'top')
        self.psmMenu.pack(expand='no', side = 'top')
        self.psmvar.trace('w', self.find_psm)

        #print (font_val)
        #button
        conv_button = Button(self.frame_button_drop, text = "Convert", command = self.OCR_command)
        conv_button.pack(expand='no', side = 'top')
        conv_button1 = Button(self.frame_button_drop, text = "Convert All", command = self.OCR_command_all)
        conv_button1.pack(expand='no', side = 'top')

        #################################################################################
        #text frame
        self.frame_text = Frame(self.root, height = self.h_, width=self.width_*0.45, background = "white")
        #self.frame_text.place(height = self.h_, width=self.width_*0.45)
        self.frame_text.pack(expand='no', side = 'left')
        self.frame_text.pack_propagate(False)
        self.content_text = Text(self.frame_text, wrap='word', undo=1)
        self.content_text.pack(expand='yes', fill='both')
        self.scroll_bar = Scrollbar(self.content_text)
        self.content_text.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.content_text.yview)
        self.scroll_bar.pack(side='right', fill='y')
        # frame_last = Frame(root, height=200, background = 'red')
        # frame_last.pack(side='bottom')


        #######################################################################
        #menu_bar_spec
        self.menu_bar = self.menu_fn(self.root)