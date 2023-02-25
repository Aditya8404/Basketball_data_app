import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import image
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "nba_img.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "output.csv")

# st.title("Dashboard - Iris Data")
st.title('NBA Player Stats Explorer')

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)

st.header('User Input Features')

# Sidebar - Team selection
sorted_unique_team = sorted(df.Tm.unique())
selected_team = st.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar - Position selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = df[(df.Tm.isin(selected_team)) & (df.Pos.isin(selected_pos))]

st.header('Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(f)