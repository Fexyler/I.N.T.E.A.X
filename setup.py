#!/usr/bin/python
#-*-coding:utf-8-*-
# print "give me a bottle of code xd"
# ^ ^
import os,pip
content = """
#!/bin/bash
cd /usr/share/inteax
python2 main.py "$@"
"""
def main():
    if os.name!="nt":
        if os.getuid()==0:
            os.system("git clone https://github.com/Fexyler/I.N.T.E.A.X.git /usr/share/inteax")
        
            for i in ["colorama","pyaudio","speechrecognition","youtube-dl","pyttsx3"]:
                pip.main(["install", i])
            file = open("/usr/bin/inteax", "w")
	    file.write(content)
            file.close()
            os.system("chmod +x /usr/bin/inteax")
            print "\n\n[+]Installiation is completed,type 'inteax' and use!"
        else:
            print("Type 'sudo' please.")
    else:
        print("Sorry you can not run in Windows,in the V2 you will run.")
if __name__="__main__":
    main()
