from youtube_pipeline import Extract, Transform, Load_CSV, Load_SQL
import os 
from dotenv import load_dotenv


load_dotenv()

#  API key here
api_key = os.getenv('YOUTUBE_API_KEY')
if not api_key:
    raise ValueError("API key is missing or empty")

# Functions here
raw_data = Extract(api_key)
transformed_data = Transform(raw_data)

Load_CSV(transformed_data, 'clean_youtube_data.csv')
Load_SQL(transformed_data)
