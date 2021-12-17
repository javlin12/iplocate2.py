import requests#for request the GET
import argparse#for the arguments
import json#for the json as data received in json format

#if __name__=="__main__":#for program to start from here
	
neo = argparse.ArgumentParser()
	#passing parse syntax
	
neo.add_argument("-i","--ipaddress",help="to check the ip")
neo.add_argument("-u","--usage",dest="usage", help="-i google.com")
	#passing arguments
	
args = neo.parse_args()
	#to get all argument
	
ip = args.ipaddress
	#passing ip the value
	
url= "http://ip-api.com/json/"+ip
	#for the url and the ip value
	
response=requests.get(url)
	
data = json.loads(response.content)
	
print(data)
	
	
print("\t[+] IP\t\t\t", data["query"])
print("\t[+] CITY\t\t", data["city"])
print("\t[+] ISP\t\t\t", data["isp"])
print("\t[+] LOC\t\t\t", data["country"])
print("\t[+] REG\t\t\t", data["regionName"])
print("\t[+] TIME\t\t", data["timezone"])
print("\t[+] ZIP\t\t\t", data["zip"])
print("\t[+] LAT\t\t\t", data["lat"])
print("\t[+] LON\t\t\t", data["lon"])
print("\t[+] timezone\t",data["timezone"])
print("\t[+] isp\t",data["isp"])
print("\t[t] org\t",data["org"])

#print("\t[t] asname",data["asname"])
#print("\t[t] mobile",data["mobile"])
#print("\t[t] hosting",data["hosting"])
#print("\t[t] proxy",data["proxy"])
#print("\t[+] currency\t",data["currency"])
