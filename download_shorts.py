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

# ydl_opts = {
#         'format_sort': ['res:1080', '+size'],
#         'extract_flat': 'discard_in_playlist',
#         'outtmpl': './videos2/%(id)s.%(ext)s',
#         # 'proxy':'socks5://127.0.0.1:8080',
#         'concurrent-fragments': 32,
#         'retries' : 3,
#         'fragment_retries': 3,
#         'ignoreerrors': 'only_download',
#         # below config is the key to speed.
#         'socket_timeout': 20.0,
#         'throttledratelimit': 256000
# }
ydl_opts = {'extract_flat': 'discard_in_playlist',
           'format': 'bv+ba/b',
           'format_sort': ['ext'],
           'fragment_retries': 10,
           'ignoreerrors': 'only_download',
           'postprocessors': [{'key': 'FFmpegConcat',
                               'only_multi_video': True,
                               'when': 'playlist'}],
           'retries': 10}


def download_shorts(url, channel):

    try:
        ydl_opts['outtmpl'] = f"./{channel}/%(id)s.%(ext)s"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return url


if __name__ == "__main__":
    # 朝鲜日报 # >> jtbc ~ newskbs 
    # 韩国的在youtube的9大新闻问题,应该只有朝鲜日报的shorts具有比较多的talking face数据
    korean_channels = ["@chosunmedia"]
    # FRANCE24 找到的最好的法语news channel
    french_channels = ["FRANCE24 "]
    # ANN News:https://www.youtube.com/@ANNnewsCH/videos 具有少量的talking face 
    # テレ東NEWS‍: https://www.youtube.com/@tvtokyobiz/shorts 会多一些talking,但是视频具有很多字幕
    # NHK NEWS : 全tm 相扑
    # Yahoo : 不太行
    japanese_channels = ["@tvtokyobiz"]
    
    all_channels = korean_channels + french_channels + japanese_channels
    
    for channel in all_channels:
        url = "https://www.youtube.com/{channel}/shorts".format(channel=channel)
        download_shorts(url,channel=channel[1:])