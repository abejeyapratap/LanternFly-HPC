# Web Scrapper 

# Using the WebScrapper 
This Web Scrapper uses Beautiful Soup to comb a certain website for image urls and converts all the urls to .img files and
downloads all the images to that directory. Simply run it and enter a pathname and website address when prompted. There are some sites that do not work like 
Google images but websites such as Flikr, Iphoto, and pintrest all work.

# Output
If a file in the pathname does not exist, it will create a file with that name.
If the images that will be downloaded already exist in the folder, the script will not redownload them.

The default website is https://www.istockphoto.com/photos/spotted-lanternfly so if no pathname is given, it will download all the images off this website

## Final Scripts
- SLF-Webscrapper.py 
  The webscrapper meant to comb websites with images of Spotted Lanterflies but works on any website with a few exceptions
