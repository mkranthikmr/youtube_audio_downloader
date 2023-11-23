# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 02:04:21 2023

@author: Kranthi

"""
# Import required libraries

from pytube import YouTube

destination = r"F:\Python Projects\mp3downloader\songs"
video_link = "https://www.youtube.com/watch?v=5Eqb_-j3FDA"


try:
    selected_video = YouTube(video_link)
    audio = selected_video.streams.filter(only_audio=True, subtype='mp4', abr="128kbps").first()
    audio.download(destination)
    print("Download Completed Successfully")
except Exception as e:
        print(f"An error occurred: {str(e)}")
