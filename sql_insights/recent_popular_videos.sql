CREATE TABLE IF NOT EXISTS recent_popular_videos(
title TEXT NOT NULL,
published_at TIMESTAMP NOT NULL,
channel_title TEXT NOT NULL,
viewcount INT NOT NULL,
categoryid INT NOT NULL
);

INSERT INTO recent_popular_videos(
SELECT title, published_at, channel_title, viewcount, categoryid
FROM youtube_data
WHERE published_at >= NOW() - INTERVAL '24 hours' AND viewcount > 1000000
);

SELECT *
FROM recent_popular_videos
