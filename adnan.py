# # AUTHER
# coding = # -*- coding: utf-8 -*-
#!user/bin/python 
import requests
import requests as Hisham
import  os 
import concurrent.futures

os.system("clear")
os.system("figlet ADmin-BRute")
print(f'''
\33[97m Hey Buddy,You Call Me DEVIL.


\33[91m     ADMIN - FINDER TOOL
\33[93m──────────────────────────────────────────────────
\33[93m▸ AUTHOR     : Adnan Adif Hisham
\33[1;32m▸ FACEBOOK   : Facebook.com/call.me.devil.2004
\33[91m▸ GITHUB     : GITHUB.COM/C4LLM3D3V1L
\33[91m──────────────────────────────────────────────────''')

web =str(input("\33[97m>> Enter Site Url : "))

if web == "":
  # TODO: write code...
  exit()
else :
  try :
      o= open("paths.txt","r").readlines()
      
  except Exception as e :
    print("[!] ERROR : "+str(e))
    
    
def brute(x):
  path = x.strip()
  url = web+path
  req = Hisham.get(url,timeout=10)
  if req.status_code < 400:
    print(f"\033[1;32m[+] FOUND : {url} | status : {req.status_code}")
  else:
    print(f"\033[91m[+] NOT FOUND : {url} | status : {req.status_code}")
    
with concurrent.futures.ThreadPoolExecutor() as exe :
 	exe.map(brute,o)