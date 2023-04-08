import os, shutil
import re


def clear_folder_image(file):
    os.remove(file)         
        
          
def clear_folder_upload(file):
    os.remove(file)         
    
    
def clear_blank_lines(string_params):
    string = re.sub(r'^\s+$|\n', '', string_params)
    return string


def clear_array_empty(array):
    array_clear_empty = [x for x in array if x != '']
    return array_clear_empty
 


def clear_jump_lines(string):
    lines = string.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]

    string_without_empty_lines = ""

    for line in non_empty_lines:
        string_without_empty_lines += line + "\n"
        
    return string_without_empty_lines       