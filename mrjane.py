#!/usr/bin/env python3
# This tool was made completely by @L3V1python on github
# go check out my other tool WebWeaver
# ©COPYRIGHTED© 

import time 
import os
import requests
import cmd
import colorama
import json
import random
from bs4 import BeautifulSoup
from urllib.parse import quote
sites = {
    "Instagram": "https://www.instagram.com/{}",
    "X/Twitter": "https://x.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Threads": "https://www.threads.net/@{}",
    "Facebook": "https://www.facebook.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Tumblr": "https://{}.tumblr.com",
    "Reddit": "https://www.reddit.com/user/{}",
    "Telegram": "https://t.me/{}",
    "Mastodon": "https://mastodon.social/@{}",
    "Bluesky": "https://bsky.app/profile/{}.bsky.social",
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "Codeberg": "https://codeberg.org/{}",
    "SourceForge": "https://sourceforge.net/u/{}/",
    "Stack Overflow": "https://stackoverflow.com/users/{}",
    "Stack Exchange": "https://stackexchange.com/users/{}",
    "Replit": "https://replit.com/@{}",
    "CodePen": "https://codepen.io/{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "Docker Hub": "https://hub.docker.com/u/{}",
    "npm": "https://www.npmjs.com/~{}",
    "PyPI": "https://pypi.org/user/{}",
    "Hugging Face": "https://huggingface.co/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "Chess.com": "https://www.chess.com/member/{}",
    "Lichess": "https://lichess.org/@/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Kick": "https://kick.com/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Vimeo": "https://vimeo.com/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Mixcloud": "https://www.mixcloud.com/{}",
    "Bandcamp": "https://{}.bandcamp.com",
    "Medium": "https://medium.com/@{}",
    "Dev.to": "https://dev.to/{}",
    "Hashnode": "https://hashnode.com/@{}",
    "WordPress": "https://{}.wordpress.com",
    "Blogger": "https://{}.blogspot.com",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "Goodreads": "https://www.goodreads.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "pornhub": "https://pornhub.com/users/@{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "ArtStation": "https://www.artstation.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "500px": "https://500px.com/p/{}",
    "Unsplash": "https://unsplash.com/@{}",
    "Linktree": "https://linktr.ee/{}",
    "About.me": "https://about.me/{}",
    "Gravatar": "https://gravatar.com/{}",
    "Ko-fi": "https://ko-fi.com/{}",
    "Patreon": "https://patreon.com/{}",
    "Buy Me a Coffee": "https://buymeacoffee.com/{}",
    "OpenSea": "https://opensea.io/{}",
    "IMDb": "https://www.imdb.com/user/{}",
    "Letterboxd": "https://letterboxd.com/{}/",
    "Product Hunt": "https://www.producthunt.com/@{}",
}
os.system("clear")
def search_username(username):
    print(f"\nSearching for: {username}\n")
    for name, url in sites.items():
        profile = url.format(username)
        try:
            response = requests.get(profile, timeout=5)
            if response.status_code == 200:
                print(f"[+] Found {name}: {profile}")
            else:
                print(f"[-] Not found {name}")
        except:
            print(f"[!] Error checking {name}")
        time.sleep(random.uniform(0.5, 1.5))
def start_up():
    import time
    import os
    loading = rf"""
{colorama.Fore.LIGHTRED_EX}Starting tool...

Loading...

Almost thereeeee.....

done."""
    for line in loading.strip("\n").splitlines():
        print(line)
        time.sleep(random.uniform(0.09, 0.2))
def banner():
    os.system("clear")
    bannr = rf"""
 ___      ___   _______                    ___      __      _____  ___    _______  
|"  \    /"  | /"      \                  |"  |    /""\    (\"   \|"  \  /"     "| 
 \   \  //   ||:        |                 ||  |   /    \   |.\\   \    |(: ______) 
 /\\  \/.    ||_____/   )                 |:  |  /' /\  \  |: \.   \\  | \/    |   
|: \.        | //      /   _____       ___|  /  //  __'  \ |.  \    \. | // ___)_  
|.  \    /:  ||:  __   \  ))_  ")     /  :|_/ )/   /  \\  \|    \    \ |(:      "| 
|___|\__/|___||__|  \___)(_____(     (_______/(___/    \___)\___|\____\) \_______) 
                                  L3V1"""
    for line in bannr.strip("\n").splitlines():
        print(line)
        time.sleep(0.1)
def prompt():
    while True:
        text = rf"""
>> """
        user = input(text)
        if user.lower() == "exit":
            print("Exiting...")
            break
        elif user.lower() == "help":
            print(f"{colorama.Fore.YELLOW}Commands:")
            print(f"{colorama.Fore.LIGHTRED_EX}search <username> - Search username")
            print(f"{colorama.Fore.LIGHTRED_EX}help - Show commands")
            print(f"{colorama.Fore.LIGHTRED_EX}exit - Close tool")
        elif user.lower().startswith("search "):
            username = user[7:]
            search_username(username)
        else:
            print("Use: search <username>")
start_up()
banner()
prompt()