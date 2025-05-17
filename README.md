# YouTube ETL Project

## Overview
This project implements an ETL pipeline that extracts data on the top 50 viral YouTube videos in the US, cleans and transforms the data, then loads the processed results both into a CSV file and a PostgreSQL database.

## Technologies Used
- Python 
- Apache Airflow 
- YouTube Data API 
- Pandas 
- PostgreSQL 


## Project Motivation
This is a personal project developed to apply and test skills acquired in data engineering, including API integration, data processing, and pipeline orchestration.

## Project Scope and Limitations
Originally, the project was intended to include an email notification step using Airflow's EmailOperator to notify a hypothetical team when new data was pulled from the API and is ready for data analysis and visualization. However, this feature was dropped due to version conflicts in the current development environment.

## License
This project is for educational and portfolio use. Not affiliated with YouTube or Google.

## How to Run

1. Configure your `.env` file with YouTube API key and PostgreSQL credentials.  
2. Start Apache Airflow with the provided `docker-compose.yaml`.  
3. Trigger the ETL DAG (`youtube_etl_dag`) via Airflow UI or CLI.  
4. Check the output CSV file and PostgreSQL database for results.

## Built by Brix — for learning, showcasing, and fun.
![Screenshot 2025-05-18 031517](https://github.com/user-attachments/assets/6958086e-2f18-46a5-8e6b-917aed938306)
