-- Step 1: Created a table
CREATE TABLE IF NOT EXISTS top_5_most_viewed_youtube_videos_by_category(
title TEXT NOT NULL,
categoryid INT NOT NULL, 
channel_title TEXT NOT NULL, 
viewcount INT NOT NULL, 
likecount INT NOT NULL
);

-- Step 2: Made a CTE on extracting top 5 by the use of window functions
WITH rank as (
SELECT ROW_NUMBER() OVER(PARTITION BY categoryid ORDER BY viewcount DESC) AS rn, title, categoryid, channel_title, viewcount, likecount
FROM youtube_data
)

  -- Step 3: Inserted the data into the table
INSERT INTO top_5_most_viewed_youtube_videos_by_category(
SELECT title, categoryid, channel_title, viewcount, likecount
FROM rank
WHERE rn <=5
);

  -- Read
SELECT * 
FROM top_5_most_viewed_youtube_videos_by_category
