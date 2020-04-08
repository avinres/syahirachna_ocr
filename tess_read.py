import os
import numpy as np
import subprocess
import sys
import tempfile
from glob import iglob
from numpy import ndarray
try:
    from PIL import Image
except ImportError:
    import Image

tess_main = 'system/tesseract/tess'

def main_tess_fn(image, lan, psm):
    
    if psm == 'Uniform Text Mode':
        num_ = '6'
    elif psm == 'Normal Mode':
        num_ = '1'
    else: num_= '3'
    #saving a image in temporary file
    image = Image.fromarray(image)
    image = image.convert("RGB")
    extension_im = "png"
    extension_txt = 'txt'
    with tempfile.NamedTemporaryFile(prefix='syahi_', delete=False) as f:
        temp_name = f.name
    input_file_name = temp_name + os.extsep + extension_im
    #print(input_file_name)
    image.save(input_file_name, format=extension_im)
    #output_file_name is defined
    output_file_n = temp_name + '_tessout'
    #tesseract arguments to be passed
    tesseract_args = [tess_main, input_file_name, output_file_n, '-l', lan, '--psm', num_, "--oem", "1"]
    #subprocess_arguments for running cmd
    subprocess_args = {'stdin': subprocess.PIPE, 'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE,
                      'startupinfo': None, 'env': os.environ}
    if hasattr(subprocess, 'STARTUPINFO'):
        subprocess_args['startupinfo'] = subprocess.STARTUPINFO()
        subprocess_args['startupinfo'].dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess_args['startupinfo'].wShowWindow = subprocess.SW_HIDE

    #running subprocess
    tess_process = subprocess.Popen(tesseract_args, **subprocess_args)
    status_code, error_string = tess_process.wait(), tess_process.stderr.read()
    tess_process.stdin.close()
    tess_process.stdout.close()
    tess_process.stderr.close()

    output_file_name = output_file_n + os.extsep + extension_txt
    with open(output_file_name, 'rb') as output_file:
        text = output_file.read().decode('utf-8').strip()
        
    for filename in iglob(temp_name + '*' if temp_name else temp_name):
        os.remove(filename)
        
    return text
