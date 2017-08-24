#!/usr/bin/python
#-*-coding:utf-8-*-
# print "give me a bottle of code xd"
# ^ ^
__author__="Fexyler"
__date__ ="20.08.2017"
__thanksto__="Black Viking"
config_name="inteaxconfig"

from colorama import Fore,init,Style,Back
import random,re,base64,getpass,time,os,sys
from needto import stt,speech,stp

reload(sys)
sys.setdefaultencoding("utf-8")

colors = {
    "":        "",
    "red":     Fore.RED,
    "cyan":    Fore.CYAN,
    "blue":    Fore.BLUE,
    "green":   Fore.GREEN,
    "white":   Fore.WHITE,
    "yellow":  Fore.YELLOW,
    "magenta": Fore.MAGENTA,
    "bright":  Style.BRIGHT
}
types = {"info" : "[INFO] ", "error" : "[ERROR] ", "config" : "[CONFIG] ","nospeech" : "[NOSPEECH] "}

konus = lambda  string:speech.say(string)
clear = lambda: os.system("clear")
dinle = lambda: stt.STT()
feval = lambda  text:stp.evaluate(text)

def fxprint(text,type=None,color=""):
    if color=="random":
        color = random.choice(colors.keys())
    text = colors[color] + types[type] + text
    print text
def fxinput(text,type=None,color=""):
    if color=="random":
        color = random.choice(colors.keys())
    text = colors[color] + types[type] + text
    return raw_input(text)

def genconfig(confname):
    global name,age,gender,muzikpath
    dosya=open(confname,"w")
    name       = fxinput("Lütfen adınızı giriniz : ","config","random")
    age        = int(fxinput("Lütfen yaşınızı giriniz : ","config", "random"))
    gender     = fxinput("Lütfen cinsiyetinizi giriniz : ","config", "random")
    muzikpath = fxinput("Lütfen Müziklerinizi Tuttuğunuz Klasörün Yolunu Giriniz :","config","random")
    mailadress = fxinput("Lütfen mail adresinizi giriniz : ","config", "random")
    mailpass   = getpass.getpass("Lütfen mail adresinizin şifrenisini giriniz : ")
    confex="""
<userinfo>
    <name>%s</name>
    <age>%s</age>
    <gender>%s</gender>
    <muzikpath>%s</muzikpath>
    <mailadress>%s</mailadress>
    <mailpass>%s</mailpass>
</userinfo>
"""%(name,age,gender,muzikpath,mailadress,base64.b64encode(mailpass))
    dosya.write(confex.lstrip("\n"))
    dosya.close()
def confcontrol(confname):
    global name,age,gender,muzikpath
    if os.path.exists(confname):
        dosya=open(confname).read().strip()
        if dosya !="" :
            name       = re.findall("<name>(.*?)</name>",dosya)[0]
            age        = re.findall("<age>(.*?)</age>",dosya)[0]
            gender     = re.findall("<gender>(.*?)</gender>",dosya)[0]
            muzikpath  = re.findall("<muzikpath>(.*?)</muzikpath>",dosya)[0]
            mailadress = re.findall("<mailadress>(.*?)</mailadress>",dosya)[0]
            mailpass   = re.findall("<mailpass>(.*?)</mailpass>",dosya)[0]
                
        else:
            fxprint("Bir Hata Oluştu,Uygulamadan Çıkıyorsunuz",type="error",color="red")
            sys.exit()
    else:
        tanisma="Merhaba,ben I.N.T.E.A.X sanırım sizi tanımıyorum efendim,hadi tanışalım!"
        fxprint(tanisma,"info","blue")
        konus(tanisma)
        genconfig(confname)
def maincode(STT=True):
    info = "Merhaba %s, saat %s"%(name.split()[0], time.strftime('%H:%M'))
    fxprint(info, "info", "green")
    konus(info)
    while True:
        if STT==True:
            selam=("Merhaba ben I.N.T.E.A.X,seni dinliyorum %s."%(name.split()[0]))
            fxprint(selam,"info","blue")
            kelime=dinle()
            fxprint("Yakalanan kelime : %s "+kelime,"info","random")
            result = feval(kelime)
            fxprint(result[0], type=result[1], color=result[2])
            konus(result[3])
        else:
            kelime=fxinput("I.N.T.E.A.X > ","nospeech","random")
            if kelime=="exit" or kelime=="bye" or kelime=="görüşürüz" or kelime=="çıkış":
                sys.exit()
            result=feval(kelime)
            fxprint(result[0],type=result[1],color=result[2])
            konus(result[3])

if __name__=='__main__':
    dinle()
    init(autoreset=True)
    confcontrol(config_name)
    if len(sys.argv) == 2 and sys.argv[-1] == "--no-stt":
        maincode(STT=False)
    else:
        maincode()
