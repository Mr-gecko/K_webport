from kore.add_ons.Yui import structure as Yui
from kore.more import load_json

config_file = load_json("kore/config.json")
colors = config_file["colors"]
prompt_paint_conf = config_file["paint_confs"]["prompt"]

def bool_paint(line:str):
    if line.upper() == "TRUE":
        line = brush("<true>True<r>")
    elif line.upper() == "FALSE":
        line = brush("<false>False<r>")
    return line

def brush(line):
    for brush_key in config_file["brush_keys"]:
        line = line.replace(f"{brush_key}", Yui.brush(config_file["brush_keys"][brush_key][0],config_file["brush_keys"][brush_key][1]))
    return line

def message(who:str, what:str):
    print(brush(f"[ {who} ]   {what}"))
