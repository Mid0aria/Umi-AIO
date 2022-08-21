import threading, os, time, urllib, colorama, requests, random, string, names, datetime
colorama.init(convert=True)

lock = threading.Lock()
counter = 0
errorcounter = 0
proxyfilelines = 0
proxies = []
proxy_counter = 0
modulename = "Spotify"
moduleowner = "ESU"

class spotifyuserfollow:

    def __init__(self, profile, proxytype = None, proxy = None):
        self.session = requests.Session()
        self.profile = profile
        self.proxy = proxy
        self.proxytype = proxytype
    
    def register_account(self):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.spotify.com/"
        }
        email = ("").join(random.choices(string.ascii_letters + string.digits, k = 8)) + "@gmail.com"
        password = ("").join(random.choices(string.ascii_letters + string.digits, k = 8))
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}
        data = f"birth_day=1&birth_month=01&birth_year=1970&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname={names.get_full_name()}&email={email}&gender=neutral&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={password}&password_repeat={password}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0"
        try:
            create = self.session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers = headers, data = data, proxies = proxies)
            if "login_token" in create.text:
                login_token = create.json()['login_token']
                return login_token
            else:
                return None
        except:
            return False

    def get_csrf_token(self):
        try:
            r = self.session.get("https://www.spotify.com/uk/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1")
            return r.text.split('csrfToken":"')[1].split('"')[0]
        except:
            return None
        
    def get_token(self, login_token):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRF-Token": self.get_csrf_token(),
            "Host": "www.spotify.com"
        }
        self.session.post("https://www.spotify.com/api/signup/authenticate", headers = headers, data = "splot=" + login_token)
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Spotify/1.1.91.824 Safari/537.36",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "app-platform": "Windows",
            "Host": "open.spotify.com",
            "Referer": "https://open.spotify.com/"
        }
        try:
            r = self.session.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers = headers
            )
            return r.json()["accessToken"]
        except:
            return None

    def follow(self):
        if "/user/" in self.profile:
            self.profile = self.profile.split("/user/")[1]
        if "?" in self.profile:
            self.profile = self.profile.split("?")[0]
        login_token = self.register_account()
        if login_token == None:
            return None, "while registering, ratelimit"
        elif login_token == False:
            if self.proxy == None:
                return None, f"unable to send request on register"
            return None, f"bad proxy on register {self.proxy}"
        auth_token = self.get_token(login_token)
        if auth_token == None:
            return None, "while getting auth token"
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Spotify/1.1.91.824 Safari/537.36",
            "app-platform": "Windows",
            "Referer": "https://open.spotify.com/",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "authorization": "Bearer {}".format(auth_token),
        }
        try:
            self.session.put(
                "https://api.spotify.com/v1/me/following?type=user&ids=" + self.profile,
                headers = headers
            )
            return True, None
        except:
            return False, "while following"
        
"""
class spotifyplaylistfollow:

    def __init__(self, playlist, proxytype, proxy = None):
        self.session = requests.Session()
        self.playlist = playlist
        self.proxy = proxy
        self.proxytype = proxytype
    
    def register_account(self):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.spotify.com/"
        }
        email = ("").join(random.choices(string.ascii_letters + string.digits, k = 8)) + "@gmail.com"
        password = ("").join(random.choices(string.ascii_letters + string.digits, k = 8))
        proxies = None
        proxies = None
        if self.proxy != None:
            if self.proxytype == 1:
                proxies = {"http": f"http://{self.proxy}","https": f"http://{self.proxy}"}
            if self.proxytype == 2:
                proxies = {"http": f"socks4://{self.proxy}","https": f"socks4://{self.proxy}"}
            if self.proxytype == 3:
                proxies = {"http": f"socks5://{self.proxy}","https": f"socks5://{self.proxy}"}
        data = f"birth_day=1&birth_month=01&birth_year=1970&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname={names.get_full_name()}&email={email}&gender=neutral&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={password}&password_repeat={password}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0"
        try:
            create = self.session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers = headers, data = data, proxies = proxies)
            if "login_token" in create.text:
                login_token = create.json()['login_token']
                with open("Created.txt", "a") as f:
                    f.write(f'{email}:{password}:{login_token}\n')
                return login_token
            else:
                return None
        except:
            return False

    def get_csrf_token(self):
        try:
            r = self.session.get("https://www.spotify.com/uk/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1")
            return r.text.split('csrfToken":"')[1].split('"')[0]
        except:
            return None
        
    def get_token(self, login_token):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRF-Token": self.get_csrf_token(),
            "Host": "www.spotify.com"
        }
        self.session.post("https://www.spotify.com/api/signup/authenticate", headers = headers, data = "splot=" + login_token)
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Spotify/1.1.91.824 Safari/537.36",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "app-platform": "Windows",
            "Host": "open.spotify.com",
            "Referer": "https://open.spotify.com/"
        }
        try:
            r = self.session.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers = headers
            )
            return r.json()["accessToken"]
        except:
            return None

    def get_userid(self, access_token):          
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Spotify/1.1.91.824 Safari/537.36",
            "app-platform": "Windows",
            "Referer": "https://open.spotify.com/",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "authorization": "Bearer {}".format(access_token),
        }
        try:
            r = self.session.get(
                "https://api.spotify.com/v1/me",
                headers = headers
            )
            return r.json()["id"]
        except:
            return None
        
    def gaboservicepublic(self):
        headers = {
            "content-type": "application/json"
        }
        data = {"suppress_persist":"false","events":[{"sequence_id":"POlihn5z6/Q88FryU2cmCA==","sequence_number":2,"event_name":"EventSenderStats2NonAuth","fragments":{"context_sdk":{"version_name":"2.2.1","type":"javascript"},"context_time":{"timestamp":1660835471100},"context_client_id":{"value":"2KXtlY0nTC6O5xfmpLCXHQ=="},"context_application":{"version":"web-player_2022-08-18_1660829058823_1a7e931"},"context_user_agent":{"value":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"},"context_correlation_id":{"value":"042be736-9481-4dcd-a10d-4cd56d2b38b4"},"message":{"sequence_ids":["POlihn5z6/Q88FryU2cmCA=="],"event_names":["ConfigurationApplied","EventSenderStats2NonAuth","KmPageView","UbiExpr2PageView","UbiProd1Impression","UbiProd1Interaction","KmInteraction"],"loss_stats_num_entries_per_sequence_id":[7],"loss_stats_event_name_index":[0,1,2,3,4,5,6],"loss_stats_storage_sizes":[0,0,0,0,0,1,0],"loss_stats_sequence_number_mins":[2,2,2,2,3,2,2],"loss_stats_sequence_number_nexts":[2,2,2,2,3,3,2]}}}]}
        
        try:
            r = self.session.post("https://gew4-spclient.spotify.com/gabo-receiver-service/public/v3/events", headers = headers, json = data)
            print(r.text())
        except:
            return False, "GRSP not responding"           
    def gaboservice(self, access_token):
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "tr",
            "app-platform": "WebPlayer",
            "authorization": "Bearer {}".format(access_token),
            "content-length": "1571",
            "content-type": "application/json",
            "origin": "https://open.spotify.com",
            "referer": "https://open.spotify.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "spotify-app-version": "1.1.93.174.gd2981e5f"
        }
        data = {
  "suppress_persist": "false",
  "events": [
    {
      "sequence_id": "W5Cx4r+WMW2RNBSPmrB3AQ==",
      "sequence_number": 5,
      "event_name": "UbiProd1Interaction",
      "fragments": {
        "context_sdk": {
          "version_name": "2.2.1",
          "type": "javascript"
        },
        "context_time": {
          "timestamp": 1660665294650
        },
        "context_client_id": {
          "value": "2KXtlY0nTC6O5xfmpLCXHQ=="
        },
        "context_application": {
          "version": "web-player_2022-08-16_1660663149285_f738f16"
        },
        "context_user_agent": {
          "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"
        },
        "context_correlation_id": {
          "value": "6bae7cce-eab8-4360-95ca-bfca477f8ff9"
        },
        "message": {
          "action_parameter_names": [
            "item_to_be_liked"
          ],
          "action_parameter_values": [
            "spotify:playlist:" + self.playlist
          ],
          "action_name": "like",
          "action_version": "1",
          "annotator_configuration_version": "",
          "annotator_version": "",
          "app": "music",
          "element_path_ids": [
            "",
            "",
            ""
          ],
          "element_path_names": [
            "desktop-playlist",
            "action_bar",
            "heart_button"
          ],
          "element_path_pos": [
            "",
            "",
            ""
          ],
          "element_path_reasons": [
            "",
            "",
            ""
          ],
          "element_path_uris": [
            "spotify:playlist:" + self.playlist,
            "",
            ""
          ],
          "generator_version": "9.4.13",
          "interaction_id": "49e9393b-8184-401d-b8d3-b485e33348f7",
          "interaction_type": "hit",
          "parent_modes": [],
          "parent_path_ids": [],
          "parent_path_names": [],
          "parent_path_pos": [],
          "parent_path_reasons": [],
          "parent_path_uris": [],
          "parent_specification_versions": [],
          "specification_version": "2.0.0",
          "specification_mode": "default",
          "page_instance_id": "6962e61d-82ca-4cd9-b959-2c14f4b65383",
          "playback_id": "null",
          "play_context_uri": "spotify:station:playlist:2BTNm0QrzDKwo9eGnw0Aag"
        }
      }
    }
  ]
}
        try:
            r = self.session.post(
                "https://gew4-spclient.spotify.com/gabo-receiver-service/v3/events",
                headers = headers,
                json = data
            )
            print(r.text())
            if not "reason" in r.text():
                return print(colorama.Fore.RESET + "GRS Accepted")
        except:
            return False, "GRS not responding!"



    def follow(self):
        if "/playlist/" in self.playlist:
            self.playlist = self.playlist.split("/playlist/")[1]
        if "?" in self.playlist:
            self.playlist = self.playlist.split("?")[0]
        login_token = self.register_account()
        if login_token == None:
            return None, "while registering, ratelimit"
        elif login_token == False:
            if self.proxy == None:
                return None, f"unable to send request on register"
            return None, f"bad proxy on register {self.proxy}"
        auth_token = self.get_token(login_token)
        if auth_token == None:
            return None, "while getting auth token"
        user_id = self.get_userid(auth_token)
        if user_id == None:
            return None, "while getting userid"
        dt = datetime.datetime.now()    
        time_stamp = datetime.datetime.timestamp(dt)    

        headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "tr",
            "app-platform": "WebPlayer",
            "authorization": "Bearer {}".format(auth_token),
            "content-length": "577",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://open.spotify.com",
            "referer": "https://open.spotify.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "spotify-app-version": "1.1.93.174.gd2981e5f"

        }

        data = {
            "baseRevision": "AAAAAj6iTwnHqw5drsdValAfXrsDTLpz","deltas": [{"ops": [{"kind": "ADD","add": {"fromIndex": 0,"items": [{"uri": "spotify:playlist:" + self.playlist,"attributes": {"addedBy": "","timestamp": time_stamp,"seenAt": "0","public": "false","formatAttributes": []}}],"addLast": "false","addFirst": "true"}}],"info": {"user": "","timestamp": "0","admin": "false","undo": "false","redo": "false","merge": "false","compressed": "false","migration": "false","splitId": 0,"source": {"client": "WEBPLAYER","app": "","source": "","version": ""}}}],
            "wantResultingRevisions": "false",
            "wantSyncResult": "false",
            "nonces": []
        }

        try:
            self.gaboservicepublic()
            self.gaboservice(auth_token)
            v = self.session.post("https://spclient.wg.spotify.com/playlist/v2/user/"+ user_id +"/rootlist/changes", json = data, headers = headers)           
            print("post" + v.status_code)
            if v.status_code == 200:
                return True, None
            if v.status_code == 400:
                return False, "Status Code 400 (Bad Request)" 
        except:
            return False, "while following"
"""


os.system(f"title {modulename} by {moduleowner}")
print("\n[1] Profile Follower Bot") #\n[2] Playlist Follower Bot(Not Working)")
moduleinput = int(input(f"\n[{modulename}] Select Module > "))
if moduleinput == 1:
    spotify_profile = str(input(f"[{modulename}/User] Spotify User Link: "))
else:
    spotify_playlist = str(input(f"[{modulename}/Playlist] Spotify Playlist Link: "))
    
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
    if moduleinput == 1:
        if proxyinput == 1:
            obj = spotifyuserfollow(spotify_profile, proxytype, proxies[proxy_counter])
        if proxyinput == 2:
            obj = spotifyuserfollow(spotify_profile, proxytype, proxies[proxy_counter])
        else:
            obj = spotifyuserfollow(spotify_profile)
        result, error = obj.follow()
        if result == True:
            counter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}/User] " + colorama.Fore.GREEN + "Follower Sended")
            count()
        else:
            errorcounter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}/User] " + colorama.Fore.RED + f"Error {error}")
            count()
    else:
        if proxyinput == 1:
            obj = spotifyplaylistfollow(spotify_playlist, proxytype, proxies[proxy_counter])
        if proxyinput == 2:
            obj = spotifyplaylistfollow(spotify_playlist, proxytype, proxies[proxy_counter])
        else:
            obj = spotifyplaylistfollow(spotify_playlist, proxytype)
        result, error = obj.follow()
        if result == True:
            counter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}/Playlist] " + colorama.Fore.GREEN + "Follower Sended")
            count()
        else:
            errorcounter += 1
            safe_print(colorama.Fore.MAGENTA + f"[{modulename}/Playlist] " + colorama.Fore.RED + f"Error {error}")
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

