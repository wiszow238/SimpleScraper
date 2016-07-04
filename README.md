# SimpleScraper
A simple web crawler which would save internal links, and follow the links. The script would ask for a starting link 
and the depth number. Using this information, the script would launch a web crawler starting at the given link and fetch all
internal links. The depth number represents the maximum number of levels the crawler can go. 
The results will be stored in a JSON file in the same folder. The structure would contain the current web address and all 
internal links at that address. 

# Requirements
  - Python 3.3+
  - Scrapy (1.1.0)
  - tldextract (1.7.1)
  
# How to run
```
./emcScraper.sh
```
Or
```
python3 ./emcScraper.py
```
