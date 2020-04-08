import tess_read as tr
import cv2
import os
import uni_to_kruti as uk
import uni_to_shiv as us
import uni_to_walkman as uw


def simple_ocr(img, lan, psm):
    recon = img
    if lan == 'English':
        text = tr.main_tess_fn(recon, lan="eng", psm = psm)
    elif lan == 'Hindi':
        text = tr.main_tess_fn(recon, lan="hin", psm = psm)
    elif lan == 'Punjabi':
        text = tr.main_tess_fn(recon, lan="pan", psm = psm)
    elif lan == 'oriya':
        text = tr.main_tess_fn(recon, lan="ori", psm = psm)
    elif lan == 'Bengali':
        text = tr.main_tess_fn(recon, lan="ben", psm = psm)
    return text

def text_out(img,lan,font,psm):
    text = simple_ocr(img = img, lan=lan,psm=psm)
    if font == 'Shiva-Medium':
        text = us.convert_to_shiva(text)
    elif font == 'Kruti-Dev':
        text = uk.convert_to_kruti(text)
    elif font == 'Walkman-Chanakya':
        text = uw.convert_to_walkman(text)
    elif (font == 'Unicode') or (font == 'English'):
        text = text

    position_of_new_line = text.find("\n")
    #print(position_of_new_line)
    while(position_of_new_line != -1):
        character_right_to_new_line = text[position_of_new_line + 1]
        text = text.replace("\n", " ")
        if (character_right_to_new_line == "\n"):
            position_of_new_line = position_of_new_line + 3
        position_of_new_line = text.find("\n", position_of_new_line)
    #print(text)
    #final_string = final_string + "\n" + text
    #text = final_string
    return text