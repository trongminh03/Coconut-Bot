from pixivpy3 import *
import requests
# import pandas as pd
# from bs4 import BeautifulSoup
import os, shutil
from datetime import datetime
    
    
REFRESH_TOKEN = 'Qsv1MTUy10WolXoIflhoHHo1M0aLIzBYgfSItBr2hDI'
api = AppPixivAPI()
# api.login("username", "password")   # Not required
api.auth(refresh_token=REFRESH_TOKEN)
# get origin url
# json_result = api.illust_detail(59580629)
# illust = json_result.illust
# print(">>> origin url: %s" % illust.image_urls['large'])
# get ranking: 1-30
# mode: [day, week, month, day_male, day_female, week_original, week_rookie, day_manga]


def search(tag):
    json_result = api.search_illust(str(tag),  search_target="exact_match_for_tags", sort="popular_desc")

    i = 0
    for illust in json_result.illusts[:5]:
        api.download(illust.image_urls.large, str(i) , './download', "image.jpg", True)
        i = i + 1

def daily():
    # json_result = api.
    json_result = api.illust_ranking(mode = "month")
    # print(rank_list)
    # ranking = rank_list.response[0]
    i = 0
    for illust in json_result.illusts[:5]:
        api.download(illust.image_urls.large, str(i) , './download', "image.jpg", True)
        i = i + 1

def risu():
    json_result = api.search_illust('risu',  search_target="exact_match_for_tags", sort="popular_desc")
    dt = datetime.now()
    x = dt.day
    i = 0
    for illust in json_result.illusts[:5]:
        if(i == x):
            api.download(illust.image_urls.large, str(0) , './download', "image.jpg", True)
        i = i + 1
    
    
def delete():
    folder = 'download'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    


