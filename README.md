# covid19-datacollection

This repository contains our current methodology for collecting data from the Twitter.

# Scripts Description

1) **streaming_simple.py**- It will keep streaming until the user exits. All output stored to output.json (one tweet per line)
2) **streaming.py** - a class file for streaming_simple.py
3) **auth.py**- a class where we put our authorization keys (note: please put your keys, you can request them here: [Access Tokens](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens]))
4) **data2spreadsheet.py**- converts *output.json* to a utf-8 spreadsheet
5) **search_generic.py** - searches for terms in tweets (not part of 1-4, it's independent)
