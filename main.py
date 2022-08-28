import os,colorama

colorama.init(convert=True)

os.system("title Umi AIO")
os.system("cls")

print(colorama.Fore.GREEN + "[1] Bot Modules"+ colorama.Fore.MAGENTA + "\n[2] SmsBomb Modules"+ colorama.Fore.YELLOW + "\n[3] Generator Modules" + colorama.Fore.RED )#+ "\n[4] Checker Modules")
moduleinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))

#Bot Modules
if moduleinput == 1: 
    os.system("cls")
    print(colorama.Fore.GREEN + "[1] Spotify" + colorama.Fore.RESET + "(User&Playlist Follower)" + colorama.Fore.MAGENTA + "\n[2] Twitch"+ colorama.Fore.RESET +"(Viewer)")
    botinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))
#BOT Inputs
    if botinput == 1:
        os.system("cls")
        from Modules.Bot.spotify.spotify import *
    if botinput == 2:
        os.system("cls")
        from Modules.Bot.twitchviewer.twitch import *
        

#SMS Modules
if moduleinput == 2:
    os.system("cls")
    print(colorama.Fore.GREEN + "[1] SMSBomberTR(Proxyless, Turkey)")
    smsinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))  
#SMS Inputs    
    if smsinput == 1:
        os.system("cls")
        from Modules.SMS.smsbomberesu.smsbomberturkey import *    
        
#Generator Modules
if moduleinput == 3:
    os.system("cls")
    print(colorama.Fore.GREEN + "[1] MubiCodeGenerator")
    generatorinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))  
#Generator Inputs    
    if generatorinput == 1:
        os.system("cls")
        from Modules.Generator.mubicode.mubicodegenerator import *    


        
        