#!/usr/bin/python
#-*-coding:utf-8-*-
# print "give me a bottle of code xd"
# ^ ^

__author__="Fexyler"
__date__ ="20.08.2017"
__thanksto__="Black Viking"


import os,sys,smtplib,time,vlc,re,random,webbrowser,base64
import fexyoutube as fy


"""It's a part of I.N.T.E.A.X PROJECT.This script can evaluate string to process."""
musicdur = lambda: music(False)

def music(cal=True):
    global c
    if cal == False:
        c.stop()
    if cal == True:
        PATH = os.path.expanduser('~') + os.sep + "Muzik" + os.sep
        musics = []
        dirs = [PATH]
        for i in os.listdir(PATH):
            if os.path.isdir(PATH+i):
                dirs.append(PATH+i)
        for dir in dirs:
            for file in os.listdir(dir):
                if ".mp3" in file:
                    musics.append(dir+os.sep+file)
        mp3=random.choice(musics)
        c=vlc.MediaPlayer(mp3)
        c.play()

def saatkac():
    return "Şu anda saat %s "%(time.strftime("%H:%M"))

def emailgonder():
    dosya=open("/home/fexyler/Desktop/inteax/inteaxconfig").read().strip()
    email=re.findall("<mailadress>(.*?)</mailadress>",dosya)[0]
    emailpass=re.findall("<mailpass>(.*?)</mailpass>",dosya)[0]
    mailpass=base64.b64decode(emailpass)
    alici=raw_input("Lütfen alıcının mail adresini giriniz :")
    konu=raw_input("Lütfen atılacak mailin konusunu giriniz :")
    mesaj=raw_input("Mesajınızı girin :")
    emailtext="""
From: {}
To: {}
Subject: {}
{}
""".format(email,alici,konu,mesaj)
    try:
        sunucu = smtplib.SMTP("smtp.gmail.com:587")
        sunucu.starttls()
        sunucu.login(email, mailpass)
        sunucu.sendmail(email, alici, emailtext)
        sunucu.close()
    except Exception as err:
        print("|>|Error: ", err)
def kill():
    sys.exit(1)

def googleara():
    url=raw_input("Lütfen URL'yi 'https://batuhanisildak.wordpress.com' şeklinde giriniz :")
    webbrowser.open_new(url)
def naber():
    cevap=["Teşekkürler efendim,sizi sormalı?","İyiyim teşekkür ederim siz nasılsınız?","Bomba gibiyim!","Çok iyiyim!"]
    return random.choice(cevap)
def whc():
    cvp="Batuhan beni insanlara yardım etmem için üretti."
    return cvp
choices = {
    u"müzik indir"      :[fy.download,"İndirilmeye Hazırlanılıyor..."],
    u"seni kim yaptı"   :[whc,whc()],
    u"seni kim üretti"  :[whc,whc()],
    u"naber"        :[naber,naber()],
    u"nasılsın"     :[naber,naber()],
    u"exit"        :[kill,"Görüşürüz Efendim..."],
    u"çıkış"        :[kill,"Görüşürüz Efendim..."],
    u"görüşürüz"        :[kill,"Görüşürüz Efendim..."],
    u"bye"        :[kill,"Görüşürüz Efendim..."],
    u"mail gönder" :[emailgonder,"Mail gönderilmiştir efendim..."],
    u"google ara"  :[googleara,"İnternette aranıyor..."],
    u"saat kaç"    :[saatkac,saatkac()],
    u"müzik çal"   :[music,"Rastgele müzik açılıyor..."],
    u"müziği aç"   :[music,"Rastgele müzik açılıyor..."],
    u"müziği kapat":[musicdur,"Müzik Durduruluyor..."],
    u"müzik dur"   :[musicdur,"Müzik Durduruluyor..."]
}

result=""
konus=""
type=""
color=""
def evaluate(string):
    global result,konus,type,color
    denetle=False
    try:
        for choice in choices:
            if string==choice:
                choices[choice][0]()
                result=choices[choice][1]
                konus=choices[choice][1]
                type="info"
                color="blue"
                denetle=True
        if denetle==False:
            result="Sanırım dediklerinizi anlayamadım"
            konus=result
            type="error"
            color="red"
    except Exception as error:
        result="Bir Hata Oluştu"
        konus=result
        type="error"
        color="red"
    finally:
        return(result,type,color,konus)
