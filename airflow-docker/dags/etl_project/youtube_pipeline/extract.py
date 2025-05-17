import requests 
import pandas as pd 
import numpy as np 
import os 
from dotenv import load_dotenv

load_dotenv()


def Extract(api_key=None):
    if not api_key:
        api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        raise ValueError("API key is missing or empty")

    """
    Extracts the 20 most popular YouTube videos in the US region using the YouTube Data API.

    :param api_key: this can be obtained via google's Youtube API 
    :returns: A pandas DataFrame containing video details like videoId, title, viewCount, etc.
    :rtype: pandas.DataFrame

    """
    
    url = 'https://www.googleapis.com/youtube/v3/videos'
    params={'regionCode':'US', 'chart': 'mostPopular', 'part': 'snippet,statistics,contentDetails', 'maxResults': 50, 'key': api_key}
    
    response = requests.get(url, params=params)
    json_data = response.json()

    video_data = []  
    
    for video in json_data['items']:
        
        video_dict = {
            'videoId': video['id'],  
            'title': video['snippet']['title'],  
            'publishedAt': video['snippet']['publishedAt'],  
            'channelTitle': video['snippet']['channelTitle'],  
            'viewCount': video['statistics'].get('viewCount', 0),  
            'likeCount': video['statistics'].get('likeCount', 0),  
            'commentCount': video['statistics'].get('commentCount', 0),  
            'duration': video['contentDetails']['duration'],  
            'categoryId': video['snippet']['categoryId'],  
        }
        video_data.append(video_dict)
        
    raw_data = pd.DataFrame(video_data)
    return raw_data
    

