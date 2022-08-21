try:
    import os, requests, colorama, threading, time, urllib, random
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
modulename = "MubiCodeGenerator"
moduleowner = "ESU"


class mubicodegeneratorbyesu:
    def __init__(self, proxytype = None, proxy = None):
        self.proxy = proxy
        self.proxytype = proxytype

    def codegen(self, len):
        gen = ''.join((random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(len)))
        return gen      
    
            
    def generator(self): # your loop function
        code = "FZG4NZ"
        # code = self.codegen(6)
        if code == None:
            return None, "while calling codegen"
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}
        try:
            r = requests.get("https://mubi.com/services/api/special_promos/" + code)        
            if 'campaign":"' in r.text:
                script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
                rel_path = "../../../mubicodegenerated.txt"
                mubicodedir = os.path.join(script_dir, rel_path)                
                with open(mubicodedir, "a") as f:
                    f.write("Code: " + code + " Campaign: " + r.json()["campaign"] + " Type: " + r.json()["type"] + " Code Description: "+ r.json()["plain_text"] + "\n")                
                return True, "Code Generated > " + code
            if r.status_code(404):
                return None, "while generating, code is not valid"
            if 'Retry later' in r.text:
                return None, "while generating, ratelimit"
        except:
            return None, "while generating"    
    
    
    
os.system(f"title {modulename} by {moduleowner}")   

threads = int(input(f"\n[{modulename}] Threads > "))
print("\n[1] Proxies\n[2] Get Free Proxies(Maybe you get bad proxies)")
proxyinput = int(input(f"\n[{modulename}] Select Preference > "))

if proxyinput == 1:
    print("\n[1] Http\n[2] Socks4\n[3] Socks5")
    proxytype = int(input(f"\n[{modulename}] Select Proxy Type > "))
if proxyinput == 2:
    print("\n[1] Http\n[2] Socks4\n[3] Socks5")
    proxytype = int(input(f"\n[{modulename}] Select Proxy Type > "))    
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
        os.system(f'title [{modulename} by {moduleowner}] Generated = {counter} / Error = {errorcounter} / Proxy = {proxyfilelines}')

def thread_starter():
        global counter, errorcounter
        if proxyinput == 1:
            obj = mubicodegeneratorbyesu(proxytype, proxies[proxy_counter])
        if proxyinput == 2:
            obj = mubicodegeneratorbyesu(proxytype, proxies[proxy_counter])
        else:
            obj = mubicodegeneratorbyesu()
        result, message = obj.generator() # examplemodule2 The name of your module's function that will enter the thread
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