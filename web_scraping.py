"""
Lecture 11 - Web scraping

"""


"""
Guide for ethical web scraping

Disclaimer: None of this is legal advice. But if you want to read more:
    * https://en.wikipedia.org/wiki/Nguyen_v._Barnes_%26_Noble,_Inc.
    * https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act
    * Linked-in sues 100 anonymous web scrapers (https://digitalcommons.law.scu.edu/cgi/viewcontent.cgi?httpsredir=1&article=2261&context=historical)
    * Facts cannot be copywritten, but creative assembly of them can be (https://www.cendi.gov/publications/04-8copyright.html#214)

1) If an API exists, use it. There is probably a python module for the API too. Here are 3 modules for Twitter alone:
    * https://pypi.python.org/pypi/twitter
    * https://github.com/bear/python-twitter
    * https://python-twitter.readthedocs.io/en/latest/

2) Respect robots.txt; don't scrape disallowed areas.
    * https://en.wikipedia.org/wiki/Robots_exclusion_standard
    * If robots.txt is missing - don't assume scraping the entire site map is allowed or even good idea.
    * disallowed paths aren't always restricted, they may be disallowed for YOUR benefit.(lots of small worthless files)
    * urllib has a built in parser for robots.txt: https://docs.python.org/3/library/urllib.robotparser.html

3) Your web scraping should not look like a bad DoS attack (it should not look like a good DoS attack either...)
    * https://en.wikipedia.org/wiki/Denial-of-service_attack
    * In Python:  
        time.sleep(5)  # sleep for 5 seconds
    * If wrapping a Python script in Bash:
        sleep 5  # sleep for 5 seconds
    * Larger websites can handle shorter sleeps, be nice to smaller websites
    * Use off-peak hours if you are doing a lot of scraping 

4) Save the page instead of re-scraping whenever possible
    * If you are testing a program, save the page you are scraping instead of re-scraping with every test
        * Write the output to a text file and read it in - or save it as a pickle (https://docs.python.org/3/library/pickle.html)
    * This is also a good idea with XML files that you may want to extract information from multiple times

5) Include your contact information in the request header under "User-Agent"
    * Here is a truncated example from: https://docs.python.org/3.4/howto/urllib2.html#headers
        user_agent = 'Python web crawler with urllib - Contact: klevi@sdsu.edu'
        headers = { 'User-Agent' : user_agent }
        req = urllib.request.Request(url, data, headers)

6) Don't lie, cheat, or steal. (not exclusive to web scraping)
    * Don't use web scraping to steal and re-upload content
    * Don't scrape personal information and email addresses from craigslist to sell to advertisers
    * If you receive a Cease and Desist - you should cease and desist, do not change your IP and continue



"""

## Shortest example
import urllib.request as ur

url = "http://www.uniprot.org/uniprot/{0}.fasta".format('P69892')
y = ur.urlopen(url).read()
# print(y)
# print(y.decode())

# You may be able to read the undecoded version when printed, but it wont work for comparisons, or string functions
# y.split(',')
# print(y == '>sp|P69892|HBG2_HUMAN Hemoglobin subunit gamma-2 OS=Homo sapiens OX=9606 GN=HBG2 PE=1 SV=2\nMGHFTEEDKATITSLWGKVNVEDAGGETLGRLLVVYPWTQRFFDSFGNLSSASAIMGNPK\nVKAHGKKVLTSLGDAIKHLDDLKGTFAQLSELHCDKLHVDPENFKLLGNVLVTVLAIHFG\nKEFTPEVQASWQKMVTGVASALSSRYH\n')



## Another Example
# find the number of reads in a fastq file, before downloading the file (which could be 0.1 to 40 gb in size)

# import urllib.request as ur
# import re
#
# sra_file_name = "SRR3403834"
# url = "https://trace.ncbi.nlm.nih.gov/Traces/sra/?run={}".format(sra_file_name)
# string = ur.urlopen(url).read().decode()
#
# reads_per_spot = re.findall(r'This run has ([0-9]) reads per spot', string)
# print(reads_per_spot)
#
# spots = re.findall(r'<span id="total_spots">(.*?)<span class="file-size .*?">(.*?)</span>', string)
# print(spots)
