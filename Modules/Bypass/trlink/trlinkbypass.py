try:
    import os, requests, colorama, time, urllib.request
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")
    exit()

colorama.init(convert=True)    

modulename = "TrLink Bypass"
moduleowner = "ESU"


class trlinkbypass:
    def __init__(self, link):
        
        if "https://" in link:
            link = link.split("https://")[1]
        if "http://" in link:
            link = link.split("http://")[1]            
        self.link = link.split("/")[1]        

    def fget(self):
            r = urllib.request.urlopen("https://aylink.co/"+ self.link).read().decode('utf-8')
            if 'BT19X' in r:
                return None
            else:
                a = r.split("let _a = '")[1].split("',")[0]
                t = r.split("_t = '")[1].split("',")[0]
                d = r.split("_d = '")[1].split("'")[0]
                return a, t, d

    def tk(self, a, t, d):
        headers = {
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest"
        }
        r = requests.post("https://aylink.co/get/tk", data = "_a={}&_t={}&_d={}".format(a,t,d), headers = headers)
        if 'status":true' in r.text:
            return r.text.split('th":"')[1].split('"')[0]
        else:
            return None

    def go2(self, link, th):
        headers = {
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest"
        }
        r = requests.post("https://aylink.co/links/go2", data = "alias={}&csrf=&tkn={}".format(link, th), headers = headers)
        return r.text.split('url":"')[1].split('"')[0]
 
        
    def bypass(self):
        a, t, d = self.fget()
        if self.fget() == None:
            return None, "VPN Detected"
        th = self.tk(a,t,d)               
        if th == None:
            return None, "link cannot be bypassed"      
        euurl = self.go2(self.link, th)
        return True, "Link: " + euurl
    
    
def starter():
        obj = trlinkbypass(link)
        result, message = obj.bypass()
        if result == True:
            print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.GREEN + message + colorama.Fore.RESET)
        else:
            print(colorama.Fore.MAGENTA + f"[{modulename}] " + colorama.Fore.RED + f"Error {message}" + colorama.Fore.RESET)
        
os.system(f"title {modulename} by {moduleowner}")   
link = str(input(f"[{modulename}] Link > "))

starter()