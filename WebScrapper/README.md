# Web Scrapper 

# Using the WebScrapper 
This Web Scrapper uses Beautiful Soup to comb a certain website for image urls then makes a folder at a given pathname and converts all the urls to .img files and
downloads all the images to that directory. Simply run it and enter a pathname and website address when prompted. There are some sites that do not work like 
Google images but websites such as Flikr, Iphoto, and pintrest all work.

# Output
If the file "SLFpics" does not already exist at the time of execution, the script will make one. If it does exist, it will use that folder. If the images downloaded 
already exist in the folder, the script will not redownload them.

## Final Scripts
- SLF-Webscrapper.py 
  The webscrapper meant to comb websites with images of Spotted Lanterflies but works on any website with a few exceptions
