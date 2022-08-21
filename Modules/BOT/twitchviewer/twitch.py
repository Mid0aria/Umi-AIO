try:
    import os, requests, colorama, threading, time, urllib
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")
    exit()

colorama.init(convert=True)    

lock = threading.Lock()
counter = 0
errorcounter = 0
proxyfilelines = 0
proxies = []
proxy_counter = 0
modulename = "TwitchViewer"
moduleowner = "ESU"


class twitchviewerbyesu:
    def __init__(self, twitchlink, proxytype = None, proxy = None):
        self.proxy = proxy
        self.proxytype = proxytype
        self.twitchlink = twitchlink

    def viewer(self):
        if "/twitch.tv/" in self.twitchlink:
            self.twitchlink = self.twitchlink.split("/twitch.tv/")[1]
        if "?" in self.twitchlink:
            self.twitchlink = self.twitchlink.split("?")[0]
            print(self.twitchlink)    
            if self.proxy == None:
                return None, f"unable to send request on register"
            return None, f"bad proxy on register {self.proxy}"    
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}            
        try:
            requests.get("https://www.twitch.tv/"+ self.twitchlink, proxies = proxies)    
            return True, "viewer sended"
        except:
            return False, "while sending"        
    
    
    
os.system(f"title {modulename} by {moduleowner}")  
 
twitchlink = input(colorama.Fore.RESET + f"\n[{modulename}] Enter Link > ")
threads = int(input(f"\n[{modulename}] Threads > "))
print("\n[1] Proxies\n[2] Get Free Proxies(Maybe you get bad proxies)\n[3] Proxyless")
proxyinput = int(input(f"\n[${modulename}] Select Preference > "))

if proxyinput == 1:
    print("\n[1] Http\n[2] Socks4\n[3] Socks5")
    proxytype = int(input(f"\n[${modulename}] Select Proxy Type > "))
if proxyinput == 2:
    print("\n[1] Http\n[2] Socks4\n[3] Socks5")
    proxytype = int(input(f"\n[${modulename}] Select Proxy Type > "))    
os.system("cls")

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../../../proxies.txt"
proxiesdir = os.path.join(script_dir, rel_path)
           
def load_proxies():
        global proxyfilelines
        if not os.path.exists(proxiesdir):
            print(colorama.Fore.YELLOW + "\nFile proxies.txt not found")
            time.sleep(5)
            os._exit(0)
        with open(proxiesdir, "r", encoding = "UTF-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                proxyfilelines = len(proxies)
                proxyfilelines += 1
                proxies.append(line)            
            if not len(proxies):
                print(colorama.Fore.YELLOW + "\nNo proxies loaded in proxies.txt")
                time.sleep(5)
                os._exit(0)
    

def getfreeproxy():
    if proxytype == 1:
       # HTTP Proxies
       urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", proxiesdir)
    if proxytype == 2:
       # Socks4 Proxies
       urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all", proxiesdir)
    if proxytype == 3:           
       # Socks5 Proxies
       urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all", proxiesdir)

if proxyinput == 2:
        getfreeproxy()
        time.sleep(1)
        load_proxies()

if proxyinput == 1:
        load_proxies()

def safe_print(arg):
        lock.acquire()
        print(arg)
        lock.release()

def count():
        os.system(f'title [{modulename} by {moduleowner}] Sended = {counter} / Error = {errorcounter} / Proxy = {proxyfilelines}')

def thread_starter():
        global counter, errorcounter
        if proxyinput == 1:
            obj = twitchviewerbyesu(twitchlink, proxytype, proxies[proxy_counter])
        if proxyinput == 2:
            obj = twitchviewerbyesu(twitchlink, proxytype, proxies[proxy_counter])
        else:
            obj = twitchviewerbyesu(twitchlink)
        result, message = obj.viewer()
        if result == True:
            counter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.GREEN + message)
            count()
        else:
            errorcounter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.RED + f"Error {message}")
            count()
            
while True:
        if threading.active_count() <= threads:
            try:
                threading.Thread(target = thread_starter).start()
                proxy_counter += 1
            except:
                pass
            if len(proxies) <= proxy_counter: #Loops through proxy file
                proxy_counter = 0