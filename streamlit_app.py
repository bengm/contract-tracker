import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import time
import re

st.title("Contracts Tracker")

# Get the data, put it in a dataframe
url = "https://www.doge.gov/savings"

print(time.time())
session = HTMLSession()
r = session.get(url)
r.html.render()
html = r.html.html

# df_list = pd.read_html(html)

st.write(html)

# contracts = pd.DataFrame(data_json)

# Layer in the classifications
def categorize(row):
    # regexes to capture keywords that match each category
    re_sub = r'SUBSCRIPTION|BLOOMBERG|POLITICO|WALL STREET JOURNAL|WASHINGTON POST'
    re_dei = r'DEI|DIVERSITY|EQUITY|INCLUSION|JUSTICE|EEO|RACIAL|ETHNIC|YOUTH|UNCONSCIOUS BIAS'
    re_env = r'ENVIRONMENT|CLIMATE'
    re_con = r'COACHING|CONSULT|COMMUNICATION|TRAINING|PROGRAM OFFICE|PROGRAM MANAGER|STRATEGIC|SUBJECT MATTER EXPERT|ADVISORY'
    # handle None values and also shorten references to cols
    descr = row['description'] or ''
    vendor = row['vendor'] or ''
    # agency = row['agency'] or ''
    if re.search(re_sub, descr+vendor):
        return "subscription"
    elif re.search(re_dei, descr):
        return "DEI"
    elif re.search(re_env, descr):
        return "environment"
    elif re.search(re_con, descr):
        return "consulting"
    else:
        return "other"
    
# contracts['category'] = contracts.apply(categorize, axis=1)

# Setup the controls & sidebar
opt_display = st.sidebar.selectbox(
    'View by',
    ('Detail', 'By Agency', 'By Company')
)

# Display the dataframe
# st.write(contracts)

