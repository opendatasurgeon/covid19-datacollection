
________________________________________________________ USC DATA COLLECTION ______________________________________________________________________

Process of Hydration: Because our work needed to be quick, we chose to use application. Whereas we only got jsonl (jsonLines) files from the script
			version of the Hydrator, we got both csv & jsonl from the Hydrator software, which boosted our speed when we needed to run 
			botometer scripts on usernames. In addition to that, script version of the software needed libraries that needed pre-approval 
			from CIRCE. And because our personal computer lack memory, we went with application which made sense to us at the time. 
			Software can be found here (https://github.com/DocNow/hydrator).

Short Comings: Some of the jsonl(jsonLines) files had inappropriate EOFs markers so we had to recrate all the jsonl files. Furthermore, 
		at the time, their Linux version of the software was impossible to run on our CIRCE server thus Tuc, Dre & Mihir had to
		rely on their Windows OS to run each tweet IDs text files from the USC (https://github.com/echen102/COVID-19-TweetIDs)
		USF Script: Dre upgraded Dr Scott Hale's script (https://github.com/computermacgyver/twitter-python) in order to stream twitter data 
		continously. Our script is located at (https://github.com/Big-Data-Analytics-Lab-USF/covid19-datacollection).

Data Collected: Because our (USF) approach was hastags based, we were getting tweets from every topic. However we liked the USC data and pursue onto
		collecting it because it was keywords based. We later, specifically in May, adapted their technique. Therefore, we used their dataset
		to double check what we've collected from March til May.
		
		January: 01/21-01/31
		February: 02/1-02-29
		March: 03/1-03/31
		April: 04/1-04/31
		May: 05/1-05/22
 
________________________________________________________ BOTOMETER METHODS ______________________________________________________________________

<========================================================== On USCs Data ===================================================================> 
----------------
|(1) USC 2020-03 |
 ----------------
	Random Sample: Sampled with 'Without Replacement', in all unique user_screen_name column
	Available Date Range: 03/01- 03/31
	Cut-off Range: NONE
	Unique Accounts: 5,758,992
	Sample Accounts: 100,000
	Sampling Date: 05/28
	Distributed: 05/28
        Botometer Runs: Distributed 5 ways; 20,000 to each team member 
			(a) Mary: 6/01-6/02 (NA returned--->)
			(b) Wesley:6/04-6/05 (NA returned--->)
			(c) Tuc: 5/28-5/30 (NA returned--->)
			(d) Dre: 5/31-6/02 (NA returned--->)
			(e) Mihir: 5/28-5/30 (NA returned--->)


 ----------------
|(2) USC 2020-04 |
 ----------------
	Random Sample: Sampled with 'Without Replacement', in all unique user_screen_name column
	Available Date Range: 04/01- 04/30
	Cut-off Range: NONE
	Unique Accounts: 4,126,552
	Sample Accounts: 100,000
	Sampling Date: 06/04
	Distributed: 06/04
        Botometer Runs: Distributed 5 ways; 20,000 to each team member 
			(a) Mary: 
			(b) Wesley:6/04-6/06 (NA returned--->)
			(c) Tuc: 6/07-6/09 (NA returned--->)
			(d) Dre: 
			(e) Mihir: 6/04-6/06 (NA returned--->)


 ----------------
|(3) USC 2020-05 |
 ----------------
	Random Sample: Sampled with 'Without Replacement', in all unique user_screen_name column 
	Available Date Range: 05/1-05/22
	Cut-off Range: 05/1-05/22
	Unique Accounts: 3,648,720
	Sample Accounts: 100,000
	Sampling Date: 06/10
	Distributed: 06/10
        Botometer Runs: Distributed  ways; 25,000 to each team member 
			(a) Mihir (50K): 6/10-6/13 (NA returned--->)
			(b) Tuc (25K): 
			(c) Ean (25K):

<==================================================== On USF/ DREDs Data ===================================================================> 
----------------------
|(1) USF/DREs 2020-04 |
 ---------------------
	Random Sample: Sampled with 'Without Replacement', in all unique screenNames column
	Available Date Range: 04/10-04/24
	Cut-off Range: 04/10-04/24
	Unique Accounts: 
	Sample Accounts: XXXXX
	Sampling Date: 05/03
	Distributed: 05/06-05/08
        Botometer Runs: Distributed 5 ways; ~XXXXXXX to each team member 
			(a) Mary: 
			(b) Wesley: 05/06-05/26 (NA returned--->)
			(c) Tuc:
			(d) Dre: 
			(e) Mihir: 05/09-05/23 (NA returned--->)