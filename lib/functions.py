# STEP 1: Load packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import re
import pandas as pd
import numpy as np

def get_columns(url):
  # go to the page
  driver.get(url)
  
  titles_element = driver.find_elements_by_xpath("//td[@class='C(black) W(51%)']")

  # save titles

  titles = []
  for x in titles_element:
    titles.append(x.text)

  # add 'Ticker' to column labels

  titles2 = ['Ticker'] + titles
  
  # create dataframe with column labels
  
  df = pd.DataFrame(columns=titles2)

  return df
  
def get_info(url):
  
  # go to web page
  driver.get(url)
  
  # get financial values

  values_element = driver.find_elements_by_xpath("//td[@class='Ta(end) Fw(b) Lh(14px)']")

  values = [x.text for x in values_element]
  
  # find name and ticker
  
  ticker = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/div[1]/h1')
  
  ticker2 = []
  for x in ticker:
    ticker2.append(x.text)
  
  # combine company name and values
  values2 = []
  values2 = [ticker2] + values

  return values2
