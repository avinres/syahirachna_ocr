import os
import numpy as np
import subprocess
import sys
import tempfile
from glob import iglob
from numpy import ndarray
from PIL import Image, ImageTk
import math
import warnings
import tkinter as tk
from tkinter import ttk
import cv2
from tkinter import Tk, PhotoImage, Menu, Frame, Text, Scrollbar, IntVar, \
    StringVar, BooleanVar, Button, END, Label, INSERT, Canvas, OptionMenu
import tkinter.filedialog
import tkinter.messagebox
from PIL import ImageTk as itk
#import tensorflow as tf
import rsa
from datetime import datetime, timedelta
import pickle
import getpass
import netifaces
from skimage.filters import threshold_local
import imutils

import skew_correct
import uni_to_kruti
import uni_to_shiv
import uni_to_walkman
import tess_read
import sim_ocr
import zoom
import clean_im
import main_ocr

main_ocr.syahirachna_ocr()
