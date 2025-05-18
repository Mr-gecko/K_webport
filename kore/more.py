import os
import json
from PIL import Image
import eyed3
import socket #only for the is_connected() function


DESKTOP_PATH_ITEM = "#d"
LOG_SWITCH = False


def get_abs_path(file=__file__):
    return os.path.dirname(file).replace("\\","/")

def get_homepath():
    if os.name == "nt":
        return f"{os.environ['HOMEPATH']}/Desktop".replace("\\", "/")
    else:
        return f"{os.environ['HOME']}/Desktop".replace("\\", "/")

def get_desktop_path():
    if os.name == "nt":
        return f"{os.environ['HOMEDRIVE']}{os.environ['HOMEPATH']}/Desktop".replace("\\", "/")
    else:
        return f"{os.environ['HOME']}/Desktop".replace("\\", "/")

def is_path(path:str):
    if os.path.exists(path):
        if os.path.isdir(path):
            return "Dir"
        elif os.path.isfile(path):
            return "File"
        else:
            return "NonType"
    else:
        return False

def normalize_path(path:str):
    path = path.replace(DESKTOP_PATH_ITEM, get_desktop_path())
    path = path.replace("\\", "/")
    return path

def load_json(json_file:str):
    try:
        with open(json_file, 'r') as file:
            return json.load(file)
    except json.decoder.JSONDecodeError as e:
        log("json",f"Unable to decode JSON, Error: {e}",1) # LEARNED A NEW THING
        log("json", "Failed to load config.json file",1)
        log("FATAL", "Config file not loaded, impossible to continue",1)
        exit()


def save_json(info:dict, json_file:str):
    add_info = json.dumps(info, indent=4)
    with open(json_file, "w") as file:
        file.write(add_info)

def create_path(path:str):
    try:
        os.mkdir(path)
        return path
    except:
        log("roadblock", "An error as occured, it may be the case that you tried creating a sub folder without creating the first folder first?",1)

def log(who:str, what:str, run:int=None):
    if run == 1: # you put one if you want it to run even with log option off (just for very important logs)
        print(f"[ {who} ]   {what}")
        return
    if LOG_SWITCH != False:
        print(f"[ {who} ]   {what}")

def write_path(where:str, path:str):
    info = load_json(where)
    info["path"] = path
    save_json(info, )

####    WORKER FUNCTIONS    ####

def convert_to_png(file):
    if get_extension(file) == "webp":
        thbn = Image.open(file).convert("RGB") # CONVERTING FILE FROM .webp TO .png
        newfile = f"{file[:-len(get_extension(file))-1]}.png"
        thbn.save(newfile, "png") # SAVING CONVERTED FILE IN ORIGINAL PATH
        os.remove(file)
        return newfile
    else:
        return file

def crop(file:str):
    if get_extension(file) == "png":
        im = Image.open(file)
        width, height = im.size   # Get dimensions

        # left = (width - newwidth)/2
        # top = (height - newheight)/2
        # right = (width + newwidth)/2
        # bottom = (height + newwidth)/2
        #                     |
        # IT WORKS LIFE THE ABOVE, NEWWIDTH, NEWHEIGHT ARE THE VARIABLES TO CHOSE THE NEW WIDTH AND HEIGHT, TO MAKE IT SQUARE THEY ARE ALL HEIGHT

        left = (width - height)/2
        top = (height - height)/2
        right = (width + height)/2
        bottom = (height + height)/2

        # Crop the center of the image
        im = im.crop((left, top, right, bottom))
        # SAVE THE IMAGE
        newfile = file[:-4]+"_cover.png"
        im.save(newfile, "png")
        os.remove(file)  # COVER AND THUMBNAIL ROADBLOCK, THIS WILL DELETE THE THUMBNAIL FILE IF THE COVER WILL BE DOWNLOADED AFTER IT
        return newfile
    else:
        return file

def get_extension(file):
    return file.split(".")[-1]

def get_filepath(entry):
    return entry["requested_downloads"][0]["filepath"].replace("\\", "/")

def fetch_artist(title):
    title = title.split(" - ")
    return title

def butch_title(file):
    split = file.split(" - ")
    if len(split) > 1:
        return split[1]
    else:
        return split[0]

def mild_butch_title(file):
    split = file.split(" - ")
    if len(split) > 1:

        return file.split(") ")[0] + ") " + split[1]
    else:
        return split[0]

def remove_code(file, code):
    return file.replace(f" [{code}]", "")

def remove_track_number(file):
    if get_extension(file) in ["mp4", "jpg", "png"]:
        renamed = f"{int(file[:3])}) {file[4:]}"
    else:
        if file[:2] != "NA":
            renamed = file[4:]
    return renamed

def cut_name(file, tags):
    if get_extension(file) == "mp3":
        renamed = remove_code(file, tags["code"])
        if tags["track_number"] in ["NA", None]:
            renamed = butch_title(renamed)
        else:
            renamed = remove_track_number(renamed)
            renamed = butch_title(renamed)
    elif get_extension(file) in ["mp4", "jpg", "png"]:
        renamed = file
        #renamed = remove_code(renamed, tags["code"]) # BY NOT SAVING IN THE FILE DETAILS THE CODE REMOVED WILL BE TOTALLY LOST
        if tags["track_number"] in ["NA", None]:
            renamed = butch_title(renamed)
        else:
            renamed = remove_track_number(file)
            renamed = mild_butch_title(renamed)
    else:
        return file
    return renamed

def attach_tags(entry):
    tags = {
        "track_number" : entry["playlist_index"],
        "code" : entry["id"],
        "webpage_url": entry["webpage_url"],
        "title": entry["title"],
    }
    if "album" in entry:
        tags["album"] = entry["album"]
    if "artist" in entry:
        tags["artist"] = entry["artist"]
    else:
        try: # THIS TRY IS TO MITIGATE THE INDEX OUT RANGE ERROR IN FETCH_ARTIST
            tags["artist"] = fetch_artist(entry["title"])[0]
            tags["title"] = fetch_artist(entry["title"])[1]
        except:
            tags["artist"] = "nf"
            tags["title"] = "nf"
    return tags

def add_tags(file, tags):
    if get_extension(file) == "mp3":
        audio = eyed3.load(file).tag
        audio.track_num = tags["track_number"]
        audio.title = tags["title"]
        if "artist" in tags and tags["artist"]:
            audio.artist = tags["artist"]
        if "album" in tags and tags["album"]:
            audio.album = tags["album"]
        audio.artist_url = audio.audio_file_url = audio.audio_source_url = tags["webpage_url"]
        audio.save()
    else:
        pass

def exception_calculate_playlist_thumbnail_name(entry):
    return "000 " + entry["playlist_title"] + " [" + entry["playlist_id"] + "].jpg"

def delete_exception_playlist_thumbnail(entry):
    try:
        os.remove(exception_calculate_playlist_thumbnail_name(entry))
    except FileNotFoundError:
        pass
    except: # ALL EXCEPTIONS
        pass

def calculate_control(type, entry):
    if type in ["mp3", "mp4"]:
        control = os.path.basename(get_filepath(entry))
    elif type == "thumbnail":
        control = os.path.basename(get_filepath(entry)[:-(len(get_extension(get_filepath(entry))))]+"webp")
    elif type == "cover":
        control = os.path.basename(get_filepath(entry)[:-(len(get_extension(get_filepath(entry))))]+"webp")
    return control

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
