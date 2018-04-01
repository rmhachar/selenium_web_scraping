# Step 1: Import Packages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import re
import pandas as pd
import numpy as np

from lib.functions import get_columns, get_info

# Load Firefox webdriver
driver = webdriver.Firefox(executable_path='')
    # you'll have to download geckodriver and route the path towards its location

AAPL_url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
AMZN_url = 'https://finance.yahoo.com/quote/AMZN?p=AMZN'
FB_url = 'https://finance.yahoo.com/quote/FB?p=FB'
TWTR_url = 'https://finance.yahoo.com/quote/TWTR?p=TWTR'
    
url_list = [AAPL_url,AMZN_url,FB_url,TWTR_url]

i = 0

df = get_columns(url_list[1])

for url in url_list:
    info = get_info(url)
    df.loc[i] = info
    i+=1
    
df
