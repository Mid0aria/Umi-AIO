import os,colorama

colorama.init(convert=True)

os.system("title Umi AIO")
os.system("cls")

print(colorama.Fore.GREEN + "\n[1] Bot Modules" + colorama.Fore.RED + "\n[2] SmsBomb Modules")
moduleinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))

#Bot Modules
if moduleinput == 1: 
    os.system("cls")
    print(colorama.Fore.GREEN + "\n[1] Spotify" + colorama.Fore.MAGENTA + "\n[2] Twitch"+ colorama.Fore.RESET +"(Viewer)")
    botinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))
#BOT Inputs
    if botinput == 1:
        os.system("cls")
        from Modules.BOT.spotify.spotify import *
    if botinput == 2:
        os.system("cls")
        from Modules.BOT.twitchviewer.twitch import *
    
    
#SMS Modules
if moduleinput == 2:
    os.system("cls")
    print(colorama.Fore.GREEN + "\n[1] SMSBomberTR(Proxyless, Turkey)")
    smsinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))  
#SMS Inputs    
    if smsinput == 1:
        os.system("cls")
        from Modules.SMS.smsbomberesu.smsbomberturkey import *    