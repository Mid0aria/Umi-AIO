try:
    import os, requests, colorama, threading, time, urllib
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
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


class twitchviewerbyesu:
    def __init__(self, twitchlink, proxy = None):
        self.proxy = proxy
        self.twitchlink = twitchlink

    def viewer(self):
        if "/twitch.tv/" in self.twitchlink:
            self.twitchlink = self.twitchlink.split("/twitch.tv/")[1]
        if "?" in self.twitchlink:
            self.twitchlink = self.twitchlink.split("?")[0]
            if self.proxy == None:
                return None, f"unable to send request on register"
            return None, f"bad proxy on register {self.proxy}"                    
        try:
            requests.get("https://www.twitch.tv/"+ self.twitchlink, proxies = proxies)    
            return True
        except:
            return False, "while sending"


os.system("title TwitchViewer by ESU")   
    
twitchlink = input(colorama.Fore.RESET + "\n[TwitchViewer] Enter Twitch Link > ")
threads = int(input("\n[TwitchViewer] Threads: "))
print("\n[1] Proxies\n[2] Get Free Proxies(Maybe you get bad proxies)\n")
proxyinput = int(input("\nSelect Proxy Preference > "))
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
       # HTTP Proxies
       urllib.request.urlretrieve("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", proxiesdir)
       # Socks4 Proxies
       with urllib.request.urlopen("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all") as response:
           socks4data = response.read().decode("utf-8")
           with open(proxiesdir, "a+") as fp: fp.write(str(socks4data))
       # Socks5 Proxies
       with urllib.request.urlopen("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all") as response:
           socks5data = response.read().decode("utf-8")
           with open(proxiesdir, "a+") as fp : fp.write(str(socks5data))
       # Remove Blank Lines    
       with open(proxiesdir, "a+", encoding = "UTF-8") as f:
           for line in f:
             if not line.isspace():  
                 f.write(line)

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
        os.system(f'title [TwitchViewer by ESU] Sended = {counter} / Error = {errorcounter} / Proxy = {proxyfilelines}')

def thread_starter():
        global counter, errorcounter
        if proxyinput == 1:
            obj = twitchviewerbyesu(twitchlink, proxies[proxy_counter])
        if proxyinput == 2:
            obj = twitchviewerbyesu(twitchlink, proxies[proxy_counter])
        else:
            exit()
        result, message = obj.viewer()
        if result == True:
            counter += 1
            safe_print(colorama.Fore.MAGENTA + "[TwitchViewer] " + colorama.Fore.GREEN + f"Viewer Sended [{message}]")
            count()
        else:
            errorcounter += 1
            safe_print(colorama.Fore.MAGENTA + "[TwitchViewer] " + colorama.Fore.RED + f"Error {message}")
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