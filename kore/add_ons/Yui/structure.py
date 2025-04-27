# \\\\ MODIFIED 26/11/2024 - 00:30 - Mr-gecko
# LAST MODIFIED 16/02/2025 - 16:23 - Mr-gecko - NOTES: added brush() function
#

import os
import re

# enable ansi escapes
os.system("")

YuiDB = {
    "assets":{
        "line":"-",
        "dline":"=",
        "bline":"_",

        "brackets":( "[ ", " ]" ),
        "pbrackets":( "( ", " )" ),
        "gbrackets":( "{ ", " }" ),
        "sbrackets":( "| ", " |" ),
    },
    "fonts" : {
    "bold" : ("\033[1m", "\033[22m"),
    "dim" : ("\033[2m", "\033[22m"),
    "italic" : ("\033[3m", "\033[23m"),
    "underline" : ("\033[4m", "\033[24m"),
    "blink" : ("\033[5m", "\033[25m"),
    "inverse" : ("\033[7m", "\033[27m"),
    "hide" : ("\033[8m", "\033[28m"),
    "strike" : ("\033[9m", "\033[29m")
    },
    "colors" : {
        "bases" : {
            "black" : ("\033[30m", "\033[40m"),
            "red" : ("\033[31m", "\033[41m"),
            "green" : ("\033[32m", "\033[42m"),
            "yellow" : ("\033[33m", "\033[43m"),
            "blue" : ("\033[34m", "\033[44m"),
            "magenta" : ( "\033[35m", "\033[45m"),
            "cyan" : ("\033[36m", "\033[46m"),
            "white" : ("\033[37m", "\033[47m"),
            "default" : ("\033[39m", "\033[49m"),
            "reset" : ("\033[0m", "\033[0m")
            },
        "brights" : {
            "bright_black" : ("\033[90m", "\033[100m"),
            "bright_red" : ("\033[91m", "\033[101m"),
            "bright_green" : ("\033[92m", "\033[102m"),
            "bright_yellow" : ("\033[93m", "\033[103m"),
            "bright_blue" : ("\033[94m", "\033[104m"),
            "bright_magenta" : ("\033[95m", "\033[105m"),
            "bright_cyan" : ("\033[96m", "\033[106m"),
            "bright_white" : ("\033[97m", "\033[107m")
            },
        "255" : {
            "0" : ("\033[38;5;0m", "\033[48;5;0m"),
            "1" : ("\033[38;5;1m", "\033[48;5;1m"),
            "2" : ("\033[38;5;2m", "\033[48;5;2m"),
            "3" : ("\033[38;5;3m", "\033[48;5;3m"),
            "4" : ("\033[38;5;4m", "\033[48;5;4m"),
            "5" : ("\033[38;5;5m", "\033[48;5;5m"),
            "6" : ("\033[38;5;6m", "\033[48;5;6m"),
            "7" : ("\033[38;5;7m", "\033[48;5;7m"),
            "8" : ("\033[38;5;8m", "\033[48;5;8m"),
            "9" : ("\033[38;5;9m", "\033[48;5;9m"),
            "10" : ("\033[38;5;10m", "\033[48;5;10m"),
            "11" : ("\033[38;5;11m", "\033[48;5;11m"),
            "12" : ("\033[38;5;12m", "\033[48;5;12m"),
            "13" : ("\033[38;5;13m", "\033[48;5;13m"),
            "14" : ("\033[38;5;14m", "\033[48;5;14m"),
            "15" : ("\033[38;5;15m", "\033[48;5;15m"),
            "16" : ("\033[38;5;16m", "\033[48;5;16m"),
            "17" : ("\033[38;5;17m", "\033[48;5;17m"),
            "18" : ("\033[38;5;18m", "\033[48;5;18m"),
            "19" : ("\033[38;5;19m", "\033[48;5;19m"),
            "20" : ("\033[38;5;20m", "\033[48;5;20m"),
            "21" : ("\033[38;5;21m", "\033[48;5;21m"),
            "22" : ("\033[38;5;22m", "\033[48;5;22m"),
            "23" : ("\033[38;5;23m", "\033[48;5;23m"),
            "24" : ("\033[38;5;24m", "\033[48;5;24m"),
            "25" : ("\033[38;5;25m", "\033[48;5;25m"),
            "26" : ("\033[38;5;26m", "\033[48;5;26m"),
            "27" : ("\033[38;5;27m", "\033[48;5;27m"),
            "28" : ("\033[38;5;28m", "\033[48;5;28m"),
            "29" : ("\033[38;5;29m", "\033[48;5;29m"),
            "30" : ("\033[38;5;30m", "\033[48;5;30m"),
            "31" : ("\033[38;5;31m", "\033[48;5;31m"),
            "32" : ("\033[38;5;32m", "\033[48;5;32m"),
            "33" : ("\033[38;5;33m", "\033[48;5;33m"),
            "34" : ("\033[38;5;34m", "\033[48;5;34m"),
            "35" : ("\033[38;5;35m", "\033[48;5;35m"),
            "36" : ("\033[38;5;36m", "\033[48;5;36m"),
            "37" : ("\033[38;5;37m", "\033[48;5;37m"),
            "38" : ("\033[38;5;38m", "\033[48;5;38m"),
            "39" : ("\033[38;5;39m", "\033[48;5;39m"),
            "40" : ("\033[38;5;40m", "\033[48;5;40m"),
            "41" : ("\033[38;5;41m", "\033[48;5;41m"),
            "42" : ("\033[38;5;42m", "\033[48;5;42m"),
            "43" : ("\033[38;5;43m", "\033[48;5;43m"),
            "44" : ("\033[38;5;44m", "\033[48;5;44m"),
            "45" : ("\033[38;5;45m", "\033[48;5;45m"),
            "46" : ("\033[38;5;46m", "\033[48;5;46m"),
            "47" : ("\033[38;5;47m", "\033[48;5;47m"),
            "48" : ("\033[38;5;48m", "\033[48;5;48m"),
            "49" : ("\033[38;5;49m", "\033[48;5;49m"),
            "50" : ("\033[38;5;50m", "\033[48;5;50m"),
            "51" : ("\033[38;5;51m", "\033[48;5;51m"),
            "52" : ("\033[38;5;52m", "\033[48;5;52m"),
            "53" : ("\033[38;5;53m", "\033[48;5;53m"),
            "54" : ("\033[38;5;54m", "\033[48;5;54m"),
            "55" : ("\033[38;5;55m", "\033[48;5;55m"),
            "56" : ("\033[38;5;56m", "\033[48;5;56m"),
            "57" : ("\033[38;5;57m", "\033[48;5;57m"),
            "58" : ("\033[38;5;58m", "\033[48;5;58m"),
            "59" : ("\033[38;5;59m", "\033[48;5;59m"),
            "60" : ("\033[38;5;60m", "\033[48;5;60m"),
            "61" : ("\033[38;5;61m", "\033[48;5;61m"),
            "62" : ("\033[38;5;62m", "\033[48;5;62m"),
            "63" : ("\033[38;5;63m", "\033[48;5;63m"),
            "64" : ("\033[38;5;64m", "\033[48;5;64m"),
            "65" : ("\033[38;5;65m", "\033[48;5;65m"),
            "66" : ("\033[38;5;66m", "\033[48;5;66m"),
            "67" : ("\033[38;5;67m", "\033[48;5;67m"),
            "68" : ("\033[38;5;68m", "\033[48;5;68m"),
            "69" : ("\033[38;5;69m", "\033[48;5;69m"),
            "70" : ("\033[38;5;70m", "\033[48;5;70m"),
            "71" : ("\033[38;5;71m", "\033[48;5;71m"),
            "72" : ("\033[38;5;72m", "\033[48;5;72m"),
            "73" : ("\033[38;5;73m", "\033[48;5;73m"),
            "74" : ("\033[38;5;74m", "\033[48;5;74m"),
            "75" : ("\033[38;5;75m", "\033[48;5;75m"),
            "76" : ("\033[38;5;76m", "\033[48;5;76m"),
            "77" : ("\033[38;5;77m", "\033[48;5;77m"),
            "78" : ("\033[38;5;78m", "\033[48;5;78m"),
            "79" : ("\033[38;5;79m", "\033[48;5;79m"),
            "80" : ("\033[38;5;80m", "\033[48;5;80m"),
            "81" : ("\033[38;5;81m", "\033[48;5;81m"),
            "82" : ("\033[38;5;82m", "\033[48;5;82m"),
            "83" : ("\033[38;5;83m", "\033[48;5;83m"),
            "84" : ("\033[38;5;84m", "\033[48;5;84m"),
            "85" : ("\033[38;5;85m", "\033[48;5;85m"),
            "86" : ("\033[38;5;86m", "\033[48;5;86m"),
            "87" : ("\033[38;5;87m", "\033[48;5;87m"),
            "88" : ("\033[38;5;88m", "\033[48;5;88m"),
            "89" : ("\033[38;5;89m", "\033[48;5;89m"),
            "90" : ("\033[38;5;90m", "\033[48;5;90m"),
            "91" : ("\033[38;5;91m", "\033[48;5;91m"),
            "92" : ("\033[38;5;92m", "\033[48;5;92m"),
            "93" : ("\033[38;5;93m", "\033[48;5;93m"),
            "94" : ("\033[38;5;94m", "\033[48;5;94m"),
            "95" : ("\033[38;5;95m", "\033[48;5;95m"),
            "96" : ("\033[38;5;96m", "\033[48;5;96m"),
            "97" : ("\033[38;5;97m", "\033[48;5;97m"),
            "98" : ("\033[38;5;98m", "\033[48;5;98m"),
            "99" : ("\033[38;5;99m", "\033[48;5;99m"),
            "100" : ("\033[38;5;100m", "\033[48;5;100m"),
            "101" : ("\033[38;5;101m", "\033[48;5;101m"),
            "102" : ("\033[38;5;102m", "\033[48;5;102m"),
            "103" : ("\033[38;5;103m", "\033[48;5;103m"),
            "104" : ("\033[38;5;104m", "\033[48;5;104m"),
            "105" : ("\033[38;5;105m", "\033[48;5;105m"),
            "106" : ("\033[38;5;106m", "\033[48;5;106m"),
            "107" : ("\033[38;5;107m", "\033[48;5;107m"),
            "108" : ("\033[38;5;108m", "\033[48;5;108m"),
            "109" : ("\033[38;5;109m", "\033[48;5;109m"),
            "110" : ("\033[38;5;110m", "\033[48;5;110m"),
            "111" : ("\033[38;5;111m", "\033[48;5;111m"),
            "112" : ("\033[38;5;112m", "\033[48;5;112m"),
            "113" : ("\033[38;5;113m", "\033[48;5;113m"),
            "114" : ("\033[38;5;114m", "\033[48;5;114m"),
            "115" : ("\033[38;5;115m", "\033[48;5;115m"),
            "116" : ("\033[38;5;116m", "\033[48;5;116m"),
            "117" : ("\033[38;5;117m", "\033[48;5;117m"),
            "118" : ("\033[38;5;118m", "\033[48;5;118m"),
            "119" : ("\033[38;5;119m", "\033[48;5;119m"),
            "120" : ("\033[38;5;120m", "\033[48;5;120m"),
            "121" : ("\033[38;5;121m", "\033[48;5;121m"),
            "122" : ("\033[38;5;122m", "\033[48;5;122m"),
            "123" : ("\033[38;5;123m", "\033[48;5;123m"),
            "124" : ("\033[38;5;124m", "\033[48;5;124m"),
            "125" : ("\033[38;5;125m", "\033[48;5;125m"),
            "126" : ("\033[38;5;126m", "\033[48;5;126m"),
            "127" : ("\033[38;5;127m", "\033[48;5;127m"),
            "128" : ("\033[38;5;128m", "\033[48;5;128m"),
            "129" : ("\033[38;5;129m", "\033[48;5;129m"),
            "130" : ("\033[38;5;130m", "\033[48;5;130m"),
            "131" : ("\033[38;5;131m", "\033[48;5;131m"),
            "132" : ("\033[38;5;132m", "\033[48;5;132m"),
            "133" : ("\033[38;5;133m", "\033[48;5;133m"),
            "134" : ("\033[38;5;134m", "\033[48;5;134m"),
            "135" : ("\033[38;5;135m", "\033[48;5;135m"),
            "136" : ("\033[38;5;136m", "\033[48;5;136m"),
            "137" : ("\033[38;5;137m", "\033[48;5;137m"),
            "138" : ("\033[38;5;138m", "\033[48;5;138m"),
            "139" : ("\033[38;5;139m", "\033[48;5;139m"),
            "140" : ("\033[38;5;140m", "\033[48;5;140m"),
            "141" : ("\033[38;5;141m", "\033[48;5;141m"),
            "142" : ("\033[38;5;142m", "\033[48;5;142m"),
            "143" : ("\033[38;5;143m", "\033[48;5;143m"),
            "144" : ("\033[38;5;144m", "\033[48;5;144m"),
            "145" : ("\033[38;5;145m", "\033[48;5;145m"),
            "146" : ("\033[38;5;146m", "\033[48;5;146m"),
            "147" : ("\033[38;5;147m", "\033[48;5;147m"),
            "148" : ("\033[38;5;148m", "\033[48;5;148m"),
            "149" : ("\033[38;5;149m", "\033[48;5;149m"),
            "150" : ("\033[38;5;150m", "\033[48;5;150m"),
            "151" : ("\033[38;5;151m", "\033[48;5;151m"),
            "152" : ("\033[38;5;152m", "\033[48;5;152m"),
            "153" : ("\033[38;5;153m", "\033[48;5;153m"),
            "154" : ("\033[38;5;154m", "\033[48;5;154m"),
            "155" : ("\033[38;5;155m", "\033[48;5;155m"),
            "156" : ("\033[38;5;156m", "\033[48;5;156m"),
            "157" : ("\033[38;5;157m", "\033[48;5;157m"),
            "158" : ("\033[38;5;158m", "\033[48;5;158m"),
            "159" : ("\033[38;5;159m", "\033[48;5;159m"),
            "160" : ("\033[38;5;160m", "\033[48;5;160m"),
            "161" : ("\033[38;5;161m", "\033[48;5;161m"),
            "162" : ("\033[38;5;162m", "\033[48;5;162m"),
            "163" : ("\033[38;5;163m", "\033[48;5;163m"),
            "164" : ("\033[38;5;164m", "\033[48;5;164m"),
            "165" : ("\033[38;5;165m", "\033[48;5;165m"),
            "166" : ("\033[38;5;166m", "\033[48;5;166m"),
            "167" : ("\033[38;5;167m", "\033[48;5;167m"),
            "168" : ("\033[38;5;168m", "\033[48;5;168m"),
            "169" : ("\033[38;5;169m", "\033[48;5;169m"),
            "170" : ("\033[38;5;170m", "\033[48;5;170m"),
            "171" : ("\033[38;5;171m", "\033[48;5;171m"),
            "172" : ("\033[38;5;172m", "\033[48;5;172m"),
            "173" : ("\033[38;5;173m", "\033[48;5;173m"),
            "174" : ("\033[38;5;174m", "\033[48;5;174m"),
            "175" : ("\033[38;5;175m", "\033[48;5;175m"),
            "176" : ("\033[38;5;176m", "\033[48;5;176m"),
            "177" : ("\033[38;5;177m", "\033[48;5;177m"),
            "178" : ("\033[38;5;178m", "\033[48;5;178m"),
            "179" : ("\033[38;5;179m", "\033[48;5;179m"),
            "180" : ("\033[38;5;180m", "\033[48;5;180m"),
            "181" : ("\033[38;5;181m", "\033[48;5;181m"),
            "182" : ("\033[38;5;182m", "\033[48;5;182m"),
            "183" : ("\033[38;5;183m", "\033[48;5;183m"),
            "184" : ("\033[38;5;184m", "\033[48;5;184m"),
            "185" : ("\033[38;5;185m", "\033[48;5;185m"),
            "186" : ("\033[38;5;186m", "\033[48;5;186m"),
            "187" : ("\033[38;5;187m", "\033[48;5;187m"),
            "188" : ("\033[38;5;188m", "\033[48;5;188m"),
            "189" : ("\033[38;5;189m", "\033[48;5;189m"),
            "190" : ("\033[38;5;190m", "\033[48;5;190m"),
            "191" : ("\033[38;5;191m", "\033[48;5;191m"),
            "192" : ("\033[38;5;192m", "\033[48;5;192m"),
            "193" : ("\033[38;5;193m", "\033[48;5;193m"),
            "194" : ("\033[38;5;194m", "\033[48;5;194m"),
            "195" : ("\033[38;5;195m", "\033[48;5;195m"),
            "196" : ("\033[38;5;196m", "\033[48;5;196m"),
            "197" : ("\033[38;5;197m", "\033[48;5;197m"),
            "198" : ("\033[38;5;198m", "\033[48;5;198m"),
            "199" : ("\033[38;5;199m", "\033[48;5;199m"),
            "200" : ("\033[38;5;200m", "\033[48;5;200m"),
            "201" : ("\033[38;5;201m", "\033[48;5;201m"),
            "202" : ("\033[38;5;202m", "\033[48;5;202m"),
            "203" : ("\033[38;5;203m", "\033[48;5;203m"),
            "204" : ("\033[38;5;204m", "\033[48;5;204m"),
            "205" : ("\033[38;5;205m", "\033[48;5;205m"),
            "206" : ("\033[38;5;206m", "\033[48;5;206m"),
            "207" : ("\033[38;5;207m", "\033[48;5;207m"),
            "208" : ("\033[38;5;208m", "\033[48;5;208m"),
            "209" : ("\033[38;5;209m", "\033[48;5;209m"),
            "210" : ("\033[38;5;210m", "\033[48;5;210m"),
            "211" : ("\033[38;5;211m", "\033[48;5;211m"),
            "212" : ("\033[38;5;212m", "\033[48;5;212m"),
            "213" : ("\033[38;5;213m", "\033[48;5;213m"),
            "214" : ("\033[38;5;214m", "\033[48;5;214m"),
            "215" : ("\033[38;5;215m", "\033[48;5;215m"),
            "216" : ("\033[38;5;216m", "\033[48;5;216m"),
            "217" : ("\033[38;5;217m", "\033[48;5;217m"),
            "218" : ("\033[38;5;218m", "\033[48;5;218m"),
            "219" : ("\033[38;5;219m", "\033[48;5;219m"),
            "220" : ("\033[38;5;220m", "\033[48;5;220m"),
            "221" : ("\033[38;5;221m", "\033[48;5;221m"),
            "222" : ("\033[38;5;222m", "\033[48;5;222m"),
            "223" : ("\033[38;5;223m", "\033[48;5;223m"),
            "224" : ("\033[38;5;224m", "\033[48;5;224m"),
            "225" : ("\033[38;5;225m", "\033[48;5;225m"),
            "226" : ("\033[38;5;226m", "\033[48;5;226m"),
            "227" : ("\033[38;5;227m", "\033[48;5;227m"),
            "228" : ("\033[38;5;228m", "\033[48;5;228m"),
            "229" : ("\033[38;5;229m", "\033[48;5;229m"),
            "230" : ("\033[38;5;230m", "\033[48;5;230m"),
            "231" : ("\033[38;5;231m", "\033[48;5;231m"),
            "232" : ("\033[38;5;232m", "\033[48;5;232m"), # BLACK AND WHITE FADE (END)
            "233" : ("\033[38;5;233m", "\033[48;5;233m"), # |
            "234" : ("\033[38;5;234m", "\033[48;5;234m"), # V
            "235" : ("\033[38;5;235m", "\033[48;5;235m"), #
            "236" : ("\033[38;5;236m", "\033[48;5;236m"), #
            "237" : ("\033[38;5;237m", "\033[48;5;237m"), #
            "238" : ("\033[38;5;238m", "\033[48;5;238m"), #
            "239" : ("\033[38;5;239m", "\033[48;5;239m"), #
            "240" : ("\033[38;5;240m", "\033[48;5;240m"), #
            "241" : ("\033[38;5;241m", "\033[48;5;241m"), #
            "242" : ("\033[38;5;242m", "\033[48;5;242m"), #
            "243" : ("\033[38;5;243m", "\033[48;5;243m"), #
            "244" : ("\033[38;5;244m", "\033[48;5;244m"), #
            "245" : ("\033[38;5;245m", "\033[48;5;245m"), #
            "246" : ("\033[38;5;246m", "\033[48;5;246m"), #
            "247" : ("\033[38;5;247m", "\033[48;5;247m"), #
            "248" : ("\033[38;5;248m", "\033[48;5;248m"), #
            "249" : ("\033[38;5;249m", "\033[48;5;249m"), #
            "250" : ("\033[38;5;250m", "\033[48;5;250m"), #
            "251" : ("\033[38;5;251m", "\033[48;5;251m"), #
            "252" : ("\033[38;5;252m", "\033[48;5;252m"), #
            "253" : ("\033[38;5;253m", "\033[48;5;253m"), # ^
            "254" : ("\033[38;5;254m", "\033[48;5;254m"), # |
            "255" : ("\033[38;5;255m", "\033[48;5;255m")  # BLACK AND WHITE FADE (START)
            }
        }
}

#SHOWS ALL AVAILABLE COLORS TO CHOSE FROM
def old_show_colors():
    bases = []
    brights = []
    l255 = []
    for color in YuiDB["colors"]["bases"]:
        bases.append(YuiDB["colors"]["bases"][color][0] + color + YuiDB["colors"]["bases"]["default"][0])
        bases.append(YuiDB["colors"]["bases"][color][1] + color + YuiDB["colors"]["bases"]["default"][1])

    for color in YuiDB["colors"]["brights"]:
        brights.append(YuiDB["colors"]["brights"][color][0] + color + YuiDB["colors"]["bases"]["default"][0])
        brights.append(YuiDB["colors"]["brights"][color][1] + color + YuiDB["colors"]["bases"]["default"][1])

    for color in YuiDB["colors"]["255"]:
        l255.append(YuiDB["colors"]["255"][color][0] + color + YuiDB["colors"]["bases"]["default"][0])
        l255.append(YuiDB["colors"]["255"][color][1] + color + YuiDB["colors"]["bases"]["default"][1])

    print("".join(bases))
    print("".join(brights))
    print("".join(l255))

def adjust_255(num):
    num = str(num)
    if len(num) == 2:
        return str("0"+num)
    elif len(num) == 1:
        return str("00"+num)
    else:
        return num

def show_bases_brights():
    bases = []
    brights = []
    leg = [False, False, False, False]
    for i in range(len(YuiDB["colors"]["bases"])-2):

        line = ""

        if leg[0] == False:
            line = line + "\t"
            line = line + "Foreground" + "\t\t" + "Background"
            line = line + "\n\t"
            line = line + " |        " + "\t\t" + " |        "
            line = line + "\n"
            leg[0] = True

        line = line + "\t"

        line = line + list(YuiDB["colors"]["bases"].values())[i][0] + list(YuiDB["colors"]["bases"].keys())[i] + YuiDB["colors"]["bases"]["default"][0] + "  "

        line = line + "    \t\t"
        line = line + list(YuiDB["colors"]["bases"].values())[i][1] + list(YuiDB["colors"]["bases"].keys())[i] + YuiDB["colors"]["bases"]["default"][1] + "  "
        line = line + "\n"
        bases.append(line)

    for i in range(len(YuiDB["colors"]["brights"])):

        line = ""

        if leg[0] == False:
            line = line + "\t"
            line = line + "Foreground" + "\t" + "Background"
            line = line + "\n\t"
            line = line + " |        " + "\t" + " |        "
            line = line + "\n"
            leg[0] = True

        line = line + "\t"

        line = line + list(YuiDB["colors"]["brights"].values())[i][0] + list(YuiDB["colors"]["brights"].keys())[i] + YuiDB["colors"]["bases"]["default"][0] + "  "

        line = line + "    \t"
        line = line + list(YuiDB["colors"]["brights"].values())[i][1] + list(YuiDB["colors"]["brights"].keys())[i] + YuiDB["colors"]["bases"]["default"][1] + "  "
        line = line + "\n"

        bases.append(line)
        # bases.append(YuiDB["colors"]["bases"][color][1] + color + YuiDB["colors"]["bases"]["default"][1])

    print("".join(bases))

    # for color in YuiDB["colors"]["brights"]:
    #     brights.append(YuiDB["colors"]["brights"][color][0] + color + YuiDB["colors"]["bases"]["default"][0])
    #     brights.append(YuiDB["colors"]["brights"][color][1] + color + YuiDB["colors"]["bases"]["default"][1])

def show_255():
    all = []
    leg = [False, False, False]
    legl = []
    for i in range(1, 25+1):
        if i < 1:
            continue
        line = ""

        if leg[0] == False:
            # line = line + "      " +f"{adjust_255(adjust_255(str((i*10)-9))[2])}" + " " + f"{adjust_255(adjust_255(str((i*10)-8))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-7))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-6))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-5))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-4))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-3))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-2))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-1))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-0))[2])}"
            # line = line + "   " +f"{adjust_255(adjust_255(str((i*10)-9))[2])}" + " " + f"{adjust_255(adjust_255(str((i*10)-8))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-7))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-6))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-5))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-4))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-3))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-2))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-1))[2])}"+ " " + f"{adjust_255(adjust_255(str((i*10)-0))[2])}"
            line = line + "\t       " +f"##{adjust_255(str((i*10)-9))[2]}" + " " + f"##{adjust_255(str((i*10)-8))[2]}"+ " " + f"##{adjust_255(str((i*10)-7))[2]}"+ " " + f"##{adjust_255(str((i*10)-6))[2]}"+ " " + f"##{adjust_255(str((i*10)-5))[2]}"+ " " + f"##{adjust_255(str((i*10)-4))[2]}"+ " " + f"##{adjust_255(str((i*10)-3))[2]}"+ " " + f"##{adjust_255(str((i*10)-2))[2]}"+ " " + f"##{adjust_255(str((i*10)-1))[2]}"+ " " + f"##{adjust_255(str((i*10)-0))[2]}"
            line = line + "  " +f"##{adjust_255(str((i*10)-9))[2]}" + " " + f"##{adjust_255(str((i*10)-8))[2]}"+ " " + f"##{adjust_255(str((i*10)-7))[2]}"+ " " + f"##{adjust_255(str((i*10)-6))[2]}"+ " " + f"##{adjust_255(str((i*10)-5))[2]}"+ " " + f"##{adjust_255(str((i*10)-4))[2]}"+ " " + f"##{adjust_255(str((i*10)-3))[2]}"+ " " + f"##{adjust_255(str((i*10)-2))[2]}"+ " " + f"##{adjust_255(str((i*10)-1))[2]}"+ " " + f"##{adjust_255(str((i*10)-0))[2]}"
            line = line + "\n"
            line = line + "\t       " +" | "+"  | "+"  | "+"  | "+"  | "+"  | "+"  | "+"  | "+"  | "+"  | "
            line = line + "  " + " | "+"  | "+"  | "+"  | "+"  | "+"  | "+"  | "+"  | "+"  | "+"  | "
            # line = line + "\n"
            # line = line + "       " +" V "+"  V "+"  V "+"  V "+"  V "+"  V "+"  V "+"  V "+"  V "+"  V "
            # line = line + "  " +" V "+"  V "+"  V "+"  V "+"  V "+"  V "+"  V "+"  V "+"  V "+"  V "
            line = line + "\n"
            leg[0] = True

        if leg[1] == False:
            line = line + f"\t{adjust_255(str((i*10)-9))[:2]}# -- "

        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-9][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-9]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-8][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-8]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-7][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-7]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-6][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-6]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-5][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-5]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-4][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-4]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-3][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-3]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-2][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-2]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-1][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-1]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line +(list(YuiDB["colors"]["255"].values())[(i*10)-0][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-0]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line + "\t"

        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-9][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-9]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-8][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-8]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-7][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-7]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-6][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-6]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-5][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-5]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-4][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-4]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-3][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-3]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-2][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-2]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-1][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-1]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i*10)-0][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i*10)-0]) + YuiDB["colors"]["bases"]["default"][1]) + " "


        line = line + "\n"
        all.append(line)
    for i in range(1, 5+1):
        if i > 1:
            continue
        line = ""
        if leg[2] == False:
            line = line + f"\t{adjust_255(str((i+250)))[:2]}# -- "
            leg[2] = True
        line = line + "\t" +(list(YuiDB["colors"]["255"].values())[(i+250)][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line + "" +(list(YuiDB["colors"]["255"].values())[(i+250)+1][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)+1]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line + "" +(list(YuiDB["colors"]["255"].values())[(i+250)+2][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)+2]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line + "" +(list(YuiDB["colors"]["255"].values())[(i+250)+3][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)+3]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line + "" +(list(YuiDB["colors"]["255"].values())[(i+250)+4][0] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)+4]) + YuiDB["colors"]["bases"]["default"][0]) + " "
        line = line + "\t\t\t"

        line = line + (list(YuiDB["colors"]["255"].values())[(i+250)][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i+250)+1][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)+1]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i+250)+2][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)+2]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i+250)+3][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)+3]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        line = line + (list(YuiDB["colors"]["255"].values())[(i+250)+4][1] + adjust_255(list(YuiDB["colors"]["255"].keys())[(i+250)+4]) + YuiDB["colors"]["bases"]["default"][1]) + " "
        all.append(line)
    print("".join(all))

def show_colors():
    show_bases_brights()
    show_255()

def bold(line): # RETURN THE STRING IN BOLD
    return (YuiDB['fonts']["bold"][0] + line + YuiDB["fonts"]["bold"][1])

def dim(line): # RETURN THE STRING IN DIM
    return (YuiDB['fonts']["dim"][0] + line + YuiDB["fonts"]["dim"][1])

def underline(line): #RETURN THE STRING UNDERLINED
    return (YuiDB['fonts']["underline"][0] + line + YuiDB["fonts"]["underline"][1])

def inverse(line): #RETURN THE NEGATIVE OF A STRING, FORE BECAME BACK AND VICEVERSA
    return (YuiDB['fonts']["inverse"][0] + line + YuiDB["fonts"]["inverse"][1])

def fore(line, color:str): # COLOR THE FORE OF THE STRING OF THE GIVEN COLOR
    if color in YuiDB["colors"]["bases"]:
        return(YuiDB["colors"]["bases"][color][0] + line + YuiDB["colors"]["bases"]["default"][0])
    elif color in YuiDB["colors"]["brights"]:
        return(YuiDB["colors"]["brights"][color][0] + line + YuiDB["colors"]["bases"]["default"][0])
    elif color in YuiDB["colors"]["255"]:
        return(YuiDB["colors"]["255"][color][0] + line + YuiDB["colors"]["bases"]["default"][0])

def back(line, color:str): # COLOR THE BACK OF THE STRING OF THE GIVEN COLOR
    if color in YuiDB["colors"]["bases"]:
        return(YuiDB["colors"]["bases"][color][1] + line + YuiDB["colors"]["bases"]["default"][1])
    elif color in YuiDB["colors"]["brights"]:
        return(YuiDB["colors"]["brights"][color][1] + line + YuiDB["colors"]["bases"]["default"][1])
    elif color in YuiDB["colors"]["255"]:
        return(YuiDB["colors"]["255"][color][1] + line + YuiDB["colors"]["bases"]["default"][1])

def real_len(text): # RETURN THE REAL LENGTH OF A STRING THAT HAS BEEN CHANGED WITH ESCAPES
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    clean_text = ansi_escape.sub('', text)
    return len(clean_text)

def real_text(text): # RETURN THE ORIGINAL STRING OF A STRING THAT HAS BEEN CHANGED WITH ESCAPES
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', text)

def brush(fore:str=None, back:str=None):
    ret = ""

    if fore in YuiDB["colors"]["bases"]:
        ret = ret + (YuiDB["colors"]["bases"][fore][0])
    elif fore in YuiDB["colors"]["brights"]:
        ret = ret + (YuiDB["colors"]["brights"][fore][0])
    elif fore in YuiDB["colors"]["255"]:
        ret = ret + (YuiDB["colors"]["255"][fore][0])

    if back in YuiDB["colors"]["bases"]:
        ret = ret + (YuiDB["colors"]["bases"][back][1])
    elif back in YuiDB["colors"]["brights"]:
        ret = ret + (YuiDB["colors"]["brights"][back][1])
    elif back in YuiDB["colors"]["255"]:
        ret = ret + (YuiDB["colors"]["255"][back][1])
    return ret
