# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:43:12 2024

@author: Owner
"""
import os
from datetime import datetime
import time
import pandas as pd
import numpy as np
import gspread
from google.oauth2.service_account import Credentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import streamlit as st
import plotly.express as px
pd.options.display.max_columns = None

# https://streamlit.io/gallery
# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Stone Oak Live Dashboard",layout="wide",page_icon=":keyboard:")
# Title
st.title(":keyboard: Dough Gameplan")
st.header('Inputs')
################################### Inputs
time_stamp = datetime.now().strftime('%Y-%m-%d') #'2024-04-29_15' hourly_2024-04-30_13
day = pd.to_datetime(time_stamp).strftime('%A')
current_sales_df = pd.read_csv(r"stats.csv").drop(columns='Unnamed: 0').rename(columns={'xValues':'Date'})
# Clean col names
clean_col_names = []
for col in current_sales_df.columns:
    clean_col_names.append(col.split(',')[0].strip())
current_sales_df.columns = clean_col_names
current_sales_df['Date'] = pd.to_datetime(current_sales_df['Date']).dt.strftime('%Y-%m-%d')
# Rotate DF
cookie_names = [col for col in current_sales_df.columns if col not in ['Time', 'Date']]
current_sales_df0 = current_sales_df[cookie_names].sum().reset_index().rename(columns={'index':'Cookie',0:'Cookies Sold'})
current_sales_df0['Current Pcts'] = current_sales_df0['Cookies Sold'].values/current_sales_df0['Cookies Sold'].sum()
current_sales_df1 = current_sales_df0[current_sales_df0['Current Pcts'] > .05].copy()

display_df = current_sales_df1.pivot_table(index='Cookie', margins=True, margins_name='Total',aggfunc='sum').sort_values(by='Cookies Sold').reset_index()
# cell_hover = {
# "selector": "td:hover",
# "props": [("background-color", "#ffc0cb")]
# }
# index_names = {
#     "selector": ".index_name",
#     "props": "font-style: bold; font-weight:normal;"
# }
# headers = {
# "selector": "th:not(.index_name)",
# "props": "background-color: #ffc0cb; color: black;"
# }
st.table(display_df) #.set_table_styles([cell_hover, index_names, headers])
































































