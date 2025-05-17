CREATE TABLE IF NOT EXISTS average_view_count_by_category(
average_views NUMERIC NOT NULL,
categoryid INT NOT NULL
);

INSERT INTO average_view_count_by_category(
SELECT ROUND(AVG(viewcount),2) AS average_views, categoryid
FROM youtube_data
GROUP BY categoryid
ORDER BY average_views DESC
);

SELECT *
FROM average_view_count_by_category
