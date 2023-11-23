# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 02:04:21 2023

@author: Kranthi

"""
# Import required libraries

from pytube import YouTube

#destination = input("Enter the destination location to save songs: ")
video_link = input("Enter the youtubeurl: ")


try:
    selected_video = YouTube(video_link)
    audio = selected_video.streams.filter(only_audio=True, subtype='mp4', abr="128kbps").first()
    audio.download("./songs")
    print("Download Completed Successfully")
except Exception as e:
        print(f"An error occurred: {str(e)}")
