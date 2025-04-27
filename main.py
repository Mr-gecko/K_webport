from flask import Flask, render_template, request, send_file
import os
from tmore import *
from kore.structure import Auto

DEBUG_VAR = True

PATH = os.getcwd().replace("\\", "/")
os.chdir(PATH)

Auto.path(PATH+"/downloads/downloaded")

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    clear_folder(PATH+"/downloads")
    valid = False
    if request.method == "POST":
        url = request.form.get("url")
        method = request.form.get("method")
        playlist = request.form.get("playlist")
        playlist = normalize_bool(playlist)
        print(url, method, playlist)
        if check_inputs(url, method, playlist):
            try:
                Auto.playlist(playlist)
                if method.lower() == "mp3":
                    Auto.mp3(url)
                elif method.lower() == "mp4":
                    Auto.mp4(url)
                elif method.lower() == "cover":
                    Auto.cover(url)
                elif method.lower() == "album":
                    Auto.playlist(False)
                    Auto.cover(url)
                    Auto.playlist(True)
                    Auto.mp3(url)
                elif method.lower() == "thumbnail":
                    Auto.thubnail(url)
            except:
                print("something went wrong")
                error = True
                return render_template("index.html", error=error)
            valid = True
            zip(PATH+"/downloads/downloaded")
    return render_template("index.html", valid=valid)

@app.route("/downloads", methods=["POST","GET"])
def download():
    clear_folder(PATH+"/downloads")
    return send_file(PATH+"/downloads/downloaded.zip", as_attachment=True)

@app.route("/", methods=["POST","GET"])
def reset():
    clear_folder(PATH+"/downloads")
    valid = False
    error = False
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = DEBUG_VAR

app.run(host="0.0.0.0", port=8500)
