import yt_dlp
from kore.more import *
import os
import eyed3

testing_K = """\
+----------------------------------------+\n\
|                                        |\n\
|               K project                |\n\
|          Quick_dl_E Reworked           |\n\
|                                        |\n\
|              Testing Kit               |\n\
|                                        |\n\
+----------------------------------------+\
"""

print(testing_K)

try:
    config = load_json(get_abs_path(__file__)+"/config.json")
    for file in config["files"]:
        globals()[file] = config["files"][file]
except FileNotFoundError as err:
    log("error", f"config.json file not found,\n Error: {err}",1)
    log("FATAL", "config file missing, impossible to continue",1)
    log("resolve", "try download config.json file and setup again https://github.com/Mr-gecko/K",1)
    exit()


from kore.UI import message, bool_paint

def check_files_routine():
    must_files = config["files"].values()
    actual_files = []
    for file in os.listdir(get_abs_path(__file__)):
        actual_files.append(file)
    for mf in must_files:
        if mf in actual_files:
            log("log:check_files_routine", f"{mf} present")
            continue
        else:
            log("log:check_files_routine", f"{mf} missing")
            message("<error>error<r>",f"check_files_routine(),\n missing file: <file>{mf}<r>")
            message("<warning>FATAL<r>", "Path file not loaded, impossible to continue")
            # exit()

def stitch(file, entry, dl):
    control = calculate_control(dl.settings["format"], entry)
    # print("file: "  + file)
    # print("control: " + control)
    # input()
    if file == control:
        # print("inside stitch: " + file)
        # input()
        tags = attach_tags(entry)
        add_tags(file, tags)
        file = convert_to_png(file)
        if dl.settings["format"] == "cover":
            file = crop(file)
        if dl.settings["playlist"] == True:
            delete_exception_playlist_thumbnail(entry)
        renamed_file = cut_name(file, tags)
        try:
            os.rename(file, renamed_file)
        except FileExistsError:
            message("<roadblock>roadblock<r>", "<file>"+renamed_file+"<r>" + " already exists, replacing old files")
            os.remove(renamed_file)
            os.rename(file, renamed_file)
        except FileNotFoundError:
            message("<error>error<r>", "<file>"+file+"<r>" + " not found")

check_files_routine()



class Main():

    def __init__(self):
        self.ABS_PATH = get_abs_path(__file__)
        self.opts = {}
        self.settings = {
        "path": "",
        "format": "",
        "playlist": False,
        }

        self.default_init_set()

####    UTILITY FUNCTIONS    ####

    def default_init_set(self):
        self.retrieve_path()
        self.set_format("mp3")
        # self.set_opts(load_json(str(f"{self.ABS_PATH}/{CONFIG_FILE}"))["formats"][self.settings["format"]])
        self.set_playlist(False)

    def retrieve_path(self):
        try:
            with open(f"{self.ABS_PATH}/{PATH_FILE}", "r") as f:
                try:
                    path = [line.strip().replace("\\", "/") for line in f.readlines()][0]
                    path = os.path.abspath(path).replace("\\", "/")
                except:
                    log("log:Main:retrieve_path", "path could not be retrieved from the path file, default is set")
                    message("<error>error<r>", "path not found, default set to " + "<path>"+get_desktop_path()+"<r>")
                    path = get_desktop_path()
                    self.set_path(path)
                    return 0
            if os.path.exists(path):
                #print("yep")
                pass
            else:
                log("log:Main:retrieve_path", "the path retrieved is not found, default is set")
                message("<error>error<r>", "path not found, default set to " + "<path>"+get_desktop_path()+"<r>")
                path = get_desktop_path()
                self.set_path(path)
                return 0
            self.set_path(path)
        except FileNotFoundError as err:
            log("log:Main:retrieve_path", "path file is not found, initializing a new path file")
            message("<error>error<r>", f"Path file not found, creating new <file>PATH.txt<r> file. Error: {err}")
            self.write_path()
            message("error:manager", "A new path file has been created")
            return self.retrieve_path()

    def write_path(self):
        with open (f"{self.ABS_PATH}/{PATH_FILE}", "w") as f:
            f.write(self.settings["path"])
        log("log:Main:write_path", "path written to file")

    def set(self, where:str, what):
        self.settings[where] = what
        log("log:Main:set", f"\"{what}\" has been set to \"{where}\"")

    def calculate_outtmpl(self):
        if self.settings["playlist"] == True:
            return "%(playlist_index)03d %(title)s [%(id)s].%(ext)s"
        elif self.settings["playlist"] == False:
            return "%(title)s [%(id)s].%(ext)s"
        else:
            log("error:Main:calculate_outtmpl","calculate_outtmpl() error playlist",1)

    def reload_config(self):
        try:
            config = load_json(self.ABS_PATH+"/"+CONFIG_FILE)
        except:
            log("error:Main:reload_config", "smoething went wrong, could not reload config file",1)

####    MAIN FUNCTIONS    ####

    def set_path(self, path:str):
        if is_path(path) == "Dir":
            self.set("path", path)
            self.write_path()
            log("log:Main:set_path", f"path set to {path}")
            message("*", "Path has been set to " + "<path>"+path+"<r>")
        elif is_path(path) == False:
            self.set("path", create_path(path))
            self.write_path()
            log("log:Main:set_path", "the path is not found, initializing it")
            message("*", "<removed>"+path+"<r>" + " has not been found")
            message("*", "creating " + "<created>"+path+"<r>")
            message("*", "Path has been set to " + "<path>"+path+"<r>")
        else:
            log("log:Main:set_path", "something went wrong")
            message("<error>error<r>", "invalid path")

    def set_format(self, format:str):
        if format in config["formats"].keys():
            self.set("format", format)
            self.set_opts(config["formats"][format])
        else:
            message("<error>error<r>", "invalid format")

    def set_opts(self, opts:dict):
        if self.settings["playlist"] != None:
            opts["noplaylist"] = not self.settings["playlist"]
            self.opts = opts
        else:
            log("error","self_otps() error noplaylist")

    def set_playlist(self, playlist:bool):
        self.set("playlist", playlist)
        self.opts["noplaylist"] = not playlist
        message("*", "playlist set to " + bool_paint(str(playlist)))

    def download(self, url:str):
        os.chdir(self.settings["path"])
        self.opts["outtmpl"] = self.calculate_outtmpl()
        with yt_dlp.YoutubeDL(self.opts) as ydl:
            informations = ydl.sanitize_info(ydl.extract_info(url))
            return informations

dl = Main()

class Worker():

    def mp3(url:str):
        dl.set_format("mp3")
        return dl.download(url)

    def mp4(url:str): #### FROM HERE DO THE SAME FOR MP4, AS FAR AS NOW EVERYTHING WORKS EXCEPT FOR THE FileExistsError LOOK IN TO THAT
        dl.set_format("mp4")
        return dl.download(url)

    def thumbnail(url:str):
        dl.set_format("thumbnail")
        return dl.download(url)

    def cover(url:str):
        dl.set_format("cover")
        return dl.download(url)

    def automatic(informations):
        if len(informations["id"]) > 11: # THIS IS A PLAYLIST
            print("playlist automatic!")
            for file in os.listdir(dl.settings["path"]):
                for entry in informations["entries"]:
                    stitch(file, entry, dl)

        elif len(informations["id"]) == 11: # THIS IS A SINGLE
            print("single automatic!")
            for file in os.listdir(dl.settings["path"]):
                stitch(file, informations, dl)
        else:
            message("what", "in the automatic fuck is this?\nUnexpected data type")

    def playlist(play:bool=None):
        if play == None:
            log("worker", "playlist is set to " + str(dl.settings["playlist"]))
            message("*", f"playlist is set to " + bool_paint(str(dl.settings["playlist"])))
            return
        dl.set_playlist(play)
        log("worker", "playlist set to " + str(play))

    def path(path:str=None):
        if path == None:
            log("worker", "current path is set to " + dl.settings["path"])
            message("*", f"current path is set to <path>{dl.settings['path']}<r>")
            return
        elif path[0] == "/":
            path = dl.settings["path"] + path

        path = normalize_path(path)

        dl.set_path(path)
        log("worker", "path set to " + path)

class Auto():

    def mp3(url:str):
        Worker.automatic(Worker.mp3(url))
        print("\a") # SOUND EFFECT WHEN DOWNLOAD IS OVER

    def mp4(url:str):
        Worker.automatic(Worker.mp4(url))
        print("\a") # SOUND EFFECT WHEN DOWNLOAD IS OVER

    def thumbnail(url:str):
        Worker.automatic(Worker.thumbnail(url))

    def cover(url:str):
        Worker.automatic(Worker.cover(url))

    def playlist(play:bool=None):
        Worker.playlist(play)

    def path(path:str=None):
        Worker.path(path)



# url = "https://www.youtube.com/watch?v=0EVVKs6DQLo"
# url = "https://youtube.com/playlist?list=PLjtPyc_q0XcQLcNrETDfSogSrpFLziAmU&si=exl1LH9nOLY2AyFJ"
#url = "https://www.youtube.com/watch?v=6F9N-6ITFnA&list=PLjtPyc_q0XcQLcNrETDfSogSrpFLziAmU&index=1"
#url = "https://www.youtube.com/watch?v=tfyWWod9gBY&list=PLcowPSotRhCdIRHPJrm9CbdSGNBpiYa8g&index=2"

# info = Work.mp4(url)
# Work.automatic(info)

# save_json(info, dl.settings["path"]+"/INFO.json")


####    TESTING    ####
# dl.set_playlist(True)
# automatic(mp3(url))
# automatic(mp4(url))
# automatic(thumbnail(url))
# automatic(cover(url))
# dl.set_playlist(False)
# automatic(mp3(url))
# automatic(mp4(url))
# automatic(thumbnail(url))
# automatic(cover(url))
