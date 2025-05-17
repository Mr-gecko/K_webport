# import validators
import shutil
import os

def zip(folder):
    try:
        shutil.make_archive(folder, 'zip', folder)
        print("zipped!")
        return True
    except:
        return False

def clear_folder(folder):
    for file in os.listdir(folder):
        if file == "downloaded":
            clear_folder(folder+"/downloaded")
            continue
        os.remove(folder+"/"+file)

def normalize_bool(input):
    if str(input).lower() == "on":
        return True
    else:
        return False

def check_inputs(url:str, method:str, playlist:bool):
    if url:
        if method:
            return True
    return False
