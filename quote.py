#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#LO MAU RIKOD? BIAR KEREN GITU?
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
BG = "\033[1;97;41m"
RE = "\033[0m"
try:
	import requests,os,json,sys,time,random
	from bs4 import BeautifulSoup as bs
	import re
except:
	os.system('pip2 install requests bs4;python2 quote.py')
r='\033[91m'
c='\033[96m'
w='\033[0m'
def wait(t):
        for x in range(t):
            t -= 1
            sys.stdout.write('\r'+'\033[1;37m[\033[1;31m!\033[1;37m]\033[0;37m Tunggu '+ str(t)+'s')
            sys.stdout.flush();time.sleep(1)
def spin():
        try:
                L="\|/-"
                for q in range(10):
                        time.sleep(0.1)
                        sys.stdout.write("\r\033[1;32m[\033[1;33m"+L[q % len(L)]+"\033[1;32m]\033[0;37m Loading please wait...")
                        sys.stdout.flush()
        except:
                exit()
def ketik(teks):
	for i in teks + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.001)
def load(word):
    lix = [
     '/', '-', '╲', '|']
    for i in range(6):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()
def metu():
	print("%s[%sx%s] %sExiting Program"%(W1,R1,W1,R0))
	exit(1)
def koneksi():
	logo()
	try:
		rq = requests.get('http://github.com')
		spin()
		print("\n%s[%s#%s] %sKoneksi bagus"%(G1,Y1,G1,W0))
		time.sleep(2)
	except requests.exceptions.ConnectionError:
		print("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
		time.sleep(1)
		metu()
def logo():
	os.system('clear')
	ketik("""
 %s_____             %s_          %s_____%s         _
%s|     |%s___ ___ ___| |_ ___   %s|     |%s_ _ ___| |_ ___ ___
%s|   --|%s  _| -_| .'|  _| -_|  %s|  |  |%s | | . |  _| -_|_ -|
%s|_____|%s_| |___|__,|_| |___|  %s|__  _|%s___|___|_| |___|___|
                                %s|__|
%sPowered https://www.tools.w3llsquad.or.id
"""%(G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1,G1,W1))
def main():
	try:
		os.system('termux-setup-storage;git pull')
		logo()
		quote=raw_input('\033[1;32m[\033[1;33m#\033[1;32m] \033[1;37mQuote : ')
		if quote == '':
			print("%s[%s!%s] %sJangan kosong"%(G1,R1,G1,W0))
			time.sleep(0.8)
			main()
		name=raw_input('\033[1;32m[\033[1;33m#\033[1;32m] \033[1;37mName : ')
		if name == '':
			print("%s[%s!%s] %sJangan kosong"%(G1,R1,G1,W0))
			time.sleep(0.8)
			main()
		r=requests.Session()
		agent = r.get('https://pastebin.com/raw/QckwZTMc').text.split('\n')
		acak = random.choice(agent)
		spin()
		a = r.post('https://www.tools.w3llsquad.or.id/quotes-generator',headers={"User-Agent": "{acak}"},data={'name':name,'text':quote,'input':''})
		b = re.findall('<img src="(.*?)" class="card-img-top" alt="...">',a.text)
		c = b[0]
		d = r.get('%s'%(c))
		e = c.replace('https://www.tools.w3llsquad.or.id/img/capture/','')
		with open(e, "wb") as code:
			code.write(d.content)
		os.system("mv %s /sdcard"%(e))
		print ('%s[%s#%s] %sDownload selesai'%(G1,Y1,G1,W1))
		print ('%s[%s#%s] %sSilahkan cek penyimpanan internal anda'%(G1,Y1,G1,W1))
		print ('%s[%s#%s] %sTerima kasih bro :)'%(G1,Y1,G1,W1))
		exit()
	except requests.exceptions.ConnectionError:
		print("%s[%sx%s] %sTidak ada koneksi"%(W1,R1,W1,W0))
		time.sleep(1)
		metu()
if __name__=='__main__':
	koneksi()
	main()
