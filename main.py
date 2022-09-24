import os,colorama
try:
    import httplib
except:
    import http.client as httplib

colorama.init(convert=True)

def connection():
    conn = httplib.HTTPConnection("www.google.com", timeout=3)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        return False

if (connection() == False):
	if(os.name == "nt"):
		os.system("cls")
	print(colorama.Fore.RED + "You do not have an internet connection!!!" + colorama.Fore.WHITE)
	os._exit(1)


if (os.name =="nt"):
    os.system("title Umi AIO")
    os.system("cls")

print(colorama.Fore.GREEN + "[1] Bot Modules"+ colorama.Fore.MAGENTA + "\n[2] SmsBomb Modules"+ colorama.Fore.YELLOW + "\n[3] Generator Modules" + colorama.Fore.RED + "\n[4] Checker Modules" + colorama.Fore.BLUE + "\n[5] Bypass Modules")
moduleinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))

#Bot Modules
if moduleinput == 1:
    if (os.name =="nt"):
        os.system("title Umi AIO / Bot Modules")
        os.system("cls")
    print(colorama.Fore.GREEN + "[1] Spotify" + colorama.Fore.RESET + "(User&Playlist Follower)" + colorama.Fore.GREEN + "\n[2] Twitch"+ colorama.Fore.RESET +"(Viewer)")
    botinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))
#BOT Inputs
    if botinput == 1:
        if (os.name =="nt"):
            os.system("cls")
        from Modules.Bot.spotify.spotify import *
    if botinput == 2:
        if (os.name =="nt"):
            os.system("cls")
        from Modules.Bot.twitchviewer.twitch import *
        

#SMS Modules
if moduleinput == 2:
    if (os.name =="nt"):
        os.system("title Umi AIO / SmsBomb Modules")
        os.system("cls")
    print(colorama.Fore.MAGENTA + "[1] SMSBomberTR(Proxyless, Turkey)")
    smsinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))  
#SMS Inputs    
    if smsinput == 1:
        if (os.name =="nt"):
            os.system("cls")
        from Modules.SMS.smsbomberesu.smsbomberturkey import *    
        
#Generator Modules

if moduleinput == 3:
    if (os.name =="nt"):
        os.system("title Umi AIO / Generator Modules")
        os.system("cls")
    print(colorama.Fore.YELLOW+ "[1] MubiCodeGenerator")
    generatorinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))  
#Generator Inputs    
    if generatorinput == 1:
        if (os.name =="nt"):
            os.system("cls")
        from Modules.Generator.mubicode.mubicodegenerator import *    

#Checker Modules
if moduleinput == 4:
    if (os.name =="nt"):
        os.system("title Umi AIO / Checker Modules")
        os.system("cls")
    print(colorama.Fore.RED + "[1] Blutv"+ colorama.Fore.RESET +"(MailPass, Need Proxies, Web API)" + colorama.Fore.RED + "\n[2] Blutv" + colorama.Fore.RESET + "(MailPass, Need Proxies, SmartTv API)")
    checkerinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))  
#Checker Inputs    
    if checkerinput == 1:
        if (os.name =="nt"):
            os.system("cls")
        from Modules.Checker.blutv.blutv import *   
    if checkerinput == 2:
        if (os.name =="nt"):
            os.system("cls")
        from Modules.Checker.blutv.blusmart import *
        
#Bypass Modules
if moduleinput == 5:
    if (os.name =="nt"):
        os.system("title Umi AIO / Bypass Modules")
        os.system("cls")
    print(colorama.Fore.BLUE + "[1] TrLink(If you have ipv6 you need vpn)")
    bypassinput = int(input(colorama.Fore.RESET + "\n[Umi AIO] Select Module > "))  
#Bypass Inputs    
    if bypassinput == 1:
        if (os.name =="nt"):
            os.system("cls")
        from Modules.Bypass.trlink.trlinkbypass import *    
