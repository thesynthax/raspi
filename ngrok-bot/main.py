from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import subprocess
import time
import discord_webhook
import requests

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
opt.add_argument("--headless")
opt.headless = True

driver = webdriver.Firefox(executable_path='/usr/bin/geckodriver', options=opt)

connected = False
testURL = "https://google.com"
while connected == False:
    try:
        requests.get(testURL)
        connected = True
    except requests.ConnectionError as e:
        connected = False
    time.sleep(30)


URL = "localhost:4040"
urls = []

driver.get(URL)
urlList = driver.find_elements_by_tag_name("a")
for url in urlList:
    if "tcp" in url.text:
        urls.append(url.text)

time.sleep(10)

#command = "ssh -l thesynthax 0.tcp.in.ngrok.io -p " + urls[0][-5:]
#try:
#    output = subprocess.check_output(command, shell=True)
#except subprocess.CalledProcessError as e:
    
#print(output)
#if "Connection closed by remote host" in output:
#    discord_webhook.send_msg(ssh=urls[1], vnc=urls[0])
#else:
#    discord_webhook.send_msg(ssh=urls[0], vnc=urls[1])

discord_webhook.send_msg(ssh=urls[0], vnc=urls[1])

driver.quit()
