# -*- coding: utf-8 -*-

## Spotify "now playing"

# Importar bibliotecas
import subprocess
import weechat as w

# Informações de registro do script
SCRIPT_NAME	= "spnp"
SCRIPT_AUTHOR = "Kouta_Kun"
SCRIPT_VERSION	= "0.0.1"
SCRIPT_LICENSE	= "Copyleft"
SCRIPT_DESC	= "Spotify Now playing"

def getInfos():
    infos = subprocess.check_output(["sp", "metadata"]).decode("UTF-8")

    album = infos.splitlines()[3].strip("album|")
    title = infos.splitlines()[8].strip("title|")
    artist = infos.splitlines()[5].strip("artist|")

    msg = "spotify [{} | {} | {}]".format(artist,
                                          album,
                                          title)

    return msg

def saida(world, world_eol, userdata):
    try:
        w.command(w.current_buffer(), getInfos())
    except:
        
        w.prnt(w.current_buffer(), "Spotify não está sendo executado!")

    return w.WEECHAT_RC_OK

# Registro do Script
w.register(SCRIPT_NAME,
 		   SCRIPT_AUTHOR,
 		   SCRIPT_VERSION,
 		   SCRIPT_LICENSE,
 		   SCRIPT_DESC,
 		   ' ', ' ')

# Comando
w.hook_command("spnp", "Now Playing", "", "/spnp", "", "saida", "")