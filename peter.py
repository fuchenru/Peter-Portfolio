#!/usr/bin/env python
# coding: utf-8

# In[1]:

import time

import streamlit as st

import numpy as np
import pandas as pd

import webbrowser


### Header:
st.set_page_config(page_title='Peter Fu Chen\'s Portfolio', layout='wide')
st.title('Peter Fu Chen\'s Portfolio')
st.write('Always enjoy exploring insights from data and developing workable solutions to the problems')

### Summary
st.subheader('Summary')
file_path = 'summary.txt'

# Read the contents of the text file
with open(file_path, 'r') as file:
    text_content = file.read()

# Display the text using Streamlit
st.write(text_content)

### Project
st.subheader('Project')
st.write('Projects done in University of Chicago and Michigan State')

left_column, right_column = st.columns(2)

left_column.image('TD.png')
left_column.write('TradingHero')
left_column.link_button("Check it out!", "https://github.com/fuchenru/TradingHero")

right_column.image('sentiment.jpg')
right_column.write('Financial Sentiment Analysis')
right_column.link_button("Check it out!", "https://huggingface.co/fuchenru/Trading-Hero-LLM")

left_column.image('Time-Series-Analysis.jpg')
left_column.write('Time Series Analysis on Gold')
left_column.link_button("Check it out!", "https://github.com/fuchenru/Time-Series-Analysis-on-Gold")

left_column.image('traffic.png')
left_column.write('NYC Traffic Accidents Analysis')
left_column.link_button("Check it out!","https://github.com/hty0731/AWS")

left_column.image('rat.png')
left_column.write('Visualizing New York City Rat Problem')
left_column.link_button("Check it out!","https://github.com/fuchenru/Visualizing-New-York-City-Rat-Problem")

right_column.image('penny.png')
right_column.write('Real time penny stock pump and dump trading strategy')
right_column.link_button("Check it out!","https://github.com/fuchenru/Penny-stock-pump-and-dump-trading-strategy")

right_column.image('chart.png')
right_column.write('Stock Chart Analyzer')
right_column.link_button("Check it out!","https://github.com/fuchenru/Stock-Chart-Analyzer")

right_column.image('co2.jpg')
right_column.write('How have carbon emissions affected climate change?')
right_column.link_button("Check it out!","https://github.com/fuchenru/How-have-carbon-emissions-affected-climate-change-")

### Skills
st.subheader('Skills')

col1,col2,col3,col4 = st.columns(4)
with col1:
    st.success('Data Engineering')
    st.info('Data Integration')
    st.warning('Database Management')

with col2:
    st.info('Generative AI')
    st.warning('Real-Time Data Processing')
    st.error('Data and Information Visualization')

with col3:
    st.warning('Regression Analysis')
    st.error('Data Modeling')
    st.success('Time Series Analysis')

with col4:
    st.success('Cloud Platform')
    st.info('Data Governance')
    st.warning('Business Intelligence')


### Sidebar
st.sidebar.write('Hello! This is Peter!')
#Insert image
st.sidebar.image('self.JPG')
#Insert words
st.sidebar.write('Wish to connect?')
email = 'fuchenru@uchicago.edu'
linkedin_profile_url = 'https://www.linkedin.com/in/peterfuchen'
resume_url = 'https://drive.google.com/file/d/1YjCqrtd5llb0bzYKe_jZXNpCSaL_qydL/view?usp=sharing'

# Create a button
if st.sidebar.button('Connect via email'):
    # Open the default email client
    subject = 'Invitation to connect'
    body = 'Dear Peter'
    webbrowser.open(f'mailto:{email}?subject={subject}&body={body}')
    
# Create a button
st.sidebar.link_button("Visit LinkedIn","https://www.linkedin.com/in/peterfuchen")
st.sidebar.link_button("Visit Resume","https://drive.google.com/file/d/1YjCqrtd5llb0bzYKe_jZXNpCSaL_qydL/view?usp=sharing")

