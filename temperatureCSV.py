#sudo pip3 install BeautifulSoup4
from bs4 import BeautifulSoup as BS
import csv
import datetime
import time
from urllib.request import urlopen
import http.client

while True:
	try:
		html = urlopen("http://192.168.1.72", timeout=3)
		soup = BS(html,features="html.parser")
		elem = soup.findAll('p')
		essai = elem[0].text.splitlines()
		essai2 = elem[1].text.splitlines()
		#print(essai)
		#print(essai2)

		filename = "/Users/racinecubix/Documents/temperature2.csv"
		with open(filename, "a", newline="") as csvfile:
			csvwriter = csv.writer(csvfile,  delimiter=',')
			csvwriter.writerow([datetime.datetime.now(),essai[3],essai2[3]])
			#time.sleep(9.9277)
	except (KeyboardInterrupt, SystemExit):
		print("KeyboardInterrupt has been caught.")
	#except (http.client.IncompleteRead)	:#HTTPConnection
	except Exception as e:
		print(str(e), datetime.datetime.now())
		time.sleep(9.9277)#just to be sure it won't reproduce
		pass
	time.sleep(9.9277)





