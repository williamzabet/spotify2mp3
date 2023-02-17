#!/usr/bin/env python
# coding: utf-8

# In[1]:


import base64
import requests
import json
from googleapiclient.discovery import build
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import os


# In[5]:


# Enter the link for the spotify playlist you would like to download, make sure you only put the characters
    # after https://open.spotify.com/playlist/
spotify_playlist_id = ''

# Enter the client ID and Client Secret ID given to you from Spotify's API
spotify_client_id = ""
spotify_client_secret = ""

# Enter your key from Youtube's API
youtube_key = ""

# Enter the path to the chromedriver executable
# You can download it from https://sites.google.com/a/chromium.org/chromedriver/downloads
# Make sure to use the version of chromedriver that matches your version of Chrome
chromeDriver_path = ""

# Set the path to the folder where you want to save the MP3 files
playlist_path = ""


# In[6]:


def spotify2mp3(spotify_playlist_id, spotify_client_id, spotify_client_secret, youtube_key, 
                chromeDriver_path, playlist_path):
    
    # Set up client ID and client secret
    client_id = spotify_client_id
    client_secret = spotify_client_secret

    # Encode client ID and client secret as base64 string
    client_creds = f"{client_id}:{client_secret}"
    client_creds_b64 = base64.b64encode(client_creds.encode())

    # Set up token endpoint URL
    token_url = 'https://accounts.spotify.com/api/token'

    # Set up headers and data for token request
    token_headers = {
        "Authorization": f"Basic {client_creds_b64.decode()}"
    }
    token_data = {
        "grant_type": "client_credentials"
    }

    # Send POST request to token endpoint
    response = requests.post(token_url, headers=token_headers, data=token_data)

    # Get access token from response JSON
    access_token = response.json()['access_token']

    # Print access token
    print("Your Spotify access token is: ", access_token)
    
    #################################################################################
    
    endpoint = f"https://api.spotify.com/v1/playlists/{spotify_playlist_id}/tracks"

    # Set up API headers with access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Send GET request to API endpoint
    response0 = requests.get(endpoint, headers=headers)

    # Get track names and artist names from response0
    tracks = response0.json()['tracks']['items']
    playlist = []
    for i in range(len(tracks)):
        song = tracks[i]['track']['name']
        artist = tracks[i]['track']['artists'][0]['name']
        playlist.append(song + " by " + artist + " audio")
        
    #################################################################################

    api_key = youtube_key

    youtube = build('youtube', 'v3', developerKey=api_key)

    video_links = []

    for song in playlist:
        search_response = youtube.search().list(
            q=song,
            type='video',
            part='id,snippet',
            maxResults=1
        ).execute()

  
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                video_links.append('https://www.youtube.com/watch?v=' + search_result['id']['videoId'])
                
    #################################################################################

    # Set the path to the chromedriver executable
    driver_path = chromeDriver_path

    # Set the path to the folder where you want to save the MP3 files
    download_folder = playlist_path

    # Set up the Chrome webdriver with options to automatically download files to the specified folder
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': download_folder, 'safebrowsing.enabled': 'false'}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=options)

    # Loop through the list of video links and convert each one to an MP3 file
    counter = 0
    playlist_length = len(video_links)
    for link in video_links:
        # Load the tomp3.cc website
        driver.get('https://tomp3.cc/en41')
    
        # Find the input box and submit button, found them by their unique id's
        input_box = driver.find_element("id", "k__input")

        submit_button = driver.find_element("id", "btn-start")
    
        # Enter the video link and click the submit button
        input_box.send_keys(link)
        submit_button.click()
    
        # Wait for the result
        time.sleep(3)
    
        # Find the convert button and click it
        convert_button = driver.find_element("id", "btn-convert")
        convert_button.click()
    
        # Wait for the download button to appear
        time.sleep(3)
    
        # Find the download button and click it
        download_button = driver.find_element("id", "asuccess")
        download_button.click()
        
        # Wait for the download to finish
        song = playlist[counter]
        counter += 1
        output = "Successfully downloaded song " + str(counter) + "/" + str(playlist_length) + ": " + song
        print(" ")
        print(output)
        time.sleep(5)

    # Quit the webdriver
    driver.quit()
    
    #################################################################################

    folder_path = playlist_path

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an mp3 and starts with "tomp3.cc - "
        if filename.endswith('.mp3') and filename.startswith('tomp3.cc - '):
            # Rename the file by removing the "tomp3.cc - " prefix
            new_filename = filename[len('tomp3.cc - '):]
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))


# In[4]:


spotify2mp3(spotify_playlist_id, spotify_client_id, spotify_client_secret, youtube_key, 
                chromeDriver_path, playlist_path)


# In[ ]:




