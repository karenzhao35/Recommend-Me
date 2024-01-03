import streamlit as st
from recommendationsapp import *

st.set_page_config(layout="wide")
st.title("Recommend Me")
track_name = st.text_input("Enter a song name:")

if track_name:
    recommendations = get_recommendations(track_name)
    st.write("Recommended songs:")
    length = len(recommendations)
    it = 0
    while it != length: 
        columns = st.columns(4, gap="large")
        for cols in columns:
            if it == length: break
            with cols:
                # st.write(recommendations[it]['name'])
                st.image(recommendations[it]['album']['images'][0]['url'], caption=recommendations[it]['name'])
                it += 1
            
        
        
with st.sidebar:
	# input widget 1
	# input widget 2
    st.write("hi")



