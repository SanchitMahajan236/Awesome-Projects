import os, subprocess
import sys

def getlists():
    if getlastm():
        os.system('termux-media-player stop')
    print("Scan a mp3 music in this path")
    os.system("find -L ~/PYTUBE_CLI/download/audio -type f -ipath '*.mp3' >source/lists/mp3.list")
    print("scan in source download compeleto")
    #pil = input("scan sdcard? y/n ").lower()
    #if pil.strip() == 'y':
        #os.system("find -L /sdcard/YMusic -type f -ipath '*.mp3' >>source/lists/mp3.list")
        #print("scan compeleto")
    input("Please enter to continued...")
    runn()
    playy()
    
def getlastm():
        subprocess.call("termux-media-player info> source/lists/cek.xx",shell=True);f = open("source/lists/cek.xx", "r")
        ff = f.read()
        f.close()
        #True if len(ff) >= 20 else False
        if len(ff) >= 20:
            return True
        else: 
            return False
        
def runn():
    f = open("source/lists/mp3.list","r")
    a = f.read()
    aa = a.split("\n"); aa.remove('')
    f.close()
    judl = []
    for x,n in enumerate(aa,start=1):
        jd = n.split("/")
        judl.append(f"{x}. {jd[9]}")
    return judl
    
def playy():
    try:
        f = open("source/lists/mp3.list", "r")
        a = f.read()
        aa = a.split("\n"); aa.remove('')
        f.close()
        pp = True
        while pp:
            print("""\n\n
            ▀█▀ █▀█ █▀█ █░░ ▄▀█ █▄█
            ░█░ █▀▄ █▀▀ █▄▄ █▀█ ░█░
                     {aldyansyahcp}
            
            note:(Make sure you clone this repo in $HOME directory)
            """)
            for i in runn():
                print(i)
            pil = input("\nPilih nomornya: ")
            os.system("clear")
            if pil.isdigit():
                os.system("echo -n '\n\n\n'")
                os.system("termux-media-player play "+aa[int(pil)-1])
            if pil == "pause":
                os.system("termux-media-player pause")
            if pil == "resume":
                os.system("termux-media-player play")
            if pil == "exit":
                exit()
            if pil == "back":
                os.system("python yts.py")
            if pil == "help":
                names = """
                    pilih: number music
                    pause: pause music
                    resume: resumed your last music
                    exit: exit media-player
                    back: turn-back to Youtube-Downloader
                """
                print(names)
                    
    except KeyboardInterrupt:
        print("thank you!!")
    except IndexError:
        print("tenkyuu dua")

