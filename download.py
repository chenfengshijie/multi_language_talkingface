from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import os
import yt_dlp as youtube_dl
from zipfile import ZipFile
from tqdm import tqdm
import copy
import os
import shutil
import zipfile
from numpy import array_split
import time
from glob import glob

ydl_opts = {
    "format": "bv+ba/b",  # best video   # ["res:1080", "+size"],
    "extract_flat": "discard_in_playlist",
    "outtmpl": "./videos2/%(id)s.%(ext)s",
    # "proxy": "http://127.0.0.1:7890",
    "concurrent-fragments": 32,
    "retries": 10,
    "fragment_retries": 10,
    "ignoreerrors": "only_download",
    # below config is the key to speed.
}


def download_video(url, language):
    try:
        ydl_opts["outtmpl"] = f"./{language}/%(id)s.%(ext)s"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return url


if __name__ == "__main__":
    # main()
    # Japan finish

    # korean  200/1200
    # french finish 
    languages = {"korean": "urlkorean.txt"}
    for k, v in languages.items():
        with open(v, "r") as f:
            urls = [line.strip() for line in f]
        for url in urls:
            download_video(url, k)
            time.sleep(1)
