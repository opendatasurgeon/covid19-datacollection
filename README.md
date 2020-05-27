# covid19-datacollection

This repository contains our current methodology of collecting twitter data.

# Scripts Description

1) **streaming_simple.py**- It will keep streaming until the user exits. All output stored to output.json (one tweet  per line)
2) **streaming.py** - a class file for streaming_simple.py
3) **auth.py**- a class where we put our authorization keys (ofcourse you will have to fill yours)
4) **data2spreadsheet.py**- converts *output.json* to a utf-8 spreadsheet
5) **search_generic.py** - 
