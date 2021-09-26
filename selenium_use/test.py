from typing import KeysView, Optional
from selenium import webdriver   
from selenium.webdriver import ChromeOptions 
from selenium.webdriver.chrome.webdriver import WebDriver
import os      # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary             # パスを通すためのコード
import urllib.request
from pathlib import Path 
import time
from flask_test import *

@app.route('/send',methods =['POST','GET'])
def selenium():
  user_id = request.form.get("user_id")
  password = request.form.get("password")
  options = webdriver.ChromeOptions()
  options.add_experimental_option("prefs", {
    "download.default_directory": "〜\kwansei_file"
});
  chromedriver = 'chromedriver.exe'
  options.add_argument('--kiosk-printing')
  driver = webdriver.Chrome(options=options)  


  driver.get('https://luna.kwansei.ac.jp//')  # Googleを開く
  element = driver.find_element_by_name("login")
  element.click()
  search_bar_user= driver.find_element_by_name("username")
  search_bar_user.send_keys(user_id)
  search_bar_password = driver.find_element_by_name("password")
  search_bar_password.send_keys(password)
  element_log = driver.find_element_by_name("login")
  element_log.click()
  element_subject = driver.find_element_by_link_text("科目")
  element_subject.click()
  element_2021 = driver.find_element_by_link_text("2021")
  element_2021.click()
# ここまでが課題ページまで
  homeworks = ["スペイン語IV"]
  i=0;
  if not i==int(len(homeworks)):
   for search in homeworks:
    element_search=driver.find_element_by_partial_link_text(search)
    element_search.click()
    element_homework = driver.find_element_by_xpath("//ul[@class='courseMenu']/li[2]/*[@href]").get_attribute("href")
    driver.get(element_homework)
    pdfList=[]
    dlList=[]
#    if len(driver.find_element_by_xpath("//ul[@class='attachments clearfix']/li/*[@href]")> 0):
    links = driver.find_elements_by_xpath("//ul[@class='attachments clearfix']/li/*[@href]")
    if len(links)>0:
     for elem in links:
      if elem == int(len(links)):
       break
      print(elem.get_attribute("href"))
      pdfList.append(elem.get_attribute("href"))
     for download in pdfList:
      if download == int(len(pdfList)):
          break
      driver.get(download)
      driver.execute_script('window.print();')
      time.sleep(5)
      driver.back()
      time.sleep(3)
     element_title=driver.find_element_by_partial_link_text("お知らせ")
     element_title.click()
     dlList.append(element_title.get_attribute("href"))
     for download in pdfList:
       if download == int(len(dlList)):
          break
       driver.get(download)
       driver.execute_script('window.print();')
       time.sleep(5)
       driver.back()
    else:
     driver.back()
     element_title=driver.find_element_by_partial_link_text("お知らせ")
     element_title.click()
     dlList.append(element_title.get_attribute("href"))
     for download in pdfList:
      if download == int(len(dlList)):
          break
      driver.get(download)
      driver.execute_script('window.print();')
      time.sleep(5)
      driver.back()
    