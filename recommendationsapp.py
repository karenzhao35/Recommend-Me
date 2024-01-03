
# Import necessary libraries 
import spotipy
import streamlit as st
from spotipy.oauth2 import SpotifyClientCredentials
from . import sp

def get_recommendations(track_name):
    # Get track URI
    results = sp.search(q=track_name, type='track')
    track_uri = results['tracks']['items'][0]['uri']

    # Get recommended tracks
    recommendations = sp.recommendations(seed_tracks=[track_uri])['tracks']
    return recommendations

st.title("Music Recommendation System")
track_name = st.text_input("Enter a song name:")

if track_name:
    recommendations = get_recommendations(track_name)
    st.write("Recommended songs:")
    for track in recommendations:
        st.write(track['name'])
        st.image(track['album']['images'][0]['url'])
