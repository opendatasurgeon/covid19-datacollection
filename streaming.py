from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import os
import json
from auth import TwitterAuth
import time
import sys



try:
	import smtplib
	from email.mime.text import MIMEText
except:
	sys.stderr.write("Error loading smtplib. Will not be able to send emails...\n")

# Output directory to hold json files (one per day) with tweets
# Within the output directory, the script loads a file named FILTER with the terms to be tracked (one per line)

outputDir = "outputDir"

## End of Settings###

class FileDumperListener(StreamListener):

	def __init__(self,filepath):
		super(FileDumperListener,self).__init__(self)
		self.basePath=filepath
		os.system("mkdir -p %s"%(filepath))

		d=datetime.today()
		self.filename = "%i-%02d-%02d-%02d.json"%(d.year,d.month,d.day,d.hour)
		self.fh = open(self.basePath + "/" + self.filename,"a")#open for appending just in case
		
		self.tweetCount=0
		self.errorCount=0
		self.limitCount=0
		self.last=datetime.now()
	
	#This function gets called every time a new tweet is received on the stream
	def on_data(self, data):
		self.fh.write(data)
		self.tweetCount+=1
		
		#Status method prints out vitals every five minutes and also rotates the log if needed
		self.status()
		return True
		
	def close(self):
		try:
			self.fh.close()
		except:
			#Log/email
			pass
	
	#Rotate the log file if needed.
	#Warning: Check for log rotation only occurs when a tweet is received and not more than once every five minutes.
	#		  This means the log file could have tweets from a neighboring period (especially for sparse streams)
	def rotateFiles(self):
		d=datetime.today()
		filenow = "%i-%02d-%02d-%02d.json"%(d.year,d.month,d.day,d.hour)
		if (self.filename!=filenow):
			print("%s - Rotating log file. Old: %s New: %s"%(datetime.now(),self.filename,filenow))
			try:
				self.fh.close()
			except:
				#Log/Email it
				pass
			self.filename=filenow
			self.fh = open(self.basePath + "/" + self.filename,"a")

	def on_error(self, statusCode):
		print("%s - ERROR with status code %s"%(datetime.now(),statusCode))
		self.errorCount+=1
	
	def on_timeout(self):
		raise TimeoutException()
	
	def on_limit(self, track):
		print("%s - LIMIT message recieved %s"%(datetime.now(),track))
		self.limitCount+=1
	
	def status(self):
		now=datetime.now()
		if (now-self.last).total_seconds()>300:
			print("%s - %i tweets, %i limits, %i errors in previous five minutes."%(now,self.tweetCount,self.limitCount,self.errorCount))
			self.tweetCount=0
			self.limitCount=0
			self.errorCount=0
			self.last=now
			self.rotateFiles()#Check if file rotation is needed
		

class TimeoutException(Exception):
	pass

if __name__ == '__main__':
	while True:
		try:
			#Create the listener
			listener = FileDumperListener(outputDir)
			auth = OAuthHandler(TwitterAuth.consumer_key, TwitterAuth.consumer_secret)
			auth.set_access_token(TwitterAuth.access_token, TwitterAuth.access_token_secret)

			fhTerms = open(outputDir+"/FILTER","r")
			# On May 22th at 12:30PM, we changed our terms to the following:
			terms=["Coronavirus","Koronavirus","Corona","CDC","Wuhancoronavirus","Wuhanlockdown","Ncov",
				   "Wuhan","N95","Kungflu","Epidemic","outbreak","Sinophobia","China","covid-19",
				   "corona virus","covid","covid19","sars-cov-2","COVID-19","COVD","pandemic","coronapocalypse",
				   "canceleverything","Coronials","SocialDistancingNow","Social Distancing","SocialDistancing",
				   "panicbuy","panic buy","panicbuying","panic buying","14DayQuarantine","DuringMy14DayQuarantine",
				   "panic shop","panic shopping","panicshop","InMyQuarantineSurvivalKit","panic-buy",
				   "panic-shop","coronakindness","quarantinelife","chinese virus","chinesevirus",
				   "stayhomechallenge","stay home challenge","sflockdown","DontBeASpreader","lockdown","lock down",
				   "shelteringinplace","sheltering in place","staysafestayhome","stay safe stay home","trumppandemic",
				   "trump pandemic","flattenthecurve","flatten the curve","china virus","chinavirus",
				   "quarentinelife","PPEshortage","saferathome","stayathome","stay at home","stay home","stayhome",
				   "GetMePPE","covidiot","epitwitter","pandemie","virus"]
			#terms=["coronavirus","corona","cdc","Chinese virus","covid19","flu","virus"]
			# On May 5th at 10:30AM, we added the term 'virus' to the query.
			# terms=["coronavirus","corona","cdc","Chinese virus","covid19","flu"]
			# On May 4th, at 11:30AM, we switched from using hashtags to just the keywords.
			#terms=["#coronavirus","#corona","#cdc","Chinese virus","#covid19","flu"]
			for line in fhTerms:
				terms.append(line.strip())
			print("%s - Starting stream to track %s"%(datetime.now(),",".join(terms)))

			#Connect to the Twitter stream"#coronavirus","#corona","#cdc"
			stream = Stream(auth, listener)
			#stream.filter(locations=[-0.530, 51.322, 0.231, 51.707])#Tweets from London
			stream.filter(track=terms)

		except KeyboardInterrupt:
			#User pressed ctrl+c or cmd+c -- get ready to exit the program
			print("%s - KeyboardInterrupt caught. Closing stream and exiting."%datetime.now())
			listener.close()
			stream.disconnect()
			break
		except TimeoutException:
			#Timeout error, network problems? reconnect.
			print("%s - Timeout exception caught. Closing stream and reopening."%datetime.now())
			try:
				listener.close()
				stream.disconnect()
			except:
				pass
			continue
		except Exception as e:
			#Anything else
			try:
				info = str(e)
				sys.stderr.write("%s - Unexpected exception. %s\n"%(datetime.now(),info))
				msg = MIMEText("Unexpected error in Twitter collector. Check server. %s"%info);
				msg['Subject'] = "Unexpected error in Twitter collector"
				msg['From'] = "youremail@example.com"
				msg['To'] = email
				s = smtplib.SMTP("smtp.example.com") #Update this to your SMTP server
				s.sendmail("youremail@example.com", email, msg.as_string())
				s.quit()
			except:
				pass
			time.sleep(1800)#Sleep thirty minutes and resume
			
