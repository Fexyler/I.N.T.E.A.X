# usr/bin/python
# -*-coding:utf-8-*-
# print "Give me a bottle of code xd"

__author__="Fexyler"
__date__="20.08.2017"
__thanksto__="Black Viking"

import os,sys,re

command = "youtube-dl --extract-audio --audio-format mp3 "
def download():
    dosya=open("inteaxconfig").read().strip()
    dizin=re.findall("<muzikpath>(.*?)</muzikpath>",dosya)[0]
    os.chdir(dizin)
    indir=raw_input("İndirilecek müziğin url'sini giriniz :") 
    os.system(command + indir)

