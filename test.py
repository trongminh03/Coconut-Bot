
from pixivpy3 import *
import requests
# import pandas as pd
from bs4 import BeautifulSoup
import os, shutil

REFRESH_TOKEN = 'Qsv1MTUy10WolXoIflhoHHo1M0aLIzBYgfSItBr2hDI'



aapi = AppPixivAPI()

aapi.auth(refresh_token=REFRESH_TOKEN)

# json_result = aapi.illust_ranking()
# for illust in json_result.illusts[:3]:
#     aapi.download(illust.image_urls.large,"", './download', "image.jpg", True)
    
json_result = aapi.search_illust('yae',  search_target="partial_match_for_tags" )
i = 0

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

# for illust in json_result.illusts[:5]:
#     aapi.download(illust.image_urls.large, str(i) , './download', "image.jpg", True)
#     i = i + 1
    