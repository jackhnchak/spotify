import streamlit as st 
import joblib 
import pandas as pd 
from scipy.sparse import csr_matrix 
from sklearn.neighbors import NearestNeighbors
import numpy as np 
@st.cache(allow_output_mutation=True)
def load_data(path):
    song_rec = pd.read_pickle(path)
    return song_rec
def find_similarity(df, song_name): 
    df2 = df[[song_name]].sort_values(by = song_name, ascending = False)
    df2.rename(columns = {song_name : 'song_recommendations'}, inplace = True)
    return df2.head(10)
st.title("Song Recommendation System")
st.write("Just tell us your favorite song and we will give you some recommendations.")
data = load_data('/Users/jackchak/Documents/GitHub/spotify/cos_sim.zip')

option = st.selectbox('Please select your favorite song', (data.columns))
st.write('You have selected:', option)

if (st.button('Get Song Recommendations')):
    result = find_similarity(data,option)
    result.columns = ['Songs you might like']
    st.write(result)
    #st.balloons()