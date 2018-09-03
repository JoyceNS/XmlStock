import requests
import untangle
import time

#gets updated xml
def getNewData():
	r = requests.get('http://rates.fxcm.com/RatesXML' , stream="true")
	open("data.xml", "w").write(r.text)
	return untangle.parse('data.xml')

#compares passed bid rate with the target rate
def compareRates(bidData):
	if bidData >= target: # I HATE THIS UGHHHHHH
		print (target + " for " + pair + " has been reached")
		return True
	else:
		return false

#asks for user entry
print ("Please enter the currency pair:")
pair = input()
print ("Please enter the target rate:")
target = input()

done = False

#every 5 seconds download xml
while (not done):
	time.sleep(5)
	obj = getNewData()
	for elem in obj.Rates.Rate:
		if elem['Symbol'] == pair:
			done = compareRates(elem.Bid.cdata)