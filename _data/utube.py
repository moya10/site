from selenium import webdriver
import time 
import youtube_dl 
import json
import re
import random

def vidstrip(playlist):
    for i in range(len(playlist)):
        end=playlist[i].find("&")
        word = playlist[i].find("watch?v=")
        playlist[i]=playlist[i][:end]
        playlist[i] = playlist[i].replace("watch?v=", "embed/",word)
    return playlist 

driver = webdriver.Chrome(executable_path='C:/Users/utopia/Downloads/chromedriver_win32/chromedriver.exe') 
driver.get('https://www.youtube.com/playlist?list=PL9WjA4M8MrTeyCAF2D93SRyu5GMWzabF3')
time.sleep(5)
playlist=[]
desc=[]
videos=driver.find_elements_by_class_name('style-scope ytd-playlist-video-renderer')
for video in videos:
    link=video.find_element_by_xpath('.//a[@id="thumbnail"]').get_attribute("href")
    descrpt=video.find_element_by_xpath('.//a[@id="video-title"]').get_attribute("title")
    playlist.append(link)
    desc.append(descrpt)
vidlist=vidstrip(playlist)
driver.close()
year =[]
for i in range(0,len(desc)):
    match = re.search(r'[1-3][0-9]{3}', desc[i])
    if match is not None and match.group() != "1229":
        year.append(match.group())
    else:
        digits = set(range(6,10))
        last_2 = random.sample(digits, 2)
        year.append(str(19) + ''.join(map(str, last_2)))

data = {}
data['events']=[]

for i in range(0,len(vidlist)):
    data['events'].append({"start_date":{"year": year[i]}, "text": {"text": desc[i], "headline": desc[i] }, "media":{"url": vidlist[i]}})

with open("timeline.json", "w") as f:
    json.dump(data, f)
