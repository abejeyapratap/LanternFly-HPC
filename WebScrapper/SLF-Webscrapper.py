from bs4 import BeautifulSoup as bs
import requests  
from urllib.request import urlopen
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
import math
import urllib.request
import shutil
import requests

def is_valid_url(u):
    parsed = urlparse(u)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_images(link):
    imgs = []
    soup = bs(requests.get(link).content, "html.parser")
    for img in soup.select(selector="img"):
        img_url = img.attrs.get("src")
        if not img_url:
            # img has no src attribute, continue
            continue
        
        img_url = urljoin(link, img_url)

        try:
            # strip out the query string bit from the url
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        
        if is_valid_url(img_url):
            # Save img_url to the imgs list
            imgs.append(img_url)
    
    return imgs


if __name__ == "__main__":
    scrape_url = "https://www.istockphoto.com/photos/spotted-lanternfly"
    ##scrape_url = "https://www.google.com/search?q=spotted+lanternfly&hl=en&tbm=isch&sxsrf=ALeKk03xdJ4LuD62mU5osCSLr_muisY_hA%3A1620401600849&source=hp&biw=1497&bih=863&ei=wF2VYPePMaGOwbkPyvWhkAo&oq=spotted+&gs_lcp=CgNpbWcQAxgAMgQIIxAnMgUIABCxAzIFCAAQsQMyBQgAELEDMggIABCxAxCDATIFCAAQsQMyBQgAELEDMgUIABCxAzIFCAAQsQMyAggAOgcIIxDqAhAnUJlwWNZ3YNl-aAFwAHgAgAFTiAGBBJIBATiYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img"
    
    # load the url and get all img srcs
    files = get_images(scrape_url)

    # Where the images will be saved to
    IMAGE_DOWNLOAD_DIRECTORY = "/Users/jhwang/Downloads/SLFpics"

    # Ensure the image directory is created
    os.makedirs(IMAGE_DOWNLOAD_DIRECTORY, exist_ok=True)

    # Helper for finding out the local file URL of an image with the given index
    create_local_file_url = lambda i : os.path.join(IMAGE_DOWNLOAD_DIRECTORY, f"SLF-Pic{i}.jpg")

    def download_image(url: str, index: int):
        """Downloads an image from the given URL and the given index"""
        print(f"Downloading image from {url}")

        # Download the image and get the saved url
        local_url = create_local_file_url(index)

        if os.path.exists(local_url):
            # Image was already downloaded, we can safely return the existing URL
            print(f"{url} already downloaded")
            return local_url

        urllib.request.urlretrieve(url, local_url)[0]

        print(f"{url} saved to {local_url}")
        return local_url

    # Download all files
    downloaded_files = [download_image(file_url, index) for index,file_url in enumerate(files)]
