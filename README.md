# covid19-datacollection

*./covid19-datacollection/*     
*This repository contains our methodology for collecting data from the Twitter.*    
1) **streaming_simple.py**- It will keep streaming until the user exits. All output stored to output.json (one tweet per line)
2) **streaming.py** - a class file for streaming_simple.py
3) **auth.py**- a class where we put our authorization keys (note: please put your keys, you can request them here: [Access Tokens](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens]))
4) **data2spreadsheet.py**- converts *output.json* to a utf-8 spreadsheet
5) **search_generic.py** - searches for terms in tweets (not part of 1-4, it's independent)   
   
*./Refrences/*     
1) **Source.txt**- Script source   
2) **Queries.txt**- Contains all the keywords we've been using to collect raw data

# Data Collection Method        

To collect relevant Twitter dataset for our analysis, we used two step approach. First, using the Tweet ID’s made public by University of Southern California (https://github.com/echen102/COVID-19-TweetIDs). USC crawled Twitter data set using their own queries (the queries are available in their GitHub page: https://github.com/echen102/COVID-19-TweetIDs/blob/master/keywords.txt).

  From this collected Twitter dataset, the research team extracted the Tweet IDs and made them public following the Twitter policy for data sharing. Using these IDs, we collected (“hydrated") twitter data using REST API methods with a tool known as Hydrator (this open-source tool is available here: https://github.com/DocNow/hydrator).
 
  To capture the USC data from January 21st to May 22nd, we used Hydrator. Then around 3:00 PM EST, we adapted their technique and independently collected the data. Going independent allowed us to add additional keywords and remove the ones we thought were not necessary following the social media trends.

  Our (USF) data are in a form of. json which are outputted per hour. Our data collection process is ongoing since May 22nd and they All they house on our university's research cluster. We will likely share our Tweet IDs in near future. 

~Thank you very much.
     

     
