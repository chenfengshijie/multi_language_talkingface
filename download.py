from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,as_completed
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
        'format_sort': ['res:1080', '+size'],
        'extract_flat': 'discard_in_playlist',
        'outtmpl': './videos2/%(id)s.%(ext)s',
        # 'proxy':'socks5://127.0.0.1:8080',
        'concurrent-fragments': 32,
        'retries' : 3,
        'fragment_retries': 3,
        'ignoreerrors': 'only_download', 
        # below config is the key to speed.
        'socket_timeout': 20.0,
        'throttledratelimit': 256000
}

def download_video(url,language):

    try:
        ydl_opts['outtmpl'] = f"./{language}/%(id)s.%(ext)s"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return url


    
if __name__ == "__main__":
    # main()
    languages = {"japanese" :'urljapenese_4m.txt','korean' : 'urlkorean.txt'}
    for k,v in languages.items():
        with open(v,'r') as f:
            urls= [line.strip() for line in f]
        for url in urls[:20]:
            download_video(url,k)
            time.sleep(2)
