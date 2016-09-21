from irc import *
import os
import random
import requests

 
channel = "#ucsdhkntest"
server = "irc.freenode.net"
nickname = "jjjhs"
 
irc = IRC()
irc.connect(server, channel, nickname)
 
 
while 1:
    text = irc.get_text()
    print text
 
    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")

    if "PRIVMSG" in text and channel in text and "quote" in text:
        print "found quote"
	quotes_api_url = "https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous"
       	headers={
    		"X-Mashape-Key": "2WbF6TRlZgmsh8wTwHIuamNJCuvIp1gAyhBjsn0d1sU3F3TEQH",
    		"Content-Type": "application/x-www-form-urlencoded",
    		"Accept": "application/json"
  	}         
	response = requests.post(quotes_api_url, headers = headers)
	print response.text
        irc.send(channel, "'"+response.json()['quote']+"' - "+response.json()['author'])
