# SQL Insights

This folder contains SQL scripts that generate **actionable insights** from YouTube data. These insights are based on the dataset extracted by the ETL pipeline, which runs automatically every hour.

## Purpose

The SQL queries analyze video performance based on **category**, **recency**, and **viewership trends**. These insights can support:

- Identifying the top-performing videos in each category  
- Surfacing newly published videos that gained traction quickly  
- Understanding average viewership patterns across categories  

## Contents

- `top_5_most_viewed_youtube_videos_by_category.sql`  
  Extracts the top 5 most viewed videos for each category using window functions.

- `recent_popular_videos.sql`  
  Lists videos published within the last 24 hours that have over 1 million views.

- `average_view_count_by_category.sql`  
  Calculates the average view count per category to reveal overall audience interest.

## Use Case

These scripts turn raw video metadata into **insightful summaries** for content teams, marketers, or platform analysts to act on — from trend spotting to strategy development.
You can extract even more tailored insights by running your own custom queries directly on the dataset, which is updated regularly by the ETL pipeline.
