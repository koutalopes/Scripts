#!/usr/bin/env python3
# -*- coding: utf-8 -*-

    # deadbeef "now playing" para o weechat
    # Ricardo Lopes (Kouta_Kun)
    #
    # v0.2

# Importar bibliotecas
import subprocess
import weechat as w

# Informações de registro do script
SCRIPT_NAME     = "dbnp"
SCRIPT_AUTHOR   = "Kouta_Kun"
SCRIPT_VERSION  = "0.2"
SCRIPT_LICENSE  = "Copyleft"
SCRIPT_DESC = "Now playing for deadbeef"

def pbar(progress):
    barLength = 14 # Modify this to change the length of the progress bar
    status = ""

    if isinstance(progress, int):
        progress = float(progress)

    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"

    block = int(round(barLength*(progress/100)))
    text = "[{0}]".format( "#"*block + "-"*(barLength-block))

    return text

def obr(path):
    cmd = "mediainfo"
    args = "--Output=General;%OverallBitRate/String%"
    o = subprocess.check_output([cmd, args, path]).decode("UTF-8")

    if len(o.split()) == 3:
        if o.split()[2] == "Mbps":
           obr = "~" + o.split()[0] + o.split()[1] + " Mb/s"
        else:
            obr = "~" + o.split()[0] + o.split()[1] + " Kb/s"
    elif len(o.split()) == 2:
        if o.split()[1] == "Mbps":
            obr = "~" + o.split()[0] + " Mb/s"
        else:
            obr = "~" + o.split()[0] + " Kb/s"

    return obr

def fsize(path):
    cmd = "mediainfo"
    args = "--Output=General;%FileSize/String%"
    s = subprocess.check_output([cmd, args, path]).decode("UTF-8")

    if s.split()[1] == "GiB":
        size = s.split()[0] + " Gb"
    elif s.split()[1] == "MiB":
        size = s.split()[0] + " Mb"
    else:
        size = s

    return size

def getinfos ():
    cmd = "deadbeef"
    args = "--nowplaying-tf"
    fmt = "%artist%|%title%|%playback_time%|%playback_time_seconds%|%length%|%length_seconds%|%codec%|%_deadbeef_version%|%path%|%isplaying%"

    raw = subprocess.Popen([cmd, args, fmt], stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE,
                                             stdin=subprocess.PIPE)
    info, err = raw.communicate()

    return info

def msg ():
    s = getinfos()

    artist = s.split("|")[0]
    title = s.split("|")[1]
    timepos = s.split("|")[2]
    timepossec = s.split("|")[3]
    duration = s.split("|")[4]
    durationsec = s.split("|")[5]
    codec = s.split("|")[6]
    version = s.split("|")[7]
    path = s.split("|")[8]

    percent = int(round((float(timepossec) / float(durationsec)) * 100, -1))

    msg = "DeaDBeeF {} [ {} - {} |{}| {}/{} | {} | {} | {} ] ".format(version,
                                                                      artist,
                                                                      title,
                                                                      pbar(percent),
                                                                      timepos,
                                                                      duration,
                                                                      fsize(path),
                                                                      obr(path),
                                                                      codec)
    return msg

# mostrar info
def dbnp(world, world_eol, userdata):
    ison = getinfos()
    if ison.split("|")[9] != "1":
        w.prnt(w.current_buffer(), "DeadDBeeF is not playing")
    else:
        w.command(w.current_buffer(), msg())

    return w.WEECHAT_RC_OK

# registro
w.register(SCRIPT_NAME,
           SCRIPT_AUTHOR,
           SCRIPT_VERSION,
           SCRIPT_LICENSE,
           SCRIPT_DESC,
           ' ', ' ')

# comando
w.hook_command("dbnp", "Now Playing", "", "/dbnp", "", "dbnp", "")
